using System;
using System.Windows;
using System.Windows.Input;
using System.Windows.Media;

namespace ColorSliderApp
{
    public partial class MainWindow : Window
    {
        private int _randomClicks = 0;
        private const int MaxClicks = 5;

        public MainWindow()
        {
            InitializeComponent();
            UpdateColor();
            MouseWheel += OnMouseWheel;
        }

        // Собственная реализация Clamp для .NET Framework
        private double Clamp(double value, double min, double max)
        {
            return value < min ? min : (value > max ? max : value);
        }

        private void UpdateColor()
        {
            byte alpha = (byte)(AlphaSlider.Value * 2.55);

            var color = Color.FromArgb(
                alpha,
                (byte)RedSlider.Value,
                (byte)GreenSlider.Value,
                (byte)BlueSlider.Value
            );

            RectColor.Color = color;
            HiddenLabel.Foreground = new SolidColorBrush(Color.FromRgb(
                (byte)(255 - color.R),
                (byte)(255 - color.G),
                (byte)(255 - color.B)
            ));

            HiddenLabel.Visibility = (AlphaSlider.Value <= 75) ? Visibility.Hidden : Visibility.Visible;
            RandomButton.IsEnabled = _randomClicks < MaxClicks && (100 - AlphaSlider.Value) >= 25;
        }

        private void Slider_ValueChanged(object sender, RoutedPropertyChangedEventArgs<double> e)
        {
            UpdateColor();
        }

        private void RandomButton_Click(object sender, RoutedEventArgs e)
        {
            var rnd = new Random();
            RedSlider.Value = rnd.Next(0, 256);
            GreenSlider.Value = rnd.Next(0, 256);
            BlueSlider.Value = rnd.Next(0, 256);
            _randomClicks++;
            UpdateColor();
        }

        private void OnMouseWheel(object sender, MouseWheelEventArgs e)
        {
            AlphaSlider.Value += e.Delta > 0 ? 5 : -5;
            AlphaSlider.Value = Clamp(AlphaSlider.Value, 0, 100); // Используем свою Clamp
            UpdateColor();
        }

        private void AlphaSlider_ValueChanged(object sender, RoutedPropertyChangedEventArgs<double> e)
        {
            UpdateColor();
        }
    }
}