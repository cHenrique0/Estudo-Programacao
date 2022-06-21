
namespace LojaCursos.ContentContext
{
    // Modulos que um curso possui
    public class Module
    {
        // ordem do modulo: 1, 2, 3, 4, etc
        public int Order { get; set; }
        public string Title { get; set; }
        public IList<Lecture> Lectures { get; set; }

        public Module()
        {
            Lectures = new List<Lecture>();
        }
    }
}