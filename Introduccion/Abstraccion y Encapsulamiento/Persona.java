public class Persona {
    
    public static void main(String[] args) {
        Persona persona = new Persona();
        persona.setNombre("Juan Perez");
        persona.setEdad(27);
        persona.setTelefono("+59388484848");

        System.out.println("\n\tDatos personales de la Persona\n");
        System.out.println("Nombre: "+persona.getNombre());
        System.out.println("Edad: "+persona.getEdad());
        System.out.println("Teléfono: "+persona.getTelefono());
        System.out.println();
    }

    private int edad;
    private String nombre;
    private String telefono;


    //Getters and Setters
    public int getEdad() {
        return edad;
    }
    public void setEdad(int edad) {
        this.edad = edad;
    }
    public String getNombre() {
        return nombre;
    }
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    public String getTelefono() {
        return telefono;
    }
    public void setTelefono(String telefono) {
        this.telefono = telefono;
    }

    
}
