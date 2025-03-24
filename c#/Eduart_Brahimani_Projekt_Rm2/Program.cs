using System;

class Program
{
    static void Main()
    {
        int[] notat = new int[10];


        for (int i = 0; i < 10; i++)
        {
            Console.Write($"Futni notën {i + 1}: ");
            notat[i] = int.Parse(Console.ReadLine());
        }

        Console.WriteLine("\nNotat e futura:");
        for (int i = 0; i < 10; i++)
        {
            Console.WriteLine(notat[i]);
        }

        int notaMeELarte = notat[0];
        int notaMeEUlet = notat[0];
        int shuma = 0;
        int notaMbi60 = 0;

        for (int i = 0; i < 10; i++)
        {

            if (notat[i] > notaMeELarte)
                notaMeELarte = notat[i];
            if (notat[i] < notaMeEUlet)
                notaMeEUlet = notat[i];

            shuma += notat[i];

            if (notat[i] > 60)
                notaMbi60++;
        }

        double mesatarja = (double)shuma / 10;

        Console.WriteLine($"\nNota më e lartë: {notaMeELarte}");

        Console.WriteLine($"Nota më e ulët: {notaMeEUlet}");
        Console.WriteLine($"Nota mesatare: {mesatarja:F2}");

        Console.WriteLine($"Numri i notave mbi 60: {notaMbi60}");

    }
}
