
namespace LojaCursos.ContentContext
{
    /*
    A classe Content possui propriedades e metódos em comum para as outras classes.
    As outras classes herdarão da classe Content.
    */
    public abstract class Content
    {
        public Guid Id { get; set; }
        public string Title { get; set; }
        public string Url { get; set; }

        public Content(string title, string url)
        {
            // Gera um Id automatico usando o Guid(globally unique identifier)
            Id = Guid.NewGuid();
            Title = title;
            Url = url;
        }
    }
}