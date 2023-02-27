import clases

persona = clases.Persona()
persona.setNombre("Jorge")
persona.setApellidos("Fernandez")
persona.setAltura("165cm")
persona.setEdad("26 años")

print(f"La persona es {persona.getNombre()} {persona.getApellidos()}")
print(persona.dormir())
print("-----------------------------------")
informatico = clases.Informatico()

informatico.setNombre("Carlos")
informatico.setApellidos("Castro")
print(f"El informatico es {informatico.getNombre()} {informatico.getApellidos()}")
print(informatico.getLenguajes())
print(informatico.caminar())
print(informatico.experiencia)
print("-----------------------------------")

tecnico = clases.TecnicoRedes()
tecnico.setNombre("Paco")
print(tecnico.auditarRedes,tecnico.getNombre(),tecnico.getLenguajes())
