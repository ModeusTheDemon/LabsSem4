using System.Windows;
using System.Windows.Controls;

namespace Lab4
{
    public partial class MainWindow : Window
    {
        string user1 = "Миша";
        string user2 = "Саша";

        public MainWindow()
        {
            InitializeComponent();
        }

        private void BtnCalculate_Click(object sender, RoutedEventArgs e)
        {
            bool isValid = true;
            ResetFieldColors();

            if (!int.TryParse(MishaApples.Text, out int mishaA) || mishaA < 0)
            {
                MishaApples.Background = System.Windows.Media.Brushes.LightPink;
                isValid = false;
            }

            if (!int.TryParse(SashaApples.Text, out int sashaA) || sashaA < 0)
            {
                SashaApples.Background = System.Windows.Media.Brushes.LightPink;
                isValid = false;
            }

            if (!int.TryParse(MishaPears.Text, out int mishaP) || mishaP < 0)
            {
                MishaPears.Background = System.Windows.Media.Brushes.LightPink;
                isValid = false;
            }

            if (!int.TryParse(SashaPears.Text, out int sashaP) || sashaP < 0)
            {
                SashaPears.Background = System.Windows.Media.Brushes.LightPink;
                isValid = false;
            }

            if (isValid)
            {
                LockFields(true);
                TbResult.Text = $"Всего яблок {mishaA + sashaA}, а груш {mishaP + sashaP}";
                TbResult.Visibility = Visibility.Visible;
            }
            else
            {
                MessageBox.Show("Проверьте правильность введённых данных!");
            }
        }

        private void BtnReset_Click(object sender, RoutedEventArgs e)
        {
            ResetFieldColors();
            LockFields(false);
            MishaApples.Text = SashaApples.Text = MishaPears.Text = SashaPears.Text = "";
            TbResult.Visibility = Visibility.Collapsed;
        }

        private void LockFields(bool isLocked)
        {
            MishaApples.IsEnabled = !isLocked;
            SashaApples.IsEnabled = !isLocked;
            MishaPears.IsEnabled = !isLocked;
            SashaPears.IsEnabled = !isLocked;
        }

        private void ResetFieldColors()
        {
            MishaApples.ClearValue(TextBox.BackgroundProperty);
            SashaApples.ClearValue(TextBox.BackgroundProperty);
            MishaPears.ClearValue(TextBox.BackgroundProperty);
            SashaPears.ClearValue(TextBox.BackgroundProperty);
        }
    }
}