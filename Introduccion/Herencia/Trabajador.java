public class Trabajador extends Persona{
    private int salario;

    public int getSalario() {
        return salario;
    }

    public void setSalario(int salario) {
        this.salario = salario;
    }
    

    public static void main(String[] args) {
        Trabajador trabajador = new Trabajador();
        trabajador.setNombre("Juan Perez");
        trabajador.setEdad(45);
        trabajador.setTelefono("+5938484884");
        trabajador.setSalario(1000);

        System.out.println("\n\tMostrando informacion de trabajador\n");
        System.out.println("Nombre: "+trabajador.getNombre());
        System.out.println("Edad: "+trabajador.getEdad());
        System.out.println("Teléfono: "+trabajador.getTelefono());
        System.out.println("Salario: "+trabajador.getSalario());
        System.out.println();
    }
}
