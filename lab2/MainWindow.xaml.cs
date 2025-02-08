using System;
using System.Windows;
using System.Windows.Input;
using System.Windows.Media;

namespace Lab2_WPF
{
    public partial class MainWindow : Window
    {
        private int counter = 0;
        private const int VariantNumber = 3; 

        public MainWindow()
        {
            InitializeComponent();
        }

        private void Window_MouseDown(object sender, MouseButtonEventArgs e)
        {
            int previousCounter = counter;

            if (e.LeftButton == MouseButtonState.Pressed) // ЛКМ
            {
                counter++;
            }
            else if (e.RightButton == MouseButtonState.Pressed) // ПКМ
            {
                counter -= 2;
            }

            UpdateCounterDisplay();
            CheckConditions(previousCounter);
        }

        private void UpdateCounterDisplay()
        {
            CounterLabel.Content = $"Счётчик: {counter}";
            CounterLabel.Foreground = counter < 0 ? Brushes.Red : Brushes.DarkBlue;
        }

        private void CheckConditions(int previousValue)
        {
            // Проверка совпадения с номером варианта
            if (counter == VariantNumber)
            {
                MessageBox.Show($"Совпадение с вариантом {VariantNumber}!", "Внимание",
                              MessageBoxButton.OK, MessageBoxImage.Information);
            }

            // Проверка изменения знака
            bool wasPositive = previousValue >= 0;
            bool nowPositive = counter >= 0;

            if (wasPositive != nowPositive)
            {
                string message = nowPositive ? "Значение стало положительным!" : "Значение стало отрицательным!";
                MessageBox.Show(message, "Смена знака", MessageBoxButton.OK, MessageBoxImage.Warning);
            }
        }
    }
}