
using LojaCursos.ContentContext.Enums;

namespace LojaCursos.ContentContext
{
    public class Course : Content
    {
        // A tag é um tipo de identificar do curso
        public string Tag { get; set; }
        // Modulos que um curso possui
        public IList<Module> Modules { get; set; }
        // duração do curso
        public int DurationInMinutes { get; set; }
        // Nivel do curso
        public EContentLevel Level { get; set; }


        public Course(string title, string url) : base(title, url)
        {
            Modules = new List<Module>();
        }
    }
}