{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "toc_visible": true,
      "authorship_tag": "ABX9TyPjTZawYJ6V+/+2sz7AEsKa",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/KevinResendiz/Python-curso/blob/main/P3.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ELAn1PKVm5Aw",
        "outputId": "ec35f077-d8c9-4d6a-be44-d6f02f713ede"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Ingrese el primer numero: 8\n",
            "Ingrese el segundo numero: 5\n",
            "Suma:  13 Resta:  3 Division:  1.6 Multiplicacion:  40\n"
          ]
        }
      ],
      "source": [
        "n1=int(input('Ingrese el primer numero: '))\n",
        "n2=int(input('Ingrese el segundo numero: '))\n",
        "print('Suma: ',n1+n2, 'Resta: ',n1-n2, 'Division: ', n1/n2, 'Multiplicacion: ',n1*n2)"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "nombre=input('Ingrese su nombre: ')\n",
        "if len(nombre) >= 5:\n",
        "  print('Tienes', len(nombre),'letras en tu nombre')\n",
        "else:\n",
        "  print('No tienes mas de 5 letras en tu nombre')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "eW7ykAaKoyXe",
        "outputId": "0294937c-c6ad-4ce1-fad5-f76c630bd846"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Ingrese su nombre: kevin\n",
            "Tienes 5 letras en tu nombre\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "f=input('Ingrese una frase: ')\n",
        "print('Tu frase tiene', len(f),'letras')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rzmX2hKEsOL4",
        "outputId": "5e9576d1-62f9-4d2e-d07a-7cbe29078de0"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Ingrese una frase: jolnbnim\n",
            "Tu frase tiene 8 letras\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "nombre=input('Ingrese su nombre: ')\n",
        "apellido=input('Ingrese su apellido: ')\n",
        "print('Su nombre completo es: ',nombre,apellido)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1prxsjWfsgnL",
        "outputId": "87cbc8ef-8a9b-4779-9446-1c5b40fefd3e"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Ingrese su nombre: kevin\n",
            "Ingrese su apellido: resendiz\n",
            "Su nombre completo es:  kevin resendiz\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "n=[3,5,6,9,5,10]\n",
        "s=0\n",
        "for i in range (len(n)):\n",
        "  s=s+n[i]\n",
        "print(s)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "oUxUJYthtVjY",
        "outputId": "c2de2113-3863-41e9-de5f-b5c13a58eea8"
      },
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "38\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print('True and False =',True and False)\n",
        "print('False and False =',False and False)\n",
        "print('False and True =',False and True)\n",
        "print('True and True =',True and True)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0WR02HH6v3UH",
        "outputId": "7e1f53d1-0306-497d-f6d0-efd05e9dd144"
      },
      "execution_count": 22,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "True and False = False\n",
            "False and False = False\n",
            "False and True = False\n",
            "True and True = True\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print('True or False =',True or False)\n",
        "print('False or False =',False or False)\n",
        "print('False or True =',False or True)\n",
        "print('True or True =',True or True)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_U1OnVUKw_eF",
        "outputId": "62583ce6-3ff5-4717-ad70-8be72a73f915"
      },
      "execution_count": 23,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "True or False = True\n",
            "False or False = False\n",
            "False or True = True\n",
            "True or True = True\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "n1=int(input('Ingrese el primer numero: '))\n",
        "n2=int(input('Ingrese el segundo numero: '))\n",
        "if n1>n2:\n",
        "  print('El primer numero es mas grandre que el segundo')\n",
        "else:\n",
        "  print('El segundo numero es mas grandre que el primero')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "di1agScPxIcc",
        "outputId": "308159cf-412e-4dfe-bd37-d440b98f68c6"
      },
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Ingrese el primer numero: 9\n",
            "Ingrese el segundo numero: 4\n",
            "El primer numero es mas grandre que el segundo\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "nombre=input('Ingrese su nombre: ')\n",
        "edad=int(input('Ingrese su edad: '))\n",
        "print('La edad de',nombre, 'es',edad,'años')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mk5ZJQkxxh4D",
        "outputId": "7748e45b-119d-4ee5-f156-63a3298a7d60"
      },
      "execution_count": 27,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Ingrese su nombre: kevin\n",
            "Ingrese su edad: 20\n",
            "La edad de kevin es 20 años\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "n1=int(input('Ingrese el primer numero: '))\n",
        "n2=int(input('Ingrese el segundo numero: '))\n",
        "if n1==n2:\n",
        "  print('Los 2 numeros son iguales')\n",
        "else:\n",
        "  print('Los 2 numeros no son iguales')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "LQ2xZWqTy7io",
        "outputId": "486cdadf-178f-4f66-9bc0-f7357ed3cdf6"
      },
      "execution_count": 28,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Ingrese el primer numero: 8\n",
            "Ingrese el segundo numero: 8\n",
            "Los 2 numeros son iguales\n"
          ]
        }
      ]
    }
  ]
}