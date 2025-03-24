using System;

class Program
{
    static void Main(string[] args)
    {
        int studentCount = 3;
        int subjectCount = 4;
        double[,] results = new double[studentCount, subjectCount];


        for (int i = 0; i < studentCount; i++)
        {
            Console.WriteLine($"Shtoni rezultatet për studentin {i + 1}:");
            for (int j = 0; j < subjectCount; j++)
            {
                Console.Write($"Lënda {j + 1}: ");
                results[i, j] = Convert.ToDouble(Console.ReadLine());
            }
        }


        for (int i = 0; i < studentCount; i++)
        {
            double sum = 0;
            double minScore = results[i, 0];

            for (int j = 0; j < subjectCount; j++)
            {
                sum += results[i, j];
                if (results[i, j] < minScore)
                {
                    minScore = results[i, j];
                }
            }

            double average = sum / subjectCount;

            Console.WriteLine($"Studenti {i + 1}: Shuma = {sum}, Mesatarja = {average}, Nota më e ulët = {minScore}");
        }


        Console.Write("Zgjidhni lëndën për të kërkuar rezultatin më të lartë (1-4): ");
        int subjectToSearch = Convert.ToInt32(Console.ReadLine()) - 1;

        double maxScore = results[0, subjectToSearch];
        int topStudentIndex = 0;

        for (int i = 1; i < studentCount; i++)
        {
            if (results[i, subjectToSearch] > maxScore)
            {
                maxScore = results[i, subjectToSearch];
                topStudentIndex = i;
            }
        }

        Console.WriteLine($"Studenti me rezultatin më të lartë në lëndën {subjectToSearch + 1} është studenti {topStudentIndex + 1} me rezultat {maxScore}");
    }
}