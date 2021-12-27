//dotnet new console --framework net6.0
//dotnet run


// See https://aka.ms/new-console-template for more information
using System.Linq;
using System.Collections.Generic;
using System;

namespace HelloWorld
{
    class Program
    {
        static void Main(string[] args)
        {
            IEnumerable<string> names = new List<string>() { "John", "Jane", "Joe" };
            IEnumerable<string> filteredNames = names.Where(name => name.StartsWith("J"));
            foreach (string name in filteredNames)
            {
                System.Console.WriteLine(name);
            }
            foreach (string name in names)
            {
                Console.WriteLine(name);
            }
            Func<int, int, int> add = (x, y) => x + y;
            int result = add(1, 2);
            System.Console.WriteLine(result);
            Console.WriteLine("Hello World!");

            string[] cities = { "London", "Paris", "Berlin", "Madrid", "Rome" };
            var query = from city in cities
                        where city.StartsWith("M")
                        orderby city
                        select city;
            foreach (string city in query)
            {
                Console.WriteLine(city);
            }

            // IEnumerable<string> movies = new List<Movie>
            // {
            //     new Movie() { Title = "The Shawshank Redemption", Rating = 9.2f, Year = 1994 },
            //     new Movie() { Title = "The Godfather", Rating = 9.2f, Year = 1972 },
            //     new Movie() { Title = "The Godfather: Part II", Rating = 9.0f, Year = 1974 },
            //     new Movie() { Title = "The Dark Knight", Rating = 8.9f, Year = 2008 }
            // };

            // var query2 = from movie in movies
            //              where movie.Year > 2000
            //              orderby movie.Title
            //              select movie;

        }
    }
}