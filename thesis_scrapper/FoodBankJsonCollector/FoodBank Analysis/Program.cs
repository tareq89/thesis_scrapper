using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FoodBank_Analysis
{
    class Program
    {
        static void Main(string[] args)
        {
            List<Datum> mainData = new List<Datum>();

            string json = File.ReadAllText(@"D:\FoodBankPosts.txt");

            mainData = JsonConvert.DeserializeObject<List<Datum>>(json);

            List<string> onlyMsg = new List<string>();
            foreach (var item in mainData)
            {
                Console.WriteLine(item.message + "\n\n");
                onlyMsg.Add(item.message);
            }

            string JsonMSG = JsonConvert.SerializeObject(onlyMsg);

            File.WriteAllText(@"D:\onlyMSG.txt", JsonMSG);
            //Console.ReadLine();
        }
    }
}
