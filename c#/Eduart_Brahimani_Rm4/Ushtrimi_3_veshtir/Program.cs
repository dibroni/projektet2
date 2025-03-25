using System;

class Program
{
    // Gjej vleren maksimale ne matrice
    static int GjejMax(int[,] matrix)
    {
        int maksimumi = matrix[0, 0];
        for (int i = 0; i < 3; i++)
        {
            for (int j = 0; j < 3; j++)
            {
                if (matrix[i, j] > maksimumi)
                    maksimumi = matrix[i, j];
            }
        }
        return maksimumi;
    }

    // Numero perseritjet e vleres maksimale
    static int NumroPerseritjet(int[,] matrix, int maksimumi)
    {
        int count = 0;
        for (int i = 0; i < 3; i++)
        {
            for (int j = 0; j < 3; j++)
            {
                if (matrix[i, j] == maksimumi)
                    count++;
            }
        }
        return count;
    }

    // Zevendeso vleren maksimale me -99 dhe kthe numrin e zëvendësimeve
    static int FshijMax(int[,] matrix, int maksimumi)
    {
        int count = 0;
        for (int i = 0; i < 3; i++)
        {
            for (int j = 0; j < 3; j++)
            {
                if (matrix[i, j] == maksimumi)
                {
                    matrix[i, j] = -99;
                    count++;
                }
            }
        }
        return count;
    }

    // Gjej vleren e dyte me te madhe ne matrice
    static int GjejTeDytenMax(int[,] matrix)
    {
        int max = int.MinValue, secondMax = int.MinValue;
        for (int i = 0; i < 3; i++)
        {
            for (int j = 0; j < 3; j++)
            {
                int vlera = matrix[i, j];
                if (vlera != -99)
                {
                    if (vlera > max)
                    {
                        secondMax = max;
                        max = vlera;
                    }
                    else if (vlera > secondMax && vlera < max)
                    {
                        secondMax = vlera;
                    }
                }
            }
        }
        return secondMax == int.MinValue ? -1 : secondMax;
    }

    // Llogarit mesataren e vlerave 
    static int LlogaritMesataren(int[,] matrix)
    {
        int sum = 0, count = 0;
        for (int i = 0; i < 3; i++)
        {
            for (int j = 0; j < 3; j++)
            {
                if (matrix[i, j] != -99)
                {
                    sum += matrix[i, j];
                    count++;
                }
            }
        }
        return count > 0 ? sum / count : -1;
    }

    static void Main()
    {
        int[,] matrix = new int[3, 3];
        for (int i = 0; i < 3; i++)
        {
            for (int j = 0; j < 3; j++)
            {
                Console.Write("Shkruani elementin per rreshtin " + (i + 1) + ", kolonën " + (j + 1) + ": ");
                matrix[i, j] = int.Parse(Console.ReadLine());
            }
        }

        Console.WriteLine("Matrica origjinale:");
        for (int i = 0; i < 3; i++)
        {
            for (int j = 0; j < 3; j++)
            {
                Console.Write(matrix[i, j] + " ");
            }
            Console.WriteLine();
        }

        int maksimumi = GjejMax(matrix);
        int numriPerseritjeve = NumroPerseritjet(matrix, maksimumi);
        Console.WriteLine("Vlera maksimale: " + maksimumi);
        Console.WriteLine("Numri i perseritjeve te vleres maksimale: " + numriPerseritjeve);

        int zëvendësime = FshijMax(matrix, maksimumi);
        Console.WriteLine("Matrica e re pas fshirjes se vleres maksimale:");
        for (int i = 0; i < 3; i++)
        {
            for (int j = 0; j < 3; j++)
            {
                Console.Write(matrix[i, j] + " ");
            }
            Console.WriteLine();
        }
        Console.WriteLine("Numri i zëvendësimeve: " + zëvendësime);

        int vleraEdytë = GjejTeDytenMax(matrix);
        if (vleraEdytë != -1)
            Console.WriteLine("Vlera e dyte me e madhe: " + vleraEdytë);
        else
            Console.WriteLine("Nuk ka vlere te dyte me te madhe.");

        int mesatarja = LlogaritMesataren(matrix);
        if (mesatarja != -1)
            Console.WriteLine("Mesatarja e vlerave te mbetura: " + mesatarja);
        else
            Console.WriteLine("Nuk ka vlera per te llogaritur mesataren.");
    }
}
