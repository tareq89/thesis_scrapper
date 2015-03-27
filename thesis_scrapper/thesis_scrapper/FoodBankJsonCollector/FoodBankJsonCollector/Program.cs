using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Net;
using System.Text;
using System.Threading.Tasks;

namespace FoodBankJsonCollector
{
    class Program
    {
        static void Main(string[] args)
        {
            RootObject root = new RootObject();
            List<Datum> mainDatum = new List<Datum>();
            string Url = @"https://graph.facebook.com/537554109685212/feed?access_token=CAACEdEose0cBAAgwaUy5NZC2iZCHQ5l5me9Mji9BqsXPpfMOwjsx3I0lxQG3AKLGYxywMVlPvedCbKweuvoaQ01DZApdPO2O3gSgO7FF8QVHB4DE6iM977nIbcE8MrDZC60LE20ZC3xnispmY6L9O7IEPV10aAfcWvZC8zoa4TUkWpcKPoZBEs0T5reBQ4mF56kkJN4VQcSB1609DuDlDYO";
            WebClient client = new WebClient();
            string Json;
            int i = 0;
            while (true)
            {
                Json = client.DownloadString(Url);
                root = JsonConvert.DeserializeObject<RootObject>(Json);
                
                mainDatum.AddRange(root.data);

                if (root.paging != null)
                {
                    if (root.paging.previous != null)
                    {
                        Url = root.paging.previous;
                        Console.WriteLine(i++ + "  :  " + root.paging.previous);
                    }
                }
                string Json2 = JsonConvert.SerializeObject(mainDatum);
                File.WriteAllText(@"D:\FoodBankPosts.txt", Json2);
            }

        }
    }
}
