using System;
using System.Windows;
using System.Windows.Controls;
using StudentApp.Models;

namespace StudentApp
{
    public partial class AddStudentWindow : Window
    {
        public Student NewStudent { get; private set; }

        public AddStudentWindow()
        {
            InitializeComponent();
        }

        private void AddButton_Click(object sender, RoutedEventArgs e)
        {
            try
            {
                NewStudent = new Student
                {
                    LastName = LastNameBox.Text,
                    FirstName = FirstNameBox.Text,
                    Patronymic = PatronymicBox.Text,
                    BirthDate = BirthDatePicker.SelectedDate ?? DateTime.Today,
                    Height = double.Parse(HeightBox.Text),
                    City = (CityBox.SelectedItem as ComboBoxItem)?.Content.ToString(),
                    PhoneNumber = PhoneBox.Text
                };
                DialogResult = true;
                Close();
            }
            catch (Exception ex)
            {
                MessageBox.Show($"Ошибка ввода: {ex.Message}");
            }
        }
    }
}