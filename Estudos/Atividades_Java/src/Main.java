public class Main {
    public static void main(String[] args) {
        SistemaGestaoFuncionarios sistema = new SistemaGestaoFuncionarios();
        Gerente gerente1 = new Gerente("João", 5000);
        Programador programador1 = new Programador("Maria", 3000);
        Programador programador2 = new Programador("Pedro", 3500);

        sistema.adicionarFuncionario(gerente1);
        sistema.adicionarFuncionario(programador1);
        sistema.adicionarFuncionario(programador2);

        sistema.listarFuncionarios();

        sistema.removerFuncionario("Maria");

        sistema.listarFuncionarios();
    }
}
