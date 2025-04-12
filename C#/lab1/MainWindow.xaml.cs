using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace lab1
{
    /// <summary>
    /// Логика взаимодействия для MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
            MinHeight = 400;
            MinWidth = 600;
            MaxHeight = 800;
            MaxWidth = 1000;
            Title = "Бондаренко Ярослав lab1";
            Background = (Brush)System.ComponentModel.TypeDescriptor.GetConverter(typeof(Brush)).ConvertFromInvariantString("Red");
        }

        public void OnMouseLeftButtonDown(object sender, MouseButtonEventArgs e)
        {
            if (Background == (Brush)System.ComponentModel.TypeDescriptor.GetConverter(typeof(Brush)).ConvertFromInvariantString("Red"))
            {
                Background = (Brush)System.ComponentModel.TypeDescriptor.GetConverter(typeof(Brush)).ConvertFromInvariantString("Green");
            }
            else
            {
                Background = (Brush)System.ComponentModel.TypeDescriptor.GetConverter(typeof(Brush)).ConvertFromInvariantString("Red");
            }
        }

        public void OnMouseRightButtonDown(object sender, MouseButtonEventArgs e)
        {
            if (WindowState == WindowState.Normal)
            {
                WindowState = WindowState.Maximized;
            }
            else if (WindowState == WindowState.Maximized)
            {
                WindowState = WindowState.Minimized;
            }
            else
            {
                WindowState = WindowState.Normal;
            }
        }

        public void OnKeyDown(object sender, KeyEventArgs e)
        {
            if (e.Key == Key.Space)
            {
                double CommonWidth = (MaxWidth + MinWidth) / 2;
                double CommonHeight = (MaxHeight + MinHeight) / 2;

                Width = CommonWidth + (CommonWidth - Width);
                Height = CommonHeight + (CommonHeight - Height);
            }
            else if (e.Key == Key.Escape)
            {
                Close();
            }
        }
    }
}
