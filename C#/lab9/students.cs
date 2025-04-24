using System;

namespace StudentApp.Models
{
    public class Student
    {
        public string LastName { get; set; }
        public string FirstName { get; set; }
        public string Patronymic { get; set; }
        public DateTime BirthDate { get; set; }
        public double Height { get; set; }
        public string City { get; set; }
        public string PhoneNumber { get; set; }

        public int Age => DateTime.Now.Year - BirthDate.Year - (DateTime.Now.DayOfYear < BirthDate.DayOfYear ? 1 : 0);

        public string PhoneCode => PhoneNumber?.Substring(4, 3);
    }
}