public class Main {
    public static void main(String[] args) {
        Professor mateus = new Professor("Mateus Nunes", "12345678910");
        Disciplina matematica = new Disciplina("Matemática", mateus);

        Aluno aluno1 = new Aluno("João", 12345678);
        Aluno aluno2 = new Aluno("Pedro", 12345678);
        Aluno aluno3 = new Aluno("Maria", 12345678);
        Aluno aluno4 = new Aluno("Bruno", 12345678);

        matematica.adicionarAluno(aluno1);
        matematica.adicionarAluno(aluno2);
        matematica.adicionarAluno(aluno3);
        matematica.adicionarAluno(aluno4);

        System.out.println("Disciplina: " + matematica.getNome());
        System.out.println("Professor: " + matematica.getProfessor().getNome());
        matematica.exibirAlunos();
    }
}