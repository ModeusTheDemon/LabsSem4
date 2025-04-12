using System;
using System.Windows;
using System.Windows.Controls;

namespace Lab3
{
    public partial class MainWindow : Window
    {
        int initialX;
        int initialY;
        int currentX;
        int currentY;
        int MovementX = 20;
        int MovementY = 20;

        public MainWindow()
        {
            InitializeComponent();
            initialX = (int)PointLabel.Margin.Left;
            initialY = (int)PointLabel.Margin.Top;
            currentX = initialX;
            currentY = initialY;
            UpdateButtonStates();
        }

        private void MovePoint(int deltaX, int deltaY)
        {
            int newX = currentX + deltaX;
            int newY = currentY + deltaY;

            if (newX >= 0 && newX <= (int)Width - PointLabel.ActualWidth &&
                newY >= 0 && newY <= (int)Height - PointLabel.ActualHeight)
            {
                currentX = newX;
                currentY = newY;
                PointLabel.Margin = new Thickness(currentX, currentY, 0, 0);
            }

            UpdateButtonStates();
        }

        private void UpdateButtonStates()
        {
            UpButton.IsEnabled = currentY - MovementY >= 0;
            DownButton.IsEnabled = currentY + 2 * MovementY <= (int)Height - PointLabel.ActualHeight;
            LeftButton.IsEnabled = currentX - MovementX >= 0;
            RightButton.IsEnabled = currentX + 2 * MovementX <= (int)Width - PointLabel.ActualWidth;
        }

        private void UpButton_Click(object sender, RoutedEventArgs e)
        {
            MovePoint(0, -MovementY);
        }

        private void DownButton_Click(object sender, RoutedEventArgs e)
        {
            MovePoint(0, MovementY);
        }

        private void LeftButton_Click(object sender, RoutedEventArgs e)
        {
            MovePoint(-MovementX, 0);
        }

        private void RightButton_Click(object sender, RoutedEventArgs e)
        {
            MovePoint(MovementX, 0);
        }

        private void InfoButton_Click(object sender, RoutedEventArgs e)
        {
            int deviationX = currentX - initialX;
            int deviationY = currentY - initialY;
            string message = $"Положение ({currentX};{currentY}) Отклонение ({deviationX};{deviationY})";
            MessageBox.Show(message, "Информация о положении точки");
        }
    }
}