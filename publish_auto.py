#!/usr/bin/env python3
"""
Script automático para publicar FuxiOS.py v2.0 en GitHub
"""

import subprocess
import sys
import json
import os

def run_command(command, description=""):
    """Ejecuta un comando y maneja errores"""
    print(f"🔄 {description}")
    print(f"   $ {command}")
    
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"   ✅ {description} - EXITOSO")
            if result.stdout.strip():
                print(f"   📝 {result.stdout.strip()}")
            return True
        else:
            print(f"   ❌ {description} - ERROR")
            if result.stderr.strip():
                print(f"   🚨 {result.stderr.strip()}")
            return False
    except Exception as e:
        print(f"   💥 Error ejecutando comando: {e}")
        return False

def main():
    print("🚀 FuxiOS.py v2.0 - Script de Publicación Automática")
    print("=" * 60)
    
    # Verificar estado de Git
    print("\n📋 Verificando estado del repositorio...")
    run_command("git status --porcelain", "Verificar archivos modificados")
    run_command("git log --oneline -3", "Mostrar últimos commits")
    
    # Crear repositorio en GitHub via CLI (si está instalado)
    print("\n🌟 Creando repositorio en GitHub...")
    
    # Descripción del repositorio
    repo_description = "🎯 FuxiOS.py v2.0 - CVE-2016-4631 Exploit PoC modernizado para Python 3. Proyecto nostálgico rescatado y actualizado con amor. F0LloW_Th3_R4ts 🐀"
    
    # Intentar crear con GitHub CLI
    github_cli_cmd = f'gh repo create FuxiOS --public --description "{repo_description}" --source=.'
    
    if run_command("gh --version", "Verificar GitHub CLI"):
        print("\n🔧 GitHub CLI detectado, creando repositorio...")
        if run_command(github_cli_cmd, "Crear repositorio en GitHub"):
            print("✅ Repositorio creado exitosamente con GitHub CLI")
        else:
            print("⚠️  Fallo con GitHub CLI, usar método manual")
            manual_instructions()
    else:
        print("⚠️  GitHub CLI no encontrado, mostrando instrucciones manuales...")
        manual_instructions()
    
    # Subir archivos
    print("\n📤 Subiendo archivos a GitHub...")
    
    commands = [
        ("git push -u origin main", "Subir rama main"),
        ("git push -u origin release/v2.0-nostalgic", "Subir rama de release"),
        ("git push --tags", "Subir tags")
    ]
    
    success_count = 0
    for cmd, desc in commands:
        if run_command(cmd, desc):
            success_count += 1
    
    # Resumen final
    print("\n" + "=" * 60)
    print("📊 RESUMEN DE PUBLICACIÓN")
    print("=" * 60)
    
    if success_count == len(commands):
        print("🎉 ¡PUBLICACIÓN EXITOSA!")
        print("✅ Todas las operaciones completadas")
        print(f"🔗 Repositorio: https://github.com/l3onkers/FuxiOS")
        print("🎯 Próximos pasos:")
        print("   1. Crear Release en GitHub con tag v2.0")
        print("   2. Agregar descripción del proyecto")
        print("   3. Configurar GitHub Pages (opcional)")
    else:
        print("⚠️  Publicación parcial completada")
        print(f"   {success_count}/{len(commands)} operaciones exitosas")
        print("🔧 Revisa errores y ejecuta comandos faltantes manualmente")

def manual_instructions():
    """Muestra instrucciones manuales para crear el repositorio"""
    print("\n📋 INSTRUCCIONES MANUALES:")
    print("1. Ve a: https://github.com/new")
    print("2. Nombre del repositorio: FuxiOS")
    print("3. Descripción: 🎯 FuxiOS.py v2.0 - CVE-2016-4631 Exploit PoC modernizado")
    print("4. Público: ✅")
    print("5. NO inicializar con README (ya lo tenemos)")
    print("6. Crear repositorio")
    print("7. El script continuará automáticamente...")
    
    input("\n⏸️  Presiona ENTER cuando hayas creado el repositorio en GitHub...")

if __name__ == "__main__":
    main()
