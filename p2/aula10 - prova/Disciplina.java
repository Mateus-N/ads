import java.util.ArrayList;
import java.util.List;

public class Disciplina {
    private String nome;
    private Professor professor;
    private List<Aluno> alunos = new ArrayList<Aluno>();
    
    public Disciplina(String nome, Professor professor) {
        this.nome = nome;
        this.professor = professor;
    }
    
    public String getNome() {
        return nome;
    }
    
    public Professor getProfessor() {
        return professor;
    }

    public List<Aluno> getAlunos() {
        return alunos;
    }

    public void adicionarAluno(Aluno aluno) {
        alunos.add(aluno);
    }

    public void exibirAlunos() {
        for (Aluno aluno : alunos) {
            System.out.println("Aluno: " + aluno.getNome());
            System.out.println("Matrícula: " + aluno.getMatricula());
        }
    }
}
