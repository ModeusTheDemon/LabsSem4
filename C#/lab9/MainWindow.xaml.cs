using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Windows;
using StudentApp.Models;

namespace StudentApp
{
    public partial class MainWindow : Window
    {
        private List<Student> students = new List<Student>();

        public MainWindow()
        {
            InitializeComponent();
            LoadStudents();
            StudentsGrid.ItemsSource = students;
        }

        private void LoadStudents()
        {
            if (File.Exists("students_list.txt"))
            {
                foreach (var line in File.ReadAllLines("students_list.txt"))
                {
                    var parts = line.Split(';');
                    if (parts.Length == 7)
                    {
                        students.Add(new Student
                        {
                            LastName = parts[0],
                            FirstName = parts[1],
                            Patronymic = parts[2],
                            BirthDate = DateTime.Parse(parts[3]),
                            Height = double.Parse(parts[4]),
                            City = parts[5],
                            PhoneNumber = parts[6]
                        });
                    }
                }
            }
        }

        private void FilterMoscow_Click(object sender, RoutedEventArgs e) =>
            StudentsGrid.ItemsSource = students.Where(s => s.City == "Москва").ToList();

        private void FilterAdults_Click(object sender, RoutedEventArgs e) =>
            StudentsGrid.ItemsSource = students.Where(s => s.Age >= 18).ToList();

        private void FilterByYear_Click(object sender, RoutedEventArgs e)
        {
            if (int.TryParse(YearBox.Text, out int year))
            {
                StudentsGrid.ItemsSource = students.Where(s => s.BirthDate.Year == year).ToList();
            }
        }

        private void ShowIntro_Click(object sender, RoutedEventArgs e)
        {
            StudentsGrid.ItemsSource = students.Select(s => new
            {
                s.LastName,
                s.FirstName,
                Age = s.Age,
                s.City
            }).ToList();
        }

        private void SortByDistance_Click(object sender, RoutedEventArgs e)
        {
            var ordered = students.OrderByDescending(s => GetDistanceFromMoscow(s.City))
                                   .ThenByDescending(s => s.LastName).ToList();
            StudentsGrid.ItemsSource = ordered;
        }

        private double GetDistanceFromMoscow(string city)
        {
            Dictionary<string, double> distances = new Dictionary<string, double>
            {
                { "Москва", 0 },
                { "Санкт-Петербург", 635 },
                { "Новосибирск", 2811 },
                { "Екатеринбург", 1790 },
                { "Казань", 820 },
                { "Нижний Новгород", 400 },
                { "Красноярск", 3360 },
                { "Омск", 2700 },
                { "Самара", 1050 },
                { "Ростов-на-Дону", 1100 }
            };

            return distances.TryGetValue(city, out double distance) ? distance : 1500;
        }

        private void GroupByPhoneCode_Click(object sender, RoutedEventArgs e)
        {
            StudentsGrid.ItemsSource = students.OrderBy(s => s.PhoneCode).ToList();
        }

        private void AddStudent_Click(object sender, RoutedEventArgs e)
        {
            var window = new AddStudentWindow();
            if (window.ShowDialog() == true)
            {
                students.Add(window.NewStudent);
                StudentsGrid.ItemsSource = null;
                StudentsGrid.ItemsSource = students;
                File.AppendAllText("students_list.txt", $"{window.NewStudent.LastName};{window.NewStudent.FirstName};{window.NewStudent.Patronymic};{window.NewStudent.BirthDate:yyyy-MM-dd};{window.NewStudent.Height};{window.NewStudent.City};{window.NewStudent.PhoneNumber}\n");
            }
        }
    }
}