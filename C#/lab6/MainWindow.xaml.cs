using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Media;

namespace UserForm
{
    public partial class MainWindow : Window
    {
        public class Country
        {
            public string Name { get; set; }
            public string Code { get; set; }
        }

        public MainWindow()
        {
            InitializeComponent();

            // Заполнение списка стран
            cmbCountry.ItemsSource = new List<Country>
            {
                new Country { Name = "Россия(+7)", Code = "+7" },
                new Country { Name = "США(+1)", Code = "+1" },
                new Country { Name = "Германия(+49)", Code = "+49" },
                new Country { Name = "Гренландия(+299)", Code = "+299" }
            };

            // Установка начального типа телефона
            lstPhoneType.SelectedIndex = 0;
            UpdatePhoneMask();
        }

        private void txtPhone_GotFocus(object sender, RoutedEventArgs e)
        {
            var textBox = sender as TextBox;
            // Очистка placeholder при получении фокуса
            if (textBox.Foreground == Brushes.Gray)
            {
                textBox.Text = "";
                textBox.Foreground = SystemColors.ControlTextBrush;
            }
        }

        private void txtPhone_LostFocus(object sender, RoutedEventArgs e)
        {
            var textBox = sender as TextBox;
            // Обновление маски, если поле пустое
            if (string.IsNullOrWhiteSpace(textBox.Text))
            {
                UpdatePhoneMask();
            }
        }

        private void txtPhone_TextChanged(object sender, TextChangedEventArgs e)
        {
            var textBox = sender as TextBox;
            if (textBox.Foreground == Brushes.Gray) return;

            string text = new string(textBox.Text.Where(c => char.IsDigit(c)).ToArray());
            string formattedText = FormatPhoneNumber(text, IsMobileSelected());

            textBox.Text = formattedText;
            textBox.CaretIndex = formattedText.Length;
        }

        private void lstPhoneType_SelectionChanged(object sender, SelectionChangedEventArgs e)
        {
            // Получаем текущие цифры из поля ввода
            string digits = new string(txtPhone.Text.Where(char.IsDigit).ToArray());

            // Очищаем поле и применяем новую маску
            txtPhone.Text = "";
            UpdatePhoneMask();

            // Если были введены цифры - форматируем их по новой маске
            if (!string.IsNullOrEmpty(digits))
            {
                txtPhone.Foreground = SystemColors.ControlTextBrush;
                txtPhone.Text = FormatPhoneNumber(digits, IsMobileSelected());
            }
        }

        private bool IsMobileSelected() =>
            (lstPhoneType.SelectedItem as ListBoxItem)?.Content.ToString() == "мобильный";

        private string FormatPhoneNumber(string digits, bool isMobile)
        {
            string formatted = "";
            if (isMobile)
            {
                if (digits.Length > 0) formatted = $"({digits.Substring(0, Math.Min(3, digits.Length))}";
                if (digits.Length > 3) formatted += $") {digits.Substring(3, Math.Min(3, digits.Length - 3))}";
                if (digits.Length > 6) formatted += $"-{digits.Substring(6, Math.Min(2, digits.Length - 6))}";
                if (digits.Length > 8) formatted += $"-{digits.Substring(8)}";
            }
            else
            {
                if (digits.Length > 0) formatted = digits.Substring(0, Math.Min(3, digits.Length));
                if (digits.Length > 3) formatted += $"-{digits.Substring(3, Math.Min(3, digits.Length - 3))}";
                if (digits.Length > 6) formatted += $"-{digits.Substring(6, Math.Min(2, digits.Length - 6))}";
                if (digits.Length > 8) formatted += $"-{digits.Substring(8)}";
            }
            return formatted;
        }

        private void UpdatePhoneMask()
        {
            bool isMobile = IsMobileSelected();
            txtPhone.Text = isMobile ? "(XXX) XXX-XX-XX" : "XXX-XXX-XX-XX";
            txtPhone.Foreground = Brushes.Gray;
        }

        private void BtnSubmit_Click(object sender, RoutedEventArgs e)
        {
            // Проверка заполнения всех полей
            if (cmbCountry.SelectedItem == null ||
                lstPhoneType.SelectedItem == null ||
                string.IsNullOrWhiteSpace(txtPhone.Text) ||
                txtPhone.Foreground == Brushes.Gray ||
                string.IsNullOrWhiteSpace(txtFullName.Text) ||
                string.IsNullOrWhiteSpace(txtBirthDate.Text))
            {
                MessageBox.Show("Заполните все поля!");
                return;
            }

            // Проверка даты рождения
            if (!DateTime.TryParse(txtBirthDate.Text, out DateTime birthDate) ||
                birthDate > DateTime.Now.AddYears(-18) ||
                birthDate < DateTime.Now.AddYears(-90))
            {
                MessageBox.Show("Некорректная дата рождения!");
                return;
            }

            // Проверка имени и фамилии
            if (txtFullName.Text.Count(prb => prb == ' ') > 1 ||
                !(txtFullName.Text.Split(' ').Length == 2))
            {
                MessageBox.Show("Некорректные имя или фамилия!");
                return;
            }

            // Проверка длины номера
            if (txtPhone.Text.Replace(" ", "").Replace("(", "").Replace(")", "").Replace("-", "").Length > 10)
            {
                MessageBox.Show("Некорректный номер телефона!");
                return;
            }

            // Сохранение данных
            string data = $"{DateTime.Now:yyyy-MM-dd HH:mm}|" +
                          $"{((Country)cmbCountry.SelectedItem).Code}|" +
                          $"{((ListBoxItem)lstPhoneType.SelectedItem).Content}|" +
                          $"{txtPhone.Text}|{txtFullName.Text}|{birthDate:dd.MM.yyyy}";

            try
            {
                File.AppendAllText("users.txt", data + "\n");
                MessageBox.Show("Данные сохранены!");
            }
            catch (Exception ex)
            {
                MessageBox.Show($"Ошибка: {ex.Message}");
            }
        }
    }
}