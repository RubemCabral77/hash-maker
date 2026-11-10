# Hash Maker

## About Hash Maker

Hash Maker is a command-line interface (CLI) tool designed to generate cryptographic hashes from user-provided text phrases.

## Installation

Clone the repository and navigate to the project directory:

```shell
gh repo clone RubemCabral77/hash-maker
cd hash-maker

```

## Usage

Run the main application script:

```shell
python main.py

```

Enter your target phrase when prompted:

```shell
Enter a phrase to hash: [phrase very cool]

```

The application outputs the corresponding hash:

```shell
Hashed phrase: [AReallyCoolEncryptedHash]

```

## Architecture

This project implements the **Strategy Pattern** to decouple the core application logic from specific hashing algorithm implementations. This design allows seamless integration and swapping of different cryptographic libraries without modifying the central execution flow.

### Strategy Modules

Individual hash implementations reside within:

```text
src/strategies/

```

## Author

Developed by Rubem Gomes Cabral.

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=flat-square&logo=github&logoColor=white)](https://github.com/RubemCabral77/)
[![Instagram](https://img.shields.io/badge/Instagram-%23E4405F.svg?style=flat-square&logo=Instagram&logoColor=white)](https://instagram.com/rubem.cabral.77)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/rubem-gomes-cabral/)
[![Lattes](https://img.shields.io/badge/Currículo_Lattes-1675B7?style=flat-square&logo=curriculum&logoColor=white)](http://lattes.cnpq.br/2917286979144333)
[![ORCID](https://img.shields.io/badge/ORCID-A6CE39?style=flat-square&logo=orcid&logoColor=white)](https://orcid.org/0009-0000-2961-301X)

## License

This project is open-source software licensed under the [MIT license](https://opensource.org/license/mit).

![GitHub License](https://img.shields.io/github/license/RubemCabral77/hash-maker)
