import java.util.ArrayList;

class SistemaGestaoFuncionarios {
    private ArrayList<Funcionario> funcionarios;

    public SistemaGestaoFuncionarios() {
        this.funcionarios = new ArrayList<>();
    }

    public void adicionarFuncionario(Funcionario funcionario) {
        funcionarios.add(funcionario);
    }

    public void listarFuncionarios() {
        for (Funcionario funcionario : funcionarios) {
            System.out.println(funcionario);
        }
    }

    public void removerFuncionario(String nome) {
        for (Funcionario funcionario : funcionarios) {
            if (funcionario.getNome().equals(nome)) {
                funcionarios.remove(funcionario);
                System.out.println("Funcionário " + nome + " removido com sucesso.");
                return;
            }
        }
        System.out.println("Funcionário " + nome + " não encontrado.");
    }
}
