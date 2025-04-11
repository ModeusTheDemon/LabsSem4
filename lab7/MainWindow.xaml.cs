using System;
using System.Windows;
using System.Windows.Media;

namespace Lab7
{
    public partial class MainWindow : Window 
    {
        private int _clickCount;
        private const int _maxClickCount = 5;
        private byte alpha = 255;


        public MainWindow()
        {
            InitializeComponent();

            sliderR.ValueChanged += (s, e) => UpdateColor();
            sliderG.ValueChanged += (s, e) => UpdateColor();
            sliderB.ValueChanged += (s, e) => UpdateColor();
            scrollVisibility.ValueChanged += (s, e) => UpdateVisibility();

            scrollVisibility.PreviewMouseWheel += (s, e) =>
            {
                scrollVisibility.Value += e.Delta > 0 ? 5 : -5;
                e.Handled = true;
            };
        }

        private void UpdateColor()
        {
            var color = Color.FromArgb(alpha, (byte)sliderR.Value, (byte)sliderG.Value, (byte)sliderB.Value);
            colorRect.Fill = new SolidColorBrush(color);
            lblText.Foreground = new SolidColorBrush(Color.FromRgb((byte)(255 - color.R), (byte)(255 - color.G), (byte)(255 - color.B)));
            txtR.Text = (color.R).ToString();
            txtG.Text = (color.G).ToString();
            txtB.Text = (color.B).ToString();
        }

        private void UpdateVisibility()
        {
            alpha = (byte)(255 * (scrollVisibility.Value / 100));
            btnRandom.IsEnabled = _clickCount < _maxClickCount && scrollVisibility.Value >= 25;
            UpdateColor();
        }

        private void BtnRandom_Click(object sender, RoutedEventArgs e)
        {
            var rnd = new Random();
            sliderR.Value = rnd.Next(0, 6) * 50; // 0, 50, 100...250
            sliderG.Value = rnd.Next(0, 6) * 50;
            sliderB.Value = rnd.Next(0, 6) * 50;
            _clickCount++;
            btnRandom.IsEnabled = _clickCount < _maxClickCount && scrollVisibility.Value >= 25;
        }

    }
}