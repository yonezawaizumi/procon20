package com.wsf_lp.procon20.roman

import scala.util.matching.Regex
import scala.util.parsing.combinator._

object Roman3 extends RomanBase {

  object RomanNumeralsParser extends RegexParsers {

    override val whiteSpace: Regex = "".r

    private def createParser(chr1: Char, chro5: Option[Char], chro10: Option[Char], mul: Int): Parser[Int] = {
      val p1 = (chr1.toString + "{0,3}").r ^^ (_.length * mul)
      (for {
        chr5 <- chro5
        chr10 <- chro10
      } yield {
        (chr1.toString + chr10) ^^ (_ => 9 * mul) |
        (chr5.toString + chr1 + "{0,3}").r ^^ (s => (s.length() + 4) * mul) |
        (chr1.toString + chr5) ^^ (_ => 4 * mul) |
        p1
      }).getOrElse(p1)
    }

    lazy val romanNumerals: Parser[Int] =
      createParser('M', None, None, 1000) ~!
      createParser('C', Some('D'), Some('M'), 100) ~!
      createParser('X', Some('L'), Some('C'), 10) ~!
      createParser('I', Some('V'), Some('X'), 1) ^^ {
      case t ~ h ~ e ~ o => t + h + e + o
    }

    def parseRoman(str:String): Int = parseAll(romanNumerals, str) match {
      case Success(num, next) => num
      case NoSuccess(errorMessage, next) => -1
    }
  }

  override def parseRoman(str: String): Int = RomanNumeralsParser.parseRoman(str)
}
