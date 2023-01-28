// Generated from /Users/helenarestorff/Dropbox/DTU/Kandidat/4.semester/Speciale/cbpmc4fun_python/Grammar/Grammar.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class GrammarParser extends Parser {
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
	public static final int
		RULE_program = 0, RULE_postexpectation = 1, RULE_preexpectation = 2, RULE_inits = 3, 
		RULE_expression = 4, RULE_aexpectation = 5, RULE_bexpression = 6, RULE_bexpectation = 7, 
		RULE_command = 8, RULE_expectation = 9, RULE_aexppar = 10, RULE_expectation0 = 11, 
		RULE_constraint = 12, RULE_initialization = 13;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "postexpectation", "preexpectation", "inits", "expression", 
			"aexpectation", "bexpression", "bexpectation", "command", "expectation", 
			"aexppar", "expectation0", "constraint", "initialization"
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

	@Override
	public String getGrammarFileName() { return "Grammar.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public GrammarParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgramContext extends ParserRuleContext {
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	 
		public ProgramContext() { }
		public void copyFrom(ProgramContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class PGCLProgramContext extends ProgramContext {
		public CommandContext cmd;
		public TerminalNode EOF() { return getToken(GrammarParser.EOF, 0); }
		public CommandContext command() {
			return getRuleContext(CommandContext.class,0);
		}
		public PGCLProgramContext(ProgramContext ctx) { copyFrom(ctx); }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		try {
			_localctx = new PGCLProgramContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(28);
			((PGCLProgramContext)_localctx).cmd = command(0);
			setState(29);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class PostexpectationContext extends ParserRuleContext {
		public PostexpectationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_postexpectation; }
	 
		public PostexpectationContext() { }
		public void copyFrom(PostexpectationContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class PostExpectationContext extends PostexpectationContext {
		public ExpectationContext exp;
		public TerminalNode EOF() { return getToken(GrammarParser.EOF, 0); }
		public ExpectationContext expectation() {
			return getRuleContext(ExpectationContext.class,0);
		}
		public PostExpectationContext(PostexpectationContext ctx) { copyFrom(ctx); }
	}

	public final PostexpectationContext postexpectation() throws RecognitionException {
		PostexpectationContext _localctx = new PostexpectationContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_postexpectation);
		try {
			_localctx = new PostExpectationContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(31);
			match(T__0);
			setState(32);
			((PostExpectationContext)_localctx).exp = expectation();
			setState(33);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class PreexpectationContext extends ParserRuleContext {
		public PreexpectationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_preexpectation; }
	 
		public PreexpectationContext() { }
		public void copyFrom(PreexpectationContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class PreExpectationContext extends PreexpectationContext {
		public ConstraintContext cons;
		public TerminalNode EOF() { return getToken(GrammarParser.EOF, 0); }
		public ConstraintContext constraint() {
			return getRuleContext(ConstraintContext.class,0);
		}
		public PreExpectationContext(PreexpectationContext ctx) { copyFrom(ctx); }
	}

	public final PreexpectationContext preexpectation() throws RecognitionException {
		PreexpectationContext _localctx = new PreexpectationContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_preexpectation);
		try {
			_localctx = new PreExpectationContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(35);
			match(T__1);
			setState(36);
			((PreExpectationContext)_localctx).cons = constraint();
			setState(37);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class InitsContext extends ParserRuleContext {
		public InitsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_inits; }
	 
		public InitsContext() { }
		public void copyFrom(InitsContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class InitializationsContext extends InitsContext {
		public InitializationContext init;
		public TerminalNode EOF() { return getToken(GrammarParser.EOF, 0); }
		public InitializationContext initialization() {
			return getRuleContext(InitializationContext.class,0);
		}
		public InitializationsContext(InitsContext ctx) { copyFrom(ctx); }
	}

	public final InitsContext inits() throws RecognitionException {
		InitsContext _localctx = new InitsContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_inits);
		try {
			_localctx = new InitializationsContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(39);
			match(T__2);
			setState(40);
			((InitializationsContext)_localctx).init = initialization(0);
			setState(41);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpressionContext extends ParserRuleContext {
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	 
		public ExpressionContext() { }
		public void copyFrom(ExpressionContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class MultDivExprContext extends ExpressionContext {
		public ExpressionContext expr1;
		public Token op;
		public ExpressionContext expr2;
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode TIMES() { return getToken(GrammarParser.TIMES, 0); }
		public TerminalNode DIV() { return getToken(GrammarParser.DIV, 0); }
		public MultDivExprContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class PlusMinusDotminusExprContext extends ExpressionContext {
		public ExpressionContext expr1;
		public Token op;
		public ExpressionContext expr2;
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode PLUS() { return getToken(GrammarParser.PLUS, 0); }
		public TerminalNode MINUS() { return getToken(GrammarParser.MINUS, 0); }
		public TerminalNode DOTMINUS() { return getToken(GrammarParser.DOTMINUS, 0); }
		public PlusMinusDotminusExprContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class ExprContext extends ExpressionContext {
		public ExpressionContext expr;
		public TerminalNode LPAR() { return getToken(GrammarParser.LPAR, 0); }
		public TerminalNode RPAR() { return getToken(GrammarParser.RPAR, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public ExprContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class VarExprContext extends ExpressionContext {
		public Token var;
		public TerminalNode VAR() { return getToken(GrammarParser.VAR, 0); }
		public VarExprContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class IntExprContext extends ExpressionContext {
		public Token num;
		public TerminalNode INT() { return getToken(GrammarParser.INT, 0); }
		public IntExprContext(ExpressionContext ctx) { copyFrom(ctx); }
	}

	public final ExpressionContext expression() throws RecognitionException {
		return expression(0);
	}

	private ExpressionContext expression(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExpressionContext _localctx = new ExpressionContext(_ctx, _parentState);
		ExpressionContext _prevctx = _localctx;
		int _startState = 8;
		enterRecursionRule(_localctx, 8, RULE_expression, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(50);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT:
				{
				_localctx = new IntExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(44);
				((IntExprContext)_localctx).num = match(INT);
				}
				break;
			case LPAR:
				{
				_localctx = new ExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(45);
				match(LPAR);
				setState(46);
				((ExprContext)_localctx).expr = expression(0);
				setState(47);
				match(RPAR);
				}
				break;
			case VAR:
				{
				_localctx = new VarExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(49);
				((VarExprContext)_localctx).var = match(VAR);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(60);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,2,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(58);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
					case 1:
						{
						_localctx = new MultDivExprContext(new ExpressionContext(_parentctx, _parentState));
						((MultDivExprContext)_localctx).expr1 = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(52);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(53);
						((MultDivExprContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==TIMES || _la==DIV) ) {
							((MultDivExprContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(54);
						((MultDivExprContext)_localctx).expr2 = expression(6);
						}
						break;
					case 2:
						{
						_localctx = new PlusMinusDotminusExprContext(new ExpressionContext(_parentctx, _parentState));
						((PlusMinusDotminusExprContext)_localctx).expr1 = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(55);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(56);
						((PlusMinusDotminusExprContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << DOTMINUS) | (1L << PLUS) | (1L << MINUS))) != 0)) ) {
							((PlusMinusDotminusExprContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(57);
						((PlusMinusDotminusExprContext)_localctx).expr2 = expression(5);
						}
						break;
					}
					} 
				}
				setState(62);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,2,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class AexpectationContext extends ParserRuleContext {
		public AexpectationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_aexpectation; }
	 
		public AexpectationContext() { }
		public void copyFrom(AexpectationContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class VarAExpContext extends AexpectationContext {
		public Token var;
		public TerminalNode VAR() { return getToken(GrammarParser.VAR, 0); }
		public VarAExpContext(AexpectationContext ctx) { copyFrom(ctx); }
	}
	public static class ExprAExpContext extends AexpectationContext {
		public AexpectationContext aexp;
		public TerminalNode LPAR() { return getToken(GrammarParser.LPAR, 0); }
		public TerminalNode RPAR() { return getToken(GrammarParser.RPAR, 0); }
		public AexpectationContext aexpectation() {
			return getRuleContext(AexpectationContext.class,0);
		}
		public ExprAExpContext(AexpectationContext ctx) { copyFrom(ctx); }
	}
	public static class PlusMinusDotminusAExpContext extends AexpectationContext {
		public AexpectationContext aexp1;
		public Token op;
		public AexpectationContext aexp2;
		public List<AexpectationContext> aexpectation() {
			return getRuleContexts(AexpectationContext.class);
		}
		public AexpectationContext aexpectation(int i) {
			return getRuleContext(AexpectationContext.class,i);
		}
		public TerminalNode PLUS() { return getToken(GrammarParser.PLUS, 0); }
		public TerminalNode MINUS() { return getToken(GrammarParser.MINUS, 0); }
		public TerminalNode DOTMINUS() { return getToken(GrammarParser.DOTMINUS, 0); }
		public PlusMinusDotminusAExpContext(AexpectationContext ctx) { copyFrom(ctx); }
	}
	public static class IntAExpContext extends AexpectationContext {
		public Token num;
		public TerminalNode INT() { return getToken(GrammarParser.INT, 0); }
		public IntAExpContext(AexpectationContext ctx) { copyFrom(ctx); }
	}
	public static class RealAExpContext extends AexpectationContext {
		public Token num;
		public TerminalNode FLOAT() { return getToken(GrammarParser.FLOAT, 0); }
		public RealAExpContext(AexpectationContext ctx) { copyFrom(ctx); }
	}
	public static class MultDivAExpContext extends AexpectationContext {
		public AexpectationContext aexp1;
		public Token op;
		public AexpectationContext aexp2;
		public List<AexpectationContext> aexpectation() {
			return getRuleContexts(AexpectationContext.class);
		}
		public AexpectationContext aexpectation(int i) {
			return getRuleContext(AexpectationContext.class,i);
		}
		public TerminalNode TIMES() { return getToken(GrammarParser.TIMES, 0); }
		public TerminalNode DIV() { return getToken(GrammarParser.DIV, 0); }
		public MultDivAExpContext(AexpectationContext ctx) { copyFrom(ctx); }
	}

	public final AexpectationContext aexpectation() throws RecognitionException {
		return aexpectation(0);
	}

	private AexpectationContext aexpectation(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		AexpectationContext _localctx = new AexpectationContext(_ctx, _parentState);
		AexpectationContext _prevctx = _localctx;
		int _startState = 10;
		enterRecursionRule(_localctx, 10, RULE_aexpectation, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(71);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LPAR:
				{
				_localctx = new ExprAExpContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(64);
				match(LPAR);
				setState(65);
				((ExprAExpContext)_localctx).aexp = aexpectation(0);
				setState(66);
				match(RPAR);
				}
				break;
			case INT:
				{
				_localctx = new IntAExpContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(68);
				((IntAExpContext)_localctx).num = match(INT);
				}
				break;
			case FLOAT:
				{
				_localctx = new RealAExpContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(69);
				((RealAExpContext)_localctx).num = match(FLOAT);
				}
				break;
			case VAR:
				{
				_localctx = new VarAExpContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(70);
				((VarAExpContext)_localctx).var = match(VAR);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(81);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(79);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
					case 1:
						{
						_localctx = new MultDivAExpContext(new AexpectationContext(_parentctx, _parentState));
						((MultDivAExpContext)_localctx).aexp1 = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_aexpectation);
						setState(73);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(74);
						((MultDivAExpContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==TIMES || _la==DIV) ) {
							((MultDivAExpContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(75);
						((MultDivAExpContext)_localctx).aexp2 = aexpectation(7);
						}
						break;
					case 2:
						{
						_localctx = new PlusMinusDotminusAExpContext(new AexpectationContext(_parentctx, _parentState));
						((PlusMinusDotminusAExpContext)_localctx).aexp1 = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_aexpectation);
						setState(76);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(77);
						((PlusMinusDotminusAExpContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << DOTMINUS) | (1L << PLUS) | (1L << MINUS))) != 0)) ) {
							((PlusMinusDotminusAExpContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(78);
						((PlusMinusDotminusAExpContext)_localctx).aexp2 = aexpectation(6);
						}
						break;
					}
					} 
				}
				setState(83);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class BexpressionContext extends ParserRuleContext {
		public BexpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bexpression; }
	 
		public BexpressionContext() { }
		public void copyFrom(BexpressionContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class AndExprContext extends BexpressionContext {
		public BexpressionContext bexpr1;
		public Token op;
		public BexpressionContext bexpr2;
		public List<BexpressionContext> bexpression() {
			return getRuleContexts(BexpressionContext.class);
		}
		public BexpressionContext bexpression(int i) {
			return getRuleContext(BexpressionContext.class,i);
		}
		public TerminalNode AND() { return getToken(GrammarParser.AND, 0); }
		public AndExprContext(BexpressionContext ctx) { copyFrom(ctx); }
	}
	public static class BoolExprContext extends BexpressionContext {
		public Token val;
		public TerminalNode TRUE() { return getToken(GrammarParser.TRUE, 0); }
		public TerminalNode FALSE() { return getToken(GrammarParser.FALSE, 0); }
		public BoolExprContext(BexpressionContext ctx) { copyFrom(ctx); }
	}
	public static class BExprContext extends BexpressionContext {
		public BexpressionContext bexpr;
		public TerminalNode LPAR() { return getToken(GrammarParser.LPAR, 0); }
		public TerminalNode RPAR() { return getToken(GrammarParser.RPAR, 0); }
		public BexpressionContext bexpression() {
			return getRuleContext(BexpressionContext.class,0);
		}
		public BExprContext(BexpressionContext ctx) { copyFrom(ctx); }
	}
	public static class CompareExprContext extends BexpressionContext {
		public ExpressionContext bexpr1;
		public Token op;
		public ExpressionContext bexpr2;
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode EQ() { return getToken(GrammarParser.EQ, 0); }
		public TerminalNode NEQ() { return getToken(GrammarParser.NEQ, 0); }
		public TerminalNode GT() { return getToken(GrammarParser.GT, 0); }
		public TerminalNode LT() { return getToken(GrammarParser.LT, 0); }
		public TerminalNode GEQ() { return getToken(GrammarParser.GEQ, 0); }
		public TerminalNode LEQ() { return getToken(GrammarParser.LEQ, 0); }
		public CompareExprContext(BexpressionContext ctx) { copyFrom(ctx); }
	}
	public static class NegExprContext extends BexpressionContext {
		public Token op;
		public BexpressionContext bexpr;
		public TerminalNode NEG() { return getToken(GrammarParser.NEG, 0); }
		public BexpressionContext bexpression() {
			return getRuleContext(BexpressionContext.class,0);
		}
		public NegExprContext(BexpressionContext ctx) { copyFrom(ctx); }
	}
	public static class OrExprContext extends BexpressionContext {
		public BexpressionContext bexpr1;
		public Token op;
		public BexpressionContext bexpr2;
		public List<BexpressionContext> bexpression() {
			return getRuleContexts(BexpressionContext.class);
		}
		public BexpressionContext bexpression(int i) {
			return getRuleContext(BexpressionContext.class,i);
		}
		public TerminalNode OR() { return getToken(GrammarParser.OR, 0); }
		public OrExprContext(BexpressionContext ctx) { copyFrom(ctx); }
	}

	public final BexpressionContext bexpression() throws RecognitionException {
		return bexpression(0);
	}

	private BexpressionContext bexpression(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		BexpressionContext _localctx = new BexpressionContext(_ctx, _parentState);
		BexpressionContext _prevctx = _localctx;
		int _startState = 12;
		enterRecursionRule(_localctx, 12, RULE_bexpression, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(96);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				{
				_localctx = new BoolExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(85);
				((BoolExprContext)_localctx).val = _input.LT(1);
				_la = _input.LA(1);
				if ( !(_la==TRUE || _la==FALSE) ) {
					((BoolExprContext)_localctx).val = (Token)_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
				break;
			case 2:
				{
				_localctx = new NegExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(86);
				((NegExprContext)_localctx).op = match(NEG);
				setState(87);
				((NegExprContext)_localctx).bexpr = bexpression(5);
				}
				break;
			case 3:
				{
				_localctx = new CompareExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(88);
				((CompareExprContext)_localctx).bexpr1 = expression(0);
				setState(89);
				((CompareExprContext)_localctx).op = _input.LT(1);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << NEQ) | (1L << GEQ) | (1L << LEQ) | (1L << GT) | (1L << LT) | (1L << EQ))) != 0)) ) {
					((CompareExprContext)_localctx).op = (Token)_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(90);
				((CompareExprContext)_localctx).bexpr2 = expression(0);
				}
				break;
			case 4:
				{
				_localctx = new BExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(92);
				match(LPAR);
				setState(93);
				((BExprContext)_localctx).bexpr = bexpression(0);
				setState(94);
				match(RPAR);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(106);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,8,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(104);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
					case 1:
						{
						_localctx = new AndExprContext(new BexpressionContext(_parentctx, _parentState));
						((AndExprContext)_localctx).bexpr1 = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_bexpression);
						setState(98);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(99);
						((AndExprContext)_localctx).op = match(AND);
						setState(100);
						((AndExprContext)_localctx).bexpr2 = bexpression(5);
						}
						break;
					case 2:
						{
						_localctx = new OrExprContext(new BexpressionContext(_parentctx, _parentState));
						((OrExprContext)_localctx).bexpr1 = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_bexpression);
						setState(101);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(102);
						((OrExprContext)_localctx).op = match(OR);
						setState(103);
						((OrExprContext)_localctx).bexpr2 = bexpression(4);
						}
						break;
					}
					} 
				}
				setState(108);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,8,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class BexpectationContext extends ParserRuleContext {
		public BexpectationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bexpectation; }
	 
		public BexpectationContext() { }
		public void copyFrom(BexpectationContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class CompareExpContext extends BexpectationContext {
		public AexpectationContext bexp1;
		public Token op;
		public AexpectationContext bexp2;
		public List<AexpectationContext> aexpectation() {
			return getRuleContexts(AexpectationContext.class);
		}
		public AexpectationContext aexpectation(int i) {
			return getRuleContext(AexpectationContext.class,i);
		}
		public TerminalNode EQ() { return getToken(GrammarParser.EQ, 0); }
		public TerminalNode NEQ() { return getToken(GrammarParser.NEQ, 0); }
		public TerminalNode GT() { return getToken(GrammarParser.GT, 0); }
		public TerminalNode LT() { return getToken(GrammarParser.LT, 0); }
		public TerminalNode GEQ() { return getToken(GrammarParser.GEQ, 0); }
		public TerminalNode LEQ() { return getToken(GrammarParser.LEQ, 0); }
		public CompareExpContext(BexpectationContext ctx) { copyFrom(ctx); }
	}
	public static class NegAExpContext extends BexpectationContext {
		public Token op;
		public BexpectationContext bexp;
		public TerminalNode NEG() { return getToken(GrammarParser.NEG, 0); }
		public BexpectationContext bexpectation() {
			return getRuleContext(BexpectationContext.class,0);
		}
		public NegAExpContext(BexpectationContext ctx) { copyFrom(ctx); }
	}
	public static class AndAExpContext extends BexpectationContext {
		public BexpectationContext bexp1;
		public Token op;
		public BexpectationContext bexp2;
		public List<BexpectationContext> bexpectation() {
			return getRuleContexts(BexpectationContext.class);
		}
		public BexpectationContext bexpectation(int i) {
			return getRuleContext(BexpectationContext.class,i);
		}
		public TerminalNode AND() { return getToken(GrammarParser.AND, 0); }
		public AndAExpContext(BexpectationContext ctx) { copyFrom(ctx); }
	}
	public static class OrAExpContext extends BexpectationContext {
		public BexpectationContext bexp1;
		public Token op;
		public BexpectationContext bexp2;
		public List<BexpectationContext> bexpectation() {
			return getRuleContexts(BexpectationContext.class);
		}
		public BexpectationContext bexpectation(int i) {
			return getRuleContext(BexpectationContext.class,i);
		}
		public TerminalNode OR() { return getToken(GrammarParser.OR, 0); }
		public OrAExpContext(BexpectationContext ctx) { copyFrom(ctx); }
	}
	public static class BoolAExpContext extends BexpectationContext {
		public Token val;
		public TerminalNode TRUE() { return getToken(GrammarParser.TRUE, 0); }
		public TerminalNode FALSE() { return getToken(GrammarParser.FALSE, 0); }
		public BoolAExpContext(BexpectationContext ctx) { copyFrom(ctx); }
	}
	public static class BAExpContext extends BexpectationContext {
		public BexpectationContext bexp;
		public TerminalNode LPAR() { return getToken(GrammarParser.LPAR, 0); }
		public TerminalNode RPAR() { return getToken(GrammarParser.RPAR, 0); }
		public BexpectationContext bexpectation() {
			return getRuleContext(BexpectationContext.class,0);
		}
		public BAExpContext(BexpectationContext ctx) { copyFrom(ctx); }
	}

	public final BexpectationContext bexpectation() throws RecognitionException {
		return bexpectation(0);
	}

	private BexpectationContext bexpectation(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		BexpectationContext _localctx = new BexpectationContext(_ctx, _parentState);
		BexpectationContext _prevctx = _localctx;
		int _startState = 14;
		enterRecursionRule(_localctx, 14, RULE_bexpectation, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(121);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
			case 1:
				{
				_localctx = new BoolAExpContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(110);
				((BoolAExpContext)_localctx).val = _input.LT(1);
				_la = _input.LA(1);
				if ( !(_la==TRUE || _la==FALSE) ) {
					((BoolAExpContext)_localctx).val = (Token)_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
				break;
			case 2:
				{
				_localctx = new NegAExpContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(111);
				((NegAExpContext)_localctx).op = match(NEG);
				setState(112);
				((NegAExpContext)_localctx).bexp = bexpectation(5);
				}
				break;
			case 3:
				{
				_localctx = new CompareExpContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(113);
				((CompareExpContext)_localctx).bexp1 = aexpectation(0);
				setState(114);
				((CompareExpContext)_localctx).op = _input.LT(1);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << NEQ) | (1L << GEQ) | (1L << LEQ) | (1L << GT) | (1L << LT) | (1L << EQ))) != 0)) ) {
					((CompareExpContext)_localctx).op = (Token)_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(115);
				((CompareExpContext)_localctx).bexp2 = aexpectation(0);
				}
				break;
			case 4:
				{
				_localctx = new BAExpContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(117);
				match(LPAR);
				setState(118);
				((BAExpContext)_localctx).bexp = bexpectation(0);
				setState(119);
				match(RPAR);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(131);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,11,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(129);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,10,_ctx) ) {
					case 1:
						{
						_localctx = new AndAExpContext(new BexpectationContext(_parentctx, _parentState));
						((AndAExpContext)_localctx).bexp1 = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_bexpectation);
						setState(123);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(124);
						((AndAExpContext)_localctx).op = match(AND);
						setState(125);
						((AndAExpContext)_localctx).bexp2 = bexpectation(5);
						}
						break;
					case 2:
						{
						_localctx = new OrAExpContext(new BexpectationContext(_parentctx, _parentState));
						((OrAExpContext)_localctx).bexp1 = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_bexpectation);
						setState(126);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(127);
						((OrAExpContext)_localctx).op = match(OR);
						setState(128);
						((OrAExpContext)_localctx).bexp2 = bexpectation(4);
						}
						break;
					}
					} 
				}
				setState(133);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,11,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class CommandContext extends ParserRuleContext {
		public CommandContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_command; }
	 
		public CommandContext() { }
		public void copyFrom(CommandContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class ProbCmdContext extends CommandContext {
		public CommandContext cmd1;
		public ExpressionContext expr;
		public CommandContext cmd2;
		public List<TerminalNode> LCPAR() { return getTokens(GrammarParser.LCPAR); }
		public TerminalNode LCPAR(int i) {
			return getToken(GrammarParser.LCPAR, i);
		}
		public List<TerminalNode> RCPAR() { return getTokens(GrammarParser.RCPAR); }
		public TerminalNode RCPAR(int i) {
			return getToken(GrammarParser.RCPAR, i);
		}
		public TerminalNode LSPAR() { return getToken(GrammarParser.LSPAR, 0); }
		public TerminalNode RSPAR() { return getToken(GrammarParser.RSPAR, 0); }
		public List<CommandContext> command() {
			return getRuleContexts(CommandContext.class);
		}
		public CommandContext command(int i) {
			return getRuleContext(CommandContext.class,i);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public ProbCmdContext(CommandContext ctx) { copyFrom(ctx); }
	}
	public static class WhileCmdContext extends CommandContext {
		public BexpressionContext bexpr;
		public ExpectationContext inv;
		public CommandContext cmd;
		public TerminalNode WHILE() { return getToken(GrammarParser.WHILE, 0); }
		public TerminalNode LPAR() { return getToken(GrammarParser.LPAR, 0); }
		public TerminalNode RPAR() { return getToken(GrammarParser.RPAR, 0); }
		public TerminalNode LSPAR() { return getToken(GrammarParser.LSPAR, 0); }
		public TerminalNode RSPAR() { return getToken(GrammarParser.RSPAR, 0); }
		public TerminalNode LCPAR() { return getToken(GrammarParser.LCPAR, 0); }
		public TerminalNode RCPAR() { return getToken(GrammarParser.RCPAR, 0); }
		public BexpressionContext bexpression() {
			return getRuleContext(BexpressionContext.class,0);
		}
		public ExpectationContext expectation() {
			return getRuleContext(ExpectationContext.class,0);
		}
		public CommandContext command() {
			return getRuleContext(CommandContext.class,0);
		}
		public WhileCmdContext(CommandContext ctx) { copyFrom(ctx); }
	}
	public static class UnifCmdContext extends CommandContext {
		public Token var;
		public Token lower;
		public Token upper;
		public TerminalNode ASS() { return getToken(GrammarParser.ASS, 0); }
		public TerminalNode UNIF() { return getToken(GrammarParser.UNIF, 0); }
		public TerminalNode LPAR() { return getToken(GrammarParser.LPAR, 0); }
		public TerminalNode RANGE() { return getToken(GrammarParser.RANGE, 0); }
		public TerminalNode RPAR() { return getToken(GrammarParser.RPAR, 0); }
		public TerminalNode VAR() { return getToken(GrammarParser.VAR, 0); }
		public List<TerminalNode> INT() { return getTokens(GrammarParser.INT); }
		public TerminalNode INT(int i) {
			return getToken(GrammarParser.INT, i);
		}
		public UnifCmdContext(CommandContext ctx) { copyFrom(ctx); }
	}
	public static class SkipCmdContext extends CommandContext {
		public TerminalNode SKIIP() { return getToken(GrammarParser.SKIIP, 0); }
		public SkipCmdContext(CommandContext ctx) { copyFrom(ctx); }
	}
	public static class NonDetCmdContext extends CommandContext {
		public CommandContext cmd1;
		public CommandContext cmd2;
		public List<TerminalNode> LCPAR() { return getTokens(GrammarParser.LCPAR); }
		public TerminalNode LCPAR(int i) {
			return getToken(GrammarParser.LCPAR, i);
		}
		public List<TerminalNode> RCPAR() { return getTokens(GrammarParser.RCPAR); }
		public TerminalNode RCPAR(int i) {
			return getToken(GrammarParser.RCPAR, i);
		}
		public TerminalNode LSPAR() { return getToken(GrammarParser.LSPAR, 0); }
		public TerminalNode RSPAR() { return getToken(GrammarParser.RSPAR, 0); }
		public List<CommandContext> command() {
			return getRuleContexts(CommandContext.class);
		}
		public CommandContext command(int i) {
			return getRuleContext(CommandContext.class,i);
		}
		public NonDetCmdContext(CommandContext ctx) { copyFrom(ctx); }
	}
	public static class IfElseCmdContext extends CommandContext {
		public BexpressionContext bexpr;
		public CommandContext cmdIf;
		public CommandContext cmdElse;
		public TerminalNode IF() { return getToken(GrammarParser.IF, 0); }
		public TerminalNode LPAR() { return getToken(GrammarParser.LPAR, 0); }
		public TerminalNode RPAR() { return getToken(GrammarParser.RPAR, 0); }
		public List<TerminalNode> LCPAR() { return getTokens(GrammarParser.LCPAR); }
		public TerminalNode LCPAR(int i) {
			return getToken(GrammarParser.LCPAR, i);
		}
		public List<TerminalNode> RCPAR() { return getTokens(GrammarParser.RCPAR); }
		public TerminalNode RCPAR(int i) {
			return getToken(GrammarParser.RCPAR, i);
		}
		public TerminalNode ELSE() { return getToken(GrammarParser.ELSE, 0); }
		public BexpressionContext bexpression() {
			return getRuleContext(BexpressionContext.class,0);
		}
		public List<CommandContext> command() {
			return getRuleContexts(CommandContext.class);
		}
		public CommandContext command(int i) {
			return getRuleContext(CommandContext.class,i);
		}
		public IfElseCmdContext(CommandContext ctx) { copyFrom(ctx); }
	}
	public static class AssCmdContext extends CommandContext {
		public Token var;
		public ExpressionContext expr;
		public TerminalNode ASS() { return getToken(GrammarParser.ASS, 0); }
		public TerminalNode VAR() { return getToken(GrammarParser.VAR, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public AssCmdContext(CommandContext ctx) { copyFrom(ctx); }
	}
	public static class SeqCmdContext extends CommandContext {
		public CommandContext cmd1;
		public CommandContext cmd2;
		public TerminalNode SEQ() { return getToken(GrammarParser.SEQ, 0); }
		public List<CommandContext> command() {
			return getRuleContexts(CommandContext.class);
		}
		public CommandContext command(int i) {
			return getRuleContext(CommandContext.class,i);
		}
		public SeqCmdContext(CommandContext ctx) { copyFrom(ctx); }
	}

	public final CommandContext command() throws RecognitionException {
		return command(0);
	}

	private CommandContext command(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		CommandContext _localctx = new CommandContext(_ctx, _parentState);
		CommandContext _prevctx = _localctx;
		int _startState = 16;
		enterRecursionRule(_localctx, 16, RULE_command, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(189);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,12,_ctx) ) {
			case 1:
				{
				_localctx = new AssCmdContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(135);
				((AssCmdContext)_localctx).var = match(VAR);
				setState(136);
				match(ASS);
				setState(137);
				((AssCmdContext)_localctx).expr = expression(0);
				}
				break;
			case 2:
				{
				_localctx = new UnifCmdContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(138);
				((UnifCmdContext)_localctx).var = match(VAR);
				setState(139);
				match(ASS);
				setState(140);
				match(UNIF);
				setState(141);
				match(LPAR);
				setState(142);
				((UnifCmdContext)_localctx).lower = match(INT);
				setState(143);
				match(RANGE);
				setState(144);
				((UnifCmdContext)_localctx).upper = match(INT);
				setState(145);
				match(RPAR);
				}
				break;
			case 3:
				{
				_localctx = new SkipCmdContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(146);
				match(SKIIP);
				}
				break;
			case 4:
				{
				_localctx = new ProbCmdContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(147);
				match(LCPAR);
				setState(148);
				((ProbCmdContext)_localctx).cmd1 = command(0);
				setState(149);
				match(RCPAR);
				setState(150);
				match(LSPAR);
				setState(151);
				((ProbCmdContext)_localctx).expr = expression(0);
				setState(152);
				match(RSPAR);
				setState(153);
				match(LCPAR);
				setState(154);
				((ProbCmdContext)_localctx).cmd2 = command(0);
				setState(155);
				match(RCPAR);
				}
				break;
			case 5:
				{
				_localctx = new NonDetCmdContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(157);
				match(LCPAR);
				setState(158);
				((NonDetCmdContext)_localctx).cmd1 = command(0);
				setState(159);
				match(RCPAR);
				setState(160);
				match(LSPAR);
				setState(161);
				match(RSPAR);
				setState(162);
				match(LCPAR);
				setState(163);
				((NonDetCmdContext)_localctx).cmd2 = command(0);
				setState(164);
				match(RCPAR);
				}
				break;
			case 6:
				{
				_localctx = new IfElseCmdContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(166);
				match(IF);
				setState(167);
				match(LPAR);
				setState(168);
				((IfElseCmdContext)_localctx).bexpr = bexpression(0);
				setState(169);
				match(RPAR);
				setState(170);
				match(LCPAR);
				setState(171);
				((IfElseCmdContext)_localctx).cmdIf = command(0);
				setState(172);
				match(RCPAR);
				setState(173);
				match(ELSE);
				setState(174);
				match(LCPAR);
				setState(175);
				((IfElseCmdContext)_localctx).cmdElse = command(0);
				setState(176);
				match(RCPAR);
				}
				break;
			case 7:
				{
				_localctx = new WhileCmdContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(178);
				match(WHILE);
				setState(179);
				match(LPAR);
				setState(180);
				((WhileCmdContext)_localctx).bexpr = bexpression(0);
				setState(181);
				match(RPAR);
				setState(182);
				match(LSPAR);
				setState(183);
				((WhileCmdContext)_localctx).inv = expectation();
				setState(184);
				match(RSPAR);
				setState(185);
				match(LCPAR);
				setState(186);
				((WhileCmdContext)_localctx).cmd = command(0);
				setState(187);
				match(RCPAR);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(196);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,13,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new SeqCmdContext(new CommandContext(_parentctx, _parentState));
					((SeqCmdContext)_localctx).cmd1 = _prevctx;
					pushNewRecursionContext(_localctx, _startState, RULE_command);
					setState(191);
					if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
					setState(192);
					match(SEQ);
					setState(193);
					((SeqCmdContext)_localctx).cmd2 = command(6);
					}
					} 
				}
				setState(198);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,13,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class ExpectationContext extends ParserRuleContext {
		public AexpectationContext aexpectation() {
			return getRuleContext(AexpectationContext.class,0);
		}
		public Expectation0Context expectation0() {
			return getRuleContext(Expectation0Context.class,0);
		}
		public ExpectationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expectation; }
	}

	public final ExpectationContext expectation() throws RecognitionException {
		ExpectationContext _localctx = new ExpectationContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_expectation);
		try {
			setState(201);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,14,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(199);
				aexpectation(0);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(200);
				expectation0(0);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AexpparContext extends ParserRuleContext {
		public AexpparContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_aexppar; }
	 
		public AexpparContext() { }
		public void copyFrom(AexpparContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class IntAExpParContext extends AexpparContext {
		public Token num;
		public TerminalNode INT() { return getToken(GrammarParser.INT, 0); }
		public IntAExpParContext(AexpparContext ctx) { copyFrom(ctx); }
	}
	public static class ExprAExpParContext extends AexpparContext {
		public AexpectationContext aexp;
		public TerminalNode LPAR() { return getToken(GrammarParser.LPAR, 0); }
		public TerminalNode RPAR() { return getToken(GrammarParser.RPAR, 0); }
		public AexpectationContext aexpectation() {
			return getRuleContext(AexpectationContext.class,0);
		}
		public ExprAExpParContext(AexpparContext ctx) { copyFrom(ctx); }
	}
	public static class VarAExpParContext extends AexpparContext {
		public Token var;
		public TerminalNode VAR() { return getToken(GrammarParser.VAR, 0); }
		public VarAExpParContext(AexpparContext ctx) { copyFrom(ctx); }
	}
	public static class RealAExpParContext extends AexpparContext {
		public Token num;
		public TerminalNode FLOAT() { return getToken(GrammarParser.FLOAT, 0); }
		public RealAExpParContext(AexpparContext ctx) { copyFrom(ctx); }
	}

	public final AexpparContext aexppar() throws RecognitionException {
		AexpparContext _localctx = new AexpparContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_aexppar);
		try {
			setState(210);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LPAR:
				_localctx = new ExprAExpParContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(203);
				match(LPAR);
				setState(204);
				((ExprAExpParContext)_localctx).aexp = aexpectation(0);
				setState(205);
				match(RPAR);
				}
				break;
			case INT:
				_localctx = new IntAExpParContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(207);
				((IntAExpParContext)_localctx).num = match(INT);
				}
				break;
			case FLOAT:
				_localctx = new RealAExpParContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(208);
				((RealAExpParContext)_localctx).num = match(FLOAT);
				}
				break;
			case VAR:
				_localctx = new VarAExpParContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(209);
				((VarAExpParContext)_localctx).var = match(VAR);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Expectation0Context extends ParserRuleContext {
		public Expectation0Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expectation0; }
	 
		public Expectation0Context() { }
		public void copyFrom(Expectation0Context ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class AExpContext extends Expectation0Context {
		public AexpparContext aexp;
		public AexpparContext aexppar() {
			return getRuleContext(AexpparContext.class,0);
		}
		public AExpContext(Expectation0Context ctx) { copyFrom(ctx); }
	}
	public static class BExpContext extends Expectation0Context {
		public BexpectationContext bexp;
		public TerminalNode LSPAR() { return getToken(GrammarParser.LSPAR, 0); }
		public TerminalNode RSPAR() { return getToken(GrammarParser.RSPAR, 0); }
		public BexpectationContext bexpectation() {
			return getRuleContext(BexpectationContext.class,0);
		}
		public BExpContext(Expectation0Context ctx) { copyFrom(ctx); }
	}
	public static class AddExpContext extends Expectation0Context {
		public Expectation0Context exp1;
		public Expectation0Context exp2;
		public TerminalNode PLUS() { return getToken(GrammarParser.PLUS, 0); }
		public List<Expectation0Context> expectation0() {
			return getRuleContexts(Expectation0Context.class);
		}
		public Expectation0Context expectation0(int i) {
			return getRuleContext(Expectation0Context.class,i);
		}
		public AddExpContext(Expectation0Context ctx) { copyFrom(ctx); }
	}
	public static class ScalExpContext extends Expectation0Context {
		public Expectation0Context exp;
		public AexpparContext aexp;
		public TerminalNode TIMES() { return getToken(GrammarParser.TIMES, 0); }
		public AexpparContext aexppar() {
			return getRuleContext(AexpparContext.class,0);
		}
		public Expectation0Context expectation0() {
			return getRuleContext(Expectation0Context.class,0);
		}
		public ScalExpContext(Expectation0Context ctx) { copyFrom(ctx); }
	}
	public static class ExpContext extends Expectation0Context {
		public Expectation0Context exp;
		public TerminalNode LPAR() { return getToken(GrammarParser.LPAR, 0); }
		public TerminalNode RPAR() { return getToken(GrammarParser.RPAR, 0); }
		public Expectation0Context expectation0() {
			return getRuleContext(Expectation0Context.class,0);
		}
		public ExpContext(Expectation0Context ctx) { copyFrom(ctx); }
	}
	public static class GuardExpContext extends Expectation0Context {
		public Expectation0Context exp;
		public BexpectationContext bexp;
		public TerminalNode LSPAR() { return getToken(GrammarParser.LSPAR, 0); }
		public TerminalNode RSPAR() { return getToken(GrammarParser.RSPAR, 0); }
		public TerminalNode TIMES() { return getToken(GrammarParser.TIMES, 0); }
		public BexpectationContext bexpectation() {
			return getRuleContext(BexpectationContext.class,0);
		}
		public Expectation0Context expectation0() {
			return getRuleContext(Expectation0Context.class,0);
		}
		public GuardExpContext(Expectation0Context ctx) { copyFrom(ctx); }
	}

	public final Expectation0Context expectation0() throws RecognitionException {
		return expectation0(0);
	}

	private Expectation0Context expectation0(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Expectation0Context _localctx = new Expectation0Context(_ctx, _parentState);
		Expectation0Context _prevctx = _localctx;
		int _startState = 22;
		enterRecursionRule(_localctx, 22, RULE_expectation0, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(232);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,16,_ctx) ) {
			case 1:
				{
				_localctx = new GuardExpContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(213);
				match(LSPAR);
				setState(214);
				((GuardExpContext)_localctx).bexp = bexpectation(0);
				setState(215);
				match(RSPAR);
				setState(216);
				match(TIMES);
				setState(217);
				((GuardExpContext)_localctx).exp = expectation0(7);
				}
				break;
			case 2:
				{
				_localctx = new ScalExpContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(219);
				((ScalExpContext)_localctx).aexp = aexppar();
				setState(220);
				match(TIMES);
				setState(221);
				((ScalExpContext)_localctx).exp = expectation0(5);
				}
				break;
			case 3:
				{
				_localctx = new ExpContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(223);
				match(LPAR);
				setState(224);
				((ExpContext)_localctx).exp = expectation0(0);
				setState(225);
				match(RPAR);
				}
				break;
			case 4:
				{
				_localctx = new AExpContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(227);
				((AExpContext)_localctx).aexp = aexppar();
				}
				break;
			case 5:
				{
				_localctx = new BExpContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(228);
				match(LSPAR);
				setState(229);
				((BExpContext)_localctx).bexp = bexpectation(0);
				setState(230);
				match(RSPAR);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(248);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,18,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(246);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,17,_ctx) ) {
					case 1:
						{
						_localctx = new AddExpContext(new Expectation0Context(_parentctx, _parentState));
						((AddExpContext)_localctx).exp1 = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expectation0);
						setState(234);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(235);
						match(PLUS);
						setState(236);
						((AddExpContext)_localctx).exp2 = expectation0(5);
						}
						break;
					case 2:
						{
						_localctx = new GuardExpContext(new Expectation0Context(_parentctx, _parentState));
						((GuardExpContext)_localctx).exp = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expectation0);
						setState(237);
						if (!(precpred(_ctx, 8))) throw new FailedPredicateException(this, "precpred(_ctx, 8)");
						setState(238);
						match(TIMES);
						setState(239);
						match(LSPAR);
						setState(240);
						((GuardExpContext)_localctx).bexp = bexpectation(0);
						setState(241);
						match(RSPAR);
						}
						break;
					case 3:
						{
						_localctx = new ScalExpContext(new Expectation0Context(_parentctx, _parentState));
						((ScalExpContext)_localctx).exp = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expectation0);
						setState(243);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(244);
						match(TIMES);
						setState(245);
						((ScalExpContext)_localctx).aexp = aexppar();
						}
						break;
					}
					} 
				}
				setState(250);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,18,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class ConstraintContext extends ParserRuleContext {
		public ConstraintContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_constraint; }
	 
		public ConstraintContext() { }
		public void copyFrom(ConstraintContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class ConsContext extends ConstraintContext {
		public Token op;
		public ExpectationContext exp;
		public ExpectationContext expectation() {
			return getRuleContext(ExpectationContext.class,0);
		}
		public TerminalNode EQ() { return getToken(GrammarParser.EQ, 0); }
		public TerminalNode NEQ() { return getToken(GrammarParser.NEQ, 0); }
		public TerminalNode GT() { return getToken(GrammarParser.GT, 0); }
		public TerminalNode LT() { return getToken(GrammarParser.LT, 0); }
		public TerminalNode GEQ() { return getToken(GrammarParser.GEQ, 0); }
		public TerminalNode LEQ() { return getToken(GrammarParser.LEQ, 0); }
		public ConsContext(ConstraintContext ctx) { copyFrom(ctx); }
	}

	public final ConstraintContext constraint() throws RecognitionException {
		ConstraintContext _localctx = new ConstraintContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_constraint);
		int _la;
		try {
			_localctx = new ConsContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(251);
			((ConsContext)_localctx).op = _input.LT(1);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << NEQ) | (1L << GEQ) | (1L << LEQ) | (1L << GT) | (1L << LT) | (1L << EQ))) != 0)) ) {
				((ConsContext)_localctx).op = (Token)_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(252);
			((ConsContext)_localctx).exp = expectation();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class InitializationContext extends ParserRuleContext {
		public InitializationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_initialization; }
	 
		public InitializationContext() { }
		public void copyFrom(InitializationContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class InitContext extends InitializationContext {
		public Token var;
		public Token start;
		public Token end;
		public Token init;
		public TerminalNode LSPAR() { return getToken(GrammarParser.LSPAR, 0); }
		public TerminalNode RANGE() { return getToken(GrammarParser.RANGE, 0); }
		public TerminalNode RSPAR() { return getToken(GrammarParser.RSPAR, 0); }
		public TerminalNode ARROW() { return getToken(GrammarParser.ARROW, 0); }
		public TerminalNode VAR() { return getToken(GrammarParser.VAR, 0); }
		public List<TerminalNode> INT() { return getTokens(GrammarParser.INT); }
		public TerminalNode INT(int i) {
			return getToken(GrammarParser.INT, i);
		}
		public InitContext(InitializationContext ctx) { copyFrom(ctx); }
	}
	public static class InitSeqContext extends InitializationContext {
		public InitializationContext left;
		public InitializationContext right;
		public TerminalNode SEQ() { return getToken(GrammarParser.SEQ, 0); }
		public List<InitializationContext> initialization() {
			return getRuleContexts(InitializationContext.class);
		}
		public InitializationContext initialization(int i) {
			return getRuleContext(InitializationContext.class,i);
		}
		public InitSeqContext(InitializationContext ctx) { copyFrom(ctx); }
	}
	public static class NoInitContext extends InitializationContext {
		public NoInitContext(InitializationContext ctx) { copyFrom(ctx); }
	}

	public final InitializationContext initialization() throws RecognitionException {
		return initialization(0);
	}

	private InitializationContext initialization(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		InitializationContext _localctx = new InitializationContext(_ctx, _parentState);
		InitializationContext _prevctx = _localctx;
		int _startState = 26;
		enterRecursionRule(_localctx, 26, RULE_initialization, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(263);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,19,_ctx) ) {
			case 1:
				{
				_localctx = new NoInitContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				}
				break;
			case 2:
				{
				_localctx = new InitContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(255);
				((InitContext)_localctx).var = match(VAR);
				setState(256);
				match(LSPAR);
				setState(257);
				((InitContext)_localctx).start = match(INT);
				setState(258);
				match(RANGE);
				setState(259);
				((InitContext)_localctx).end = match(INT);
				setState(260);
				match(RSPAR);
				setState(261);
				match(ARROW);
				setState(262);
				((InitContext)_localctx).init = match(INT);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(270);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,20,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new InitSeqContext(new InitializationContext(_parentctx, _parentState));
					((InitSeqContext)_localctx).left = _prevctx;
					pushNewRecursionContext(_localctx, _startState, RULE_initialization);
					setState(265);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(266);
					match(SEQ);
					setState(267);
					((InitSeqContext)_localctx).right = initialization(3);
					}
					} 
				}
				setState(272);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,20,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 4:
			return expression_sempred((ExpressionContext)_localctx, predIndex);
		case 5:
			return aexpectation_sempred((AexpectationContext)_localctx, predIndex);
		case 6:
			return bexpression_sempred((BexpressionContext)_localctx, predIndex);
		case 7:
			return bexpectation_sempred((BexpectationContext)_localctx, predIndex);
		case 8:
			return command_sempred((CommandContext)_localctx, predIndex);
		case 11:
			return expectation0_sempred((Expectation0Context)_localctx, predIndex);
		case 13:
			return initialization_sempred((InitializationContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expression_sempred(ExpressionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 5);
		case 1:
			return precpred(_ctx, 4);
		}
		return true;
	}
	private boolean aexpectation_sempred(AexpectationContext _localctx, int predIndex) {
		switch (predIndex) {
		case 2:
			return precpred(_ctx, 6);
		case 3:
			return precpred(_ctx, 5);
		}
		return true;
	}
	private boolean bexpression_sempred(BexpressionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 4:
			return precpred(_ctx, 4);
		case 5:
			return precpred(_ctx, 3);
		}
		return true;
	}
	private boolean bexpectation_sempred(BexpectationContext _localctx, int predIndex) {
		switch (predIndex) {
		case 6:
			return precpred(_ctx, 4);
		case 7:
			return precpred(_ctx, 3);
		}
		return true;
	}
	private boolean command_sempred(CommandContext _localctx, int predIndex) {
		switch (predIndex) {
		case 8:
			return precpred(_ctx, 5);
		}
		return true;
	}
	private boolean expectation0_sempred(Expectation0Context _localctx, int predIndex) {
		switch (predIndex) {
		case 9:
			return precpred(_ctx, 4);
		case 10:
			return precpred(_ctx, 8);
		case 11:
			return precpred(_ctx, 6);
		}
		return true;
	}
	private boolean initialization_sempred(InitializationContext _localctx, int predIndex) {
		switch (predIndex) {
		case 12:
			return precpred(_ctx, 2);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3,\u0114\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3"+
		"\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\65\n\6"+
		"\3\6\3\6\3\6\3\6\3\6\3\6\7\6=\n\6\f\6\16\6@\13\6\3\7\3\7\3\7\3\7\3\7\3"+
		"\7\3\7\3\7\5\7J\n\7\3\7\3\7\3\7\3\7\3\7\3\7\7\7R\n\7\f\7\16\7U\13\7\3"+
		"\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\bc\n\b\3\b\3\b\3\b\3"+
		"\b\3\b\3\b\7\bk\n\b\f\b\16\bn\13\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t"+
		"\3\t\3\t\3\t\5\t|\n\t\3\t\3\t\3\t\3\t\3\t\3\t\7\t\u0084\n\t\f\t\16\t\u0087"+
		"\13\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n"+
		"\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3"+
		"\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n"+
		"\3\n\3\n\3\n\3\n\5\n\u00c0\n\n\3\n\3\n\3\n\7\n\u00c5\n\n\f\n\16\n\u00c8"+
		"\13\n\3\13\3\13\5\13\u00cc\n\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u00d5"+
		"\n\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3"+
		"\r\3\r\3\r\3\r\5\r\u00eb\n\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3"+
		"\r\3\r\7\r\u00f9\n\r\f\r\16\r\u00fc\13\r\3\16\3\16\3\16\3\17\3\17\3\17"+
		"\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u010a\n\17\3\17\3\17\3\17\7\17\u010f"+
		"\n\17\f\17\16\17\u0112\13\17\3\17\2\t\n\f\16\20\22\30\34\20\2\4\6\b\n"+
		"\f\16\20\22\24\26\30\32\34\2\6\3\2\34\35\4\2\27\27\36\37\3\2\6\7\5\2\22"+
		"\24\32\33\"\"\2\u012c\2\36\3\2\2\2\4!\3\2\2\2\6%\3\2\2\2\b)\3\2\2\2\n"+
		"\64\3\2\2\2\fI\3\2\2\2\16b\3\2\2\2\20{\3\2\2\2\22\u00bf\3\2\2\2\24\u00cb"+
		"\3\2\2\2\26\u00d4\3\2\2\2\30\u00ea\3\2\2\2\32\u00fd\3\2\2\2\34\u0109\3"+
		"\2\2\2\36\37\5\22\n\2\37 \7\2\2\3 \3\3\2\2\2!\"\7\3\2\2\"#\5\24\13\2#"+
		"$\7\2\2\3$\5\3\2\2\2%&\7\4\2\2&\'\5\32\16\2\'(\7\2\2\3(\7\3\2\2\2)*\7"+
		"\5\2\2*+\5\34\17\2+,\7\2\2\3,\t\3\2\2\2-.\b\6\1\2.\65\7\'\2\2/\60\7\13"+
		"\2\2\60\61\5\n\6\2\61\62\7\f\2\2\62\65\3\2\2\2\63\65\7+\2\2\64-\3\2\2"+
		"\2\64/\3\2\2\2\64\63\3\2\2\2\65>\3\2\2\2\66\67\f\7\2\2\678\t\2\2\28=\5"+
		"\n\6\b9:\f\6\2\2:;\t\3\2\2;=\5\n\6\7<\66\3\2\2\2<9\3\2\2\2=@\3\2\2\2>"+
		"<\3\2\2\2>?\3\2\2\2?\13\3\2\2\2@>\3\2\2\2AB\b\7\1\2BC\7\13\2\2CD\5\f\7"+
		"\2DE\7\f\2\2EJ\3\2\2\2FJ\7\'\2\2GJ\7(\2\2HJ\7+\2\2IA\3\2\2\2IF\3\2\2\2"+
		"IG\3\2\2\2IH\3\2\2\2JS\3\2\2\2KL\f\b\2\2LM\t\2\2\2MR\5\f\7\tNO\f\7\2\2"+
		"OP\t\3\2\2PR\5\f\7\bQK\3\2\2\2QN\3\2\2\2RU\3\2\2\2SQ\3\2\2\2ST\3\2\2\2"+
		"T\r\3\2\2\2US\3\2\2\2VW\b\b\1\2Wc\t\4\2\2XY\7!\2\2Yc\5\16\b\7Z[\5\n\6"+
		"\2[\\\t\5\2\2\\]\5\n\6\2]c\3\2\2\2^_\7\13\2\2_`\5\16\b\2`a\7\f\2\2ac\3"+
		"\2\2\2bV\3\2\2\2bX\3\2\2\2bZ\3\2\2\2b^\3\2\2\2cl\3\2\2\2de\f\6\2\2ef\7"+
		"\25\2\2fk\5\16\b\7gh\f\5\2\2hi\7\26\2\2ik\5\16\b\6jd\3\2\2\2jg\3\2\2\2"+
		"kn\3\2\2\2lj\3\2\2\2lm\3\2\2\2m\17\3\2\2\2nl\3\2\2\2op\b\t\1\2p|\t\4\2"+
		"\2qr\7!\2\2r|\5\20\t\7st\5\f\7\2tu\t\5\2\2uv\5\f\7\2v|\3\2\2\2wx\7\13"+
		"\2\2xy\5\20\t\2yz\7\f\2\2z|\3\2\2\2{o\3\2\2\2{q\3\2\2\2{s\3\2\2\2{w\3"+
		"\2\2\2|\u0085\3\2\2\2}~\f\6\2\2~\177\7\25\2\2\177\u0084\5\20\t\7\u0080"+
		"\u0081\f\5\2\2\u0081\u0082\7\26\2\2\u0082\u0084\5\20\t\6\u0083}\3\2\2"+
		"\2\u0083\u0080\3\2\2\2\u0084\u0087\3\2\2\2\u0085\u0083\3\2\2\2\u0085\u0086"+
		"\3\2\2\2\u0086\21\3\2\2\2\u0087\u0085\3\2\2\2\u0088\u0089\b\n\1\2\u0089"+
		"\u008a\7+\2\2\u008a\u008b\7\21\2\2\u008b\u00c0\5\n\6\2\u008c\u008d\7+"+
		"\2\2\u008d\u008e\7\21\2\2\u008e\u008f\7#\2\2\u008f\u0090\7\13\2\2\u0090"+
		"\u0091\7\'\2\2\u0091\u0092\7\30\2\2\u0092\u0093\7\'\2\2\u0093\u00c0\7"+
		"\f\2\2\u0094\u00c0\7$\2\2\u0095\u0096\7\17\2\2\u0096\u0097\5\22\n\2\u0097"+
		"\u0098\7\20\2\2\u0098\u0099\7\r\2\2\u0099\u009a\5\n\6\2\u009a\u009b\7"+
		"\16\2\2\u009b\u009c\7\17\2\2\u009c\u009d\5\22\n\2\u009d\u009e\7\20\2\2"+
		"\u009e\u00c0\3\2\2\2\u009f\u00a0\7\17\2\2\u00a0\u00a1\5\22\n\2\u00a1\u00a2"+
		"\7\20\2\2\u00a2\u00a3\7\r\2\2\u00a3\u00a4\7\16\2\2\u00a4\u00a5\7\17\2"+
		"\2\u00a5\u00a6\5\22\n\2\u00a6\u00a7\7\20\2\2\u00a7\u00c0\3\2\2\2\u00a8"+
		"\u00a9\7\b\2\2\u00a9\u00aa\7\13\2\2\u00aa\u00ab\5\16\b\2\u00ab\u00ac\7"+
		"\f\2\2\u00ac\u00ad\7\17\2\2\u00ad\u00ae\5\22\n\2\u00ae\u00af\7\20\2\2"+
		"\u00af\u00b0\7\t\2\2\u00b0\u00b1\7\17\2\2\u00b1\u00b2\5\22\n\2\u00b2\u00b3"+
		"\7\20\2\2\u00b3\u00c0\3\2\2\2\u00b4\u00b5\7\n\2\2\u00b5\u00b6\7\13\2\2"+
		"\u00b6\u00b7\5\16\b\2\u00b7\u00b8\7\f\2\2\u00b8\u00b9\7\r\2\2\u00b9\u00ba"+
		"\5\24\13\2\u00ba\u00bb\7\16\2\2\u00bb\u00bc\7\17\2\2\u00bc\u00bd\5\22"+
		"\n\2\u00bd\u00be\7\20\2\2\u00be\u00c0\3\2\2\2\u00bf\u0088\3\2\2\2\u00bf"+
		"\u008c\3\2\2\2\u00bf\u0094\3\2\2\2\u00bf\u0095\3\2\2\2\u00bf\u009f\3\2"+
		"\2\2\u00bf\u00a8\3\2\2\2\u00bf\u00b4\3\2\2\2\u00c0\u00c6\3\2\2\2\u00c1"+
		"\u00c2\f\7\2\2\u00c2\u00c3\7 \2\2\u00c3\u00c5\5\22\n\b\u00c4\u00c1\3\2"+
		"\2\2\u00c5\u00c8\3\2\2\2\u00c6\u00c4\3\2\2\2\u00c6\u00c7\3\2\2\2\u00c7"+
		"\23\3\2\2\2\u00c8\u00c6\3\2\2\2\u00c9\u00cc\5\f\7\2\u00ca\u00cc\5\30\r"+
		"\2\u00cb\u00c9\3\2\2\2\u00cb\u00ca\3\2\2\2\u00cc\25\3\2\2\2\u00cd\u00ce"+
		"\7\13\2\2\u00ce\u00cf\5\f\7\2\u00cf\u00d0\7\f\2\2\u00d0\u00d5\3\2\2\2"+
		"\u00d1\u00d5\7\'\2\2\u00d2\u00d5\7(\2\2\u00d3\u00d5\7+\2\2\u00d4\u00cd"+
		"\3\2\2\2\u00d4\u00d1\3\2\2\2\u00d4\u00d2\3\2\2\2\u00d4\u00d3\3\2\2\2\u00d5"+
		"\27\3\2\2\2\u00d6\u00d7\b\r\1\2\u00d7\u00d8\7\r\2\2\u00d8\u00d9\5\20\t"+
		"\2\u00d9\u00da\7\16\2\2\u00da\u00db\7\34\2\2\u00db\u00dc\5\30\r\t\u00dc"+
		"\u00eb\3\2\2\2\u00dd\u00de\5\26\f\2\u00de\u00df\7\34\2\2\u00df\u00e0\5"+
		"\30\r\7\u00e0\u00eb\3\2\2\2\u00e1\u00e2\7\13\2\2\u00e2\u00e3\5\30\r\2"+
		"\u00e3\u00e4\7\f\2\2\u00e4\u00eb\3\2\2\2\u00e5\u00eb\5\26\f\2\u00e6\u00e7"+
		"\7\r\2\2\u00e7\u00e8\5\20\t\2\u00e8\u00e9\7\16\2\2\u00e9\u00eb\3\2\2\2"+
		"\u00ea\u00d6\3\2\2\2\u00ea\u00dd\3\2\2\2\u00ea\u00e1\3\2\2\2\u00ea\u00e5"+
		"\3\2\2\2\u00ea\u00e6\3\2\2\2\u00eb\u00fa\3\2\2\2\u00ec\u00ed\f\6\2\2\u00ed"+
		"\u00ee\7\36\2\2\u00ee\u00f9\5\30\r\7\u00ef\u00f0\f\n\2\2\u00f0\u00f1\7"+
		"\34\2\2\u00f1\u00f2\7\r\2\2\u00f2\u00f3\5\20\t\2\u00f3\u00f4\7\16\2\2"+
		"\u00f4\u00f9\3\2\2\2\u00f5\u00f6\f\b\2\2\u00f6\u00f7\7\34\2\2\u00f7\u00f9"+
		"\5\26\f\2\u00f8\u00ec\3\2\2\2\u00f8\u00ef\3\2\2\2\u00f8\u00f5\3\2\2\2"+
		"\u00f9\u00fc\3\2\2\2\u00fa\u00f8\3\2\2\2\u00fa\u00fb\3\2\2\2\u00fb\31"+
		"\3\2\2\2\u00fc\u00fa\3\2\2\2\u00fd\u00fe\t\5\2\2\u00fe\u00ff\5\24\13\2"+
		"\u00ff\33\3\2\2\2\u0100\u010a\b\17\1\2\u0101\u0102\7+\2\2\u0102\u0103"+
		"\7\r\2\2\u0103\u0104\7\'\2\2\u0104\u0105\7\30\2\2\u0105\u0106\7\'\2\2"+
		"\u0106\u0107\7\16\2\2\u0107\u0108\7\31\2\2\u0108\u010a\7\'\2\2\u0109\u0100"+
		"\3\2\2\2\u0109\u0101\3\2\2\2\u010a\u0110\3\2\2\2\u010b\u010c\f\4\2\2\u010c"+
		"\u010d\7 \2\2\u010d\u010f\5\34\17\5\u010e\u010b\3\2\2\2\u010f\u0112\3"+
		"\2\2\2\u0110\u010e\3\2\2\2\u0110\u0111\3\2\2\2\u0111\35\3\2\2\2\u0112"+
		"\u0110\3\2\2\2\27\64<>IQSbjl{\u0083\u0085\u00bf\u00c6\u00cb\u00d4\u00ea"+
		"\u00f8\u00fa\u0109\u0110";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}