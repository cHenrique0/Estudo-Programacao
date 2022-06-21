
namespace LojaCursos.ContentContext
{
    public class Career : Content
    {
        // Cursos que uma carreira possui
        public IList<CareerItem> Items { get; set; }

        // Quantidade de cursos que uma carreira possui
        public int TotalCourses => Items.Count;


        public Career(string title, string url) : base(title, url)
        {
            Items = new List<CareerItem>();
        }
    }
}