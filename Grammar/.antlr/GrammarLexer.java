// Generated from /Users/helenarestorff/Dropbox/DTU/Kandidat/4.semester/Speciale/cbpmc4fun_python/Grammar/Grammar.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class GrammarLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, TRUE=4, FALSE=5, IF=6, ELSE=7, WHILE=8, LPAR=9, 
		RPAR=10, LSPAR=11, RSPAR=12, LCPAR=13, RCPAR=14, ASS=15, NEQ=16, GEQ=17, 
		LEQ=18, AND=19, OR=20, DOTMINUS=21, RANGE=22, ARROW=23, GT=24, LT=25, 
		TIMES=26, DIV=27, PLUS=28, MINUS=29, SEQ=30, NEG=31, EQ=32, UNIF=33, SKIIP=34, 
		COMMENT=35, MULTILINECOMMENT=36, INT=37, FLOAT=38, WHITESPACE=39, NEWLINE=40, 
		VAR=41, CHAR=42;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "TRUE", "FALSE", "IF", "ELSE", "WHILE", "LPAR", 
			"RPAR", "LSPAR", "RSPAR", "LCPAR", "RCPAR", "ASS", "NEQ", "GEQ", "LEQ", 
			"AND", "OR", "DOTMINUS", "RANGE", "ARROW", "GT", "LT", "TIMES", "DIV", 
			"PLUS", "MINUS", "SEQ", "NEG", "EQ", "UNIF", "SKIIP", "COMMENT", "MULTILINECOMMENT", 
			"INT", "FLOAT", "WHITESPACE", "NEWLINE", "VAR", "CHAR"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'post:'", "'pre:'", "'init:'", "'true'", "'false'", "'if'", "'else'", 
			"'while'", "'('", "')'", "'['", "']'", "'{'", "'}'", "':='", "'!='", 
			"'>='", "'<='", "'&&'", "'||'", "'.-'", "'..'", "'->'", "'>'", "'<'", 
			"'*'", "'/'", "'+'", "'-'", "';'", "'!'", "'='", "'unif'", "'skip'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, "TRUE", "FALSE", "IF", "ELSE", "WHILE", "LPAR", 
			"RPAR", "LSPAR", "RSPAR", "LCPAR", "RCPAR", "ASS", "NEQ", "GEQ", "LEQ", 
			"AND", "OR", "DOTMINUS", "RANGE", "ARROW", "GT", "LT", "TIMES", "DIV", 
			"PLUS", "MINUS", "SEQ", "NEG", "EQ", "UNIF", "SKIIP", "COMMENT", "MULTILINECOMMENT", 
			"INT", "FLOAT", "WHITESPACE", "NEWLINE", "VAR", "CHAR"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public GrammarLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Grammar.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2,\u00ff\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\3"+
		"\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\5"+
		"\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3"+
		"\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16"+
		"\3\17\3\17\3\20\3\20\3\20\3\21\3\21\3\21\3\22\3\22\3\22\3\23\3\23\3\23"+
		"\3\24\3\24\3\24\3\25\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\27\3\30\3\30"+
		"\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37"+
		"\3\37\3 \3 \3!\3!\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3$\3$\3$\3$\7$\u00c9"+
		"\n$\f$\16$\u00cc\13$\3$\3$\3%\3%\3%\3%\7%\u00d4\n%\f%\16%\u00d7\13%\3"+
		"%\3%\3%\3%\3%\3&\6&\u00df\n&\r&\16&\u00e0\3\'\3\'\3\'\3\'\3(\6(\u00e8"+
		"\n(\r(\16(\u00e9\3(\3(\3)\3)\3)\5)\u00f1\n)\3)\3)\3*\3*\3*\3*\7*\u00f9"+
		"\n*\f*\16*\u00fc\13*\3+\3+\3\u00d5\2,\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21"+
		"\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30"+
		"/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,\3\2\6"+
		"\4\2\f\f\17\17\3\2\62;\4\2\13\13\"\"\4\2C\\c|\2\u0106\2\3\3\2\2\2\2\5"+
		"\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2"+
		"\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33"+
		"\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2"+
		"\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2"+
		"\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2"+
		"\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K"+
		"\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\3W\3\2"+
		"\2\2\5]\3\2\2\2\7b\3\2\2\2\th\3\2\2\2\13m\3\2\2\2\rs\3\2\2\2\17v\3\2\2"+
		"\2\21{\3\2\2\2\23\u0081\3\2\2\2\25\u0083\3\2\2\2\27\u0085\3\2\2\2\31\u0087"+
		"\3\2\2\2\33\u0089\3\2\2\2\35\u008b\3\2\2\2\37\u008d\3\2\2\2!\u0090\3\2"+
		"\2\2#\u0093\3\2\2\2%\u0096\3\2\2\2\'\u0099\3\2\2\2)\u009c\3\2\2\2+\u009f"+
		"\3\2\2\2-\u00a2\3\2\2\2/\u00a5\3\2\2\2\61\u00a8\3\2\2\2\63\u00aa\3\2\2"+
		"\2\65\u00ac\3\2\2\2\67\u00ae\3\2\2\29\u00b0\3\2\2\2;\u00b2\3\2\2\2=\u00b4"+
		"\3\2\2\2?\u00b6\3\2\2\2A\u00b8\3\2\2\2C\u00ba\3\2\2\2E\u00bf\3\2\2\2G"+
		"\u00c4\3\2\2\2I\u00cf\3\2\2\2K\u00de\3\2\2\2M\u00e2\3\2\2\2O\u00e7\3\2"+
		"\2\2Q\u00f0\3\2\2\2S\u00f4\3\2\2\2U\u00fd\3\2\2\2WX\7r\2\2XY\7q\2\2YZ"+
		"\7u\2\2Z[\7v\2\2[\\\7<\2\2\\\4\3\2\2\2]^\7r\2\2^_\7t\2\2_`\7g\2\2`a\7"+
		"<\2\2a\6\3\2\2\2bc\7k\2\2cd\7p\2\2de\7k\2\2ef\7v\2\2fg\7<\2\2g\b\3\2\2"+
		"\2hi\7v\2\2ij\7t\2\2jk\7w\2\2kl\7g\2\2l\n\3\2\2\2mn\7h\2\2no\7c\2\2op"+
		"\7n\2\2pq\7u\2\2qr\7g\2\2r\f\3\2\2\2st\7k\2\2tu\7h\2\2u\16\3\2\2\2vw\7"+
		"g\2\2wx\7n\2\2xy\7u\2\2yz\7g\2\2z\20\3\2\2\2{|\7y\2\2|}\7j\2\2}~\7k\2"+
		"\2~\177\7n\2\2\177\u0080\7g\2\2\u0080\22\3\2\2\2\u0081\u0082\7*\2\2\u0082"+
		"\24\3\2\2\2\u0083\u0084\7+\2\2\u0084\26\3\2\2\2\u0085\u0086\7]\2\2\u0086"+
		"\30\3\2\2\2\u0087\u0088\7_\2\2\u0088\32\3\2\2\2\u0089\u008a\7}\2\2\u008a"+
		"\34\3\2\2\2\u008b\u008c\7\177\2\2\u008c\36\3\2\2\2\u008d\u008e\7<\2\2"+
		"\u008e\u008f\7?\2\2\u008f \3\2\2\2\u0090\u0091\7#\2\2\u0091\u0092\7?\2"+
		"\2\u0092\"\3\2\2\2\u0093\u0094\7@\2\2\u0094\u0095\7?\2\2\u0095$\3\2\2"+
		"\2\u0096\u0097\7>\2\2\u0097\u0098\7?\2\2\u0098&\3\2\2\2\u0099\u009a\7"+
		"(\2\2\u009a\u009b\7(\2\2\u009b(\3\2\2\2\u009c\u009d\7~\2\2\u009d\u009e"+
		"\7~\2\2\u009e*\3\2\2\2\u009f\u00a0\7\60\2\2\u00a0\u00a1\7/\2\2\u00a1,"+
		"\3\2\2\2\u00a2\u00a3\7\60\2\2\u00a3\u00a4\7\60\2\2\u00a4.\3\2\2\2\u00a5"+
		"\u00a6\7/\2\2\u00a6\u00a7\7@\2\2\u00a7\60\3\2\2\2\u00a8\u00a9\7@\2\2\u00a9"+
		"\62\3\2\2\2\u00aa\u00ab\7>\2\2\u00ab\64\3\2\2\2\u00ac\u00ad\7,\2\2\u00ad"+
		"\66\3\2\2\2\u00ae\u00af\7\61\2\2\u00af8\3\2\2\2\u00b0\u00b1\7-\2\2\u00b1"+
		":\3\2\2\2\u00b2\u00b3\7/\2\2\u00b3<\3\2\2\2\u00b4\u00b5\7=\2\2\u00b5>"+
		"\3\2\2\2\u00b6\u00b7\7#\2\2\u00b7@\3\2\2\2\u00b8\u00b9\7?\2\2\u00b9B\3"+
		"\2\2\2\u00ba\u00bb\7w\2\2\u00bb\u00bc\7p\2\2\u00bc\u00bd\7k\2\2\u00bd"+
		"\u00be\7h\2\2\u00beD\3\2\2\2\u00bf\u00c0\7u\2\2\u00c0\u00c1\7m\2\2\u00c1"+
		"\u00c2\7k\2\2\u00c2\u00c3\7r\2\2\u00c3F\3\2\2\2\u00c4\u00c5\7\61\2\2\u00c5"+
		"\u00c6\7\61\2\2\u00c6\u00ca\3\2\2\2\u00c7\u00c9\n\2\2\2\u00c8\u00c7\3"+
		"\2\2\2\u00c9\u00cc\3\2\2\2\u00ca\u00c8\3\2\2\2\u00ca\u00cb\3\2\2\2\u00cb"+
		"\u00cd\3\2\2\2\u00cc\u00ca\3\2\2\2\u00cd\u00ce\b$\2\2\u00ceH\3\2\2\2\u00cf"+
		"\u00d0\7*\2\2\u00d0\u00d1\7,\2\2\u00d1\u00d5\3\2\2\2\u00d2\u00d4\13\2"+
		"\2\2\u00d3\u00d2\3\2\2\2\u00d4\u00d7\3\2\2\2\u00d5\u00d6\3\2\2\2\u00d5"+
		"\u00d3\3\2\2\2\u00d6\u00d8\3\2\2\2\u00d7\u00d5\3\2\2\2\u00d8\u00d9\7,"+
		"\2\2\u00d9\u00da\7+\2\2\u00da\u00db\3\2\2\2\u00db\u00dc\b%\2\2\u00dcJ"+
		"\3\2\2\2\u00dd\u00df\t\3\2\2\u00de\u00dd\3\2\2\2\u00df\u00e0\3\2\2\2\u00e0"+
		"\u00de\3\2\2\2\u00e0\u00e1\3\2\2\2\u00e1L\3\2\2\2\u00e2\u00e3\5K&\2\u00e3"+
		"\u00e4\7\60\2\2\u00e4\u00e5\5K&\2\u00e5N\3\2\2\2\u00e6\u00e8\t\4\2\2\u00e7"+
		"\u00e6\3\2\2\2\u00e8\u00e9\3\2\2\2\u00e9\u00e7\3\2\2\2\u00e9\u00ea\3\2"+
		"\2\2\u00ea\u00eb\3\2\2\2\u00eb\u00ec\b(\2\2\u00ecP\3\2\2\2\u00ed\u00ee"+
		"\7\f\2\2\u00ee\u00f1\7\17\2\2\u00ef\u00f1\t\2\2\2\u00f0\u00ed\3\2\2\2"+
		"\u00f0\u00ef\3\2\2\2\u00f1\u00f2\3\2\2\2\u00f2\u00f3\b)\2\2\u00f3R\3\2"+
		"\2\2\u00f4\u00fa\5U+\2\u00f5\u00f9\5U+\2\u00f6\u00f9\5K&\2\u00f7\u00f9"+
		"\7a\2\2\u00f8\u00f5\3\2\2\2\u00f8\u00f6\3\2\2\2\u00f8\u00f7\3\2\2\2\u00f9"+
		"\u00fc\3\2\2\2\u00fa\u00f8\3\2\2\2\u00fa\u00fb\3\2\2\2\u00fbT\3\2\2\2"+
		"\u00fc\u00fa\3\2\2\2\u00fd\u00fe\t\5\2\2\u00feV\3\2\2\2\n\2\u00ca\u00d5"+
		"\u00e0\u00e9\u00f0\u00f8\u00fa\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}