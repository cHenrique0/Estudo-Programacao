
using LojaCursos.ContentContext.Enums;

namespace LojaCursos.ContentContext
{
    // Aulas que um modulo possui
    public class Lecture
    {
        // Ordem da aula
        public int Order { get; set; }
        public string Title { get; set; }
        // Duração da aula
        public int DurationInMinutes { get; set; }
        // Nivel da aula
        public EContentLevel Level { get; set; }
    }
}