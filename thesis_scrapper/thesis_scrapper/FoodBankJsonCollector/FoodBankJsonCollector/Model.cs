using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FoodBankJsonCollector
{
    public class From
    {
        public string id { get; set; }
        public string name { get; set; }
    }

    public class Datum2
    {
        public string name { get; set; }
        public string id { get; set; }
    }

    public class To
    {
        public List<Datum2> data { get; set; }
    }

    public class Action
    {
        public string name { get; set; }
        public string link { get; set; }
    }

    public class Privacy
    {
        public string value { get; set; }
    }

    public class Application
    {
        public string name { get; set; }
        public string @namespace { get; set; }
        public string id { get; set; }
    }

    public class Datum3
    {
        public string id { get; set; }
        public string name { get; set; }
    }

    public class Cursors
    {
        public string after { get; set; }
        public string before { get; set; }
    }

    public class Paging
    {
        public Cursors cursors { get; set; }
        public string next { get; set; }
    }

    public class Likes
    {
        public List<Datum3> data { get; set; }
        public Paging paging { get; set; }
    }

    public class From2
    {
        public string id { get; set; }
        public string name { get; set; }
    }

    public class MessageTag
    {
        public string id { get; set; }
        public string name { get; set; }
        public string type { get; set; }
        public int offset { get; set; }
        public int length { get; set; }
    }

    public class Datum4
    {
        public string id { get; set; }
        public From2 from { get; set; }
        public string message { get; set; }
        public bool can_remove { get; set; }
        public string created_time { get; set; }
        public int like_count { get; set; }
        public bool user_likes { get; set; }
        public List<MessageTag> message_tags { get; set; }
    }

    public class Cursors2
    {
        public string after { get; set; }
        public string before { get; set; }
    }

    public class Paging2
    {
        public Cursors2 cursors { get; set; }
        public string next { get; set; }
    }

    public class Comments
    {
        public List<Datum4> data { get; set; }
        public Paging2 paging { get; set; }
    }

    public class Shares
    {
        public int count { get; set; }
    }

    public class Location
    {
        public string city { get; set; }
        public string country { get; set; }
        public double latitude { get; set; }
        public double longitude { get; set; }
        public string street { get; set; }
        public string zip { get; set; }
    }

    public class Place
    {
        public string id { get; set; }
        public string name { get; set; }
        public Location location { get; set; }
    }

    public class Datum
    {
        public string id { get; set; }
        public From from { get; set; }
        public To to { get; set; }
        public string message { get; set; }
        public string picture { get; set; }
        public string link { get; set; }
        public string icon { get; set; }
        public List<Action> actions { get; set; }
        public Privacy privacy { get; set; }
        public string type { get; set; }
        public string object_id { get; set; }
        public Application application { get; set; }
        public string created_time { get; set; }
        public string updated_time { get; set; }
        public Likes likes { get; set; }
        public Comments comments { get; set; }
        public Shares shares { get; set; }
        public Place place { get; set; }
    }

    public class Paging3
    {
        public string previous { get; set; }
        public string next { get; set; }
    }

    public class RootObject
    {
        public List<Datum> data { get; set; }
        public Paging3 paging { get; set; }
    }
}
