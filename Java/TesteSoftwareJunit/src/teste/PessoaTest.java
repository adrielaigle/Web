package teste;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class PessoaTest {

	@Test
	void deveCriarPessoaComNomeValido() {
		try {
			Pessoa pessoa = new Pessoa("Lucas Andrade", 30);
			assertNotNull(pessoa);
			assertEquals("Lucas Andrade", pessoa.getNome());
		} catch (Exception e) {
			fail(e.getMessage());
		}
	}

	@Test
	void naoDeveCriarPessoaSemSobrenome() {
		Exception exception = assertThrows(Exception.class, () -> {
			new Pessoa("Carlos", 28);
		});
		assertEquals("Deve ser informado o sobrenome", exception.getMessage());
	}

	@Test
	void deveAceitarNomeComMaisDeCincoCaracteres() {
		try {
			Pessoa pessoa = new Pessoa("Fernando Rocha", 35);
			assertNotNull(pessoa);
			assertEquals("Fernando Rocha", pessoa.getNome());
		} catch (Exception e) {
			fail(e.getMessage());
		}
	}

	@Test
	void naoDeveAceitarNomeComMenosDeCincoCaracteres() {
		Exception exception = assertThrows(Exception.class, () -> {
			new Pessoa("Li Te", 22);
		});
		assertEquals("Nome e sobrenome devem possuir mais do que 5 caracteres", exception.getMessage());
	}

	@Test
	void deveAceitarNomeComLetrasValidas() {
		try {
			Pessoa pessoa = new Pessoa("Amanda Souza", 27);
			assertNotNull(pessoa);
			assertEquals("Amanda Souza", pessoa.getNome());
		} catch (Exception e) {
			fail(e.getMessage());
		}
	}

	@Test
	void naoDeveAceitarNomeComCaracteresInvalidos() {
		Exception exception = assertThrows(Exception.class, () -> {
			new Pessoa("Bruno@ Santos", 45);
		});
		assertEquals("Caracter inválido encontrado!", exception.getMessage());
	}

	@Test
	void naoDeveAceitarIdadeNegativa() {
		Exception exception = assertThrows(Exception.class, () -> {
			new Pessoa("Ricardo Alves", -1);
		});
		assertEquals("Idade não pode ser negativa", exception.getMessage());
	}

	@Test
	void naoDeveAceitarIdadeAcimaDe100() {
		Exception exception = assertThrows(Exception.class, () -> {
			new Pessoa("Gustavo Lima", 101);
		});
		assertEquals("Idade não pode ser maior que 100", exception.getMessage());
	}

	@Test
	void deveAceitarIdadeMinimaValida() {
		try {
			Pessoa pessoa = new Pessoa("Elisa Ramos", 0);
			assertNotNull(pessoa);
			assertEquals(0, pessoa.getIdade());
		} catch (Exception e) {
			fail(e.getMessage());
		}
	}

	@Test
	void deveAceitarIdadeMaximaValida() {
		try {
			Pessoa pessoa = new Pessoa("Fabio Pereira", 100);
			assertNotNull(pessoa);
			assertEquals(100, pessoa.getIdade());
		} catch (Exception e) {
			fail(e.getMessage());
		}
	}

	@Test // Aceita caractere inválido após o espaço e não lança nenhuma exceção
	void erro1() {
		Exception exception = assertThrows(Exception.class, () -> {
			new Pessoa("Adriel *Aigle", 22);
		});
		assertEquals("Caracter inválido encontrado!", exception.getMessage());
	}

	@Test // Aceita nome sem sobrenome se depois do nome estiver com um espaço e não lança
			// nenhuma exceção
	void erro2() {
		Exception exception = assertThrows(Exception.class, () -> {
			new Pessoa("Carlos ", 28);
		});
		assertEquals("Deve ser informado o sobrenome!", exception.getMessage());
	}
}