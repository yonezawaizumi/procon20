package com.wsf_lp.procon20.roman

import scala.util.matching.Regex
import scala.util.parsing.combinator._

object Roman2 extends RomanBase {

  object RomanNumeralsParser extends RegexParsers {

    override val whiteSpace: Regex = "".r

    lazy val thousand: Parser[Int] = "M{0,3}".r ^^ (_.length * 1000)

    lazy val hundred9: Parser[Int] = "CM" ^^ (_ => 900)
    lazy val hundred5: Parser[Int] = "DC{0,3}".r ^^ (_.length() * 100 - 100 + 500)
    lazy val hundred4: Parser[Int] = "CD" ^^ (_ => 400)
    lazy val hundred1: Parser[Int] = "C{0,3}".r ^^ (_.length * 100)

    lazy val hundred: Parser[Int] = hundred9 | hundred5 | hundred4 | hundred1

    lazy val ten9: Parser[Int] = "XC" ^^ (_ => 90)
    lazy val ten5: Parser[Int] = "LX{0,3}".r ^^ (_.length() * 10 - 10 + 50)
    lazy val ten4: Parser[Int] = "XL" ^^ (_ => 40)
    lazy val ten1: Parser[Int] = "X{0,3}".r ^^ (_.length * 10)

    lazy val ten: Parser[Int] = ten9 | ten5 | ten4 | ten1

    lazy val one9: Parser[Int] = "IX" ^^ (_ => 9)
    lazy val one5: Parser[Int] = "VI{0,3}".r ^^ (_.length() - 1 + 5)
    lazy val one4: Parser[Int] = "IV" ^^ (_ => 4)
    lazy val one1: Parser[Int] = "I{0,3}".r ^^ (_.length)

    lazy val one: Parser[Int] = one9 | one5 | one4 | one1

    lazy val romanNumerals: Parser[Int] = thousand ~! hundred ~! ten ~! one ^^ {
      case t ~ h ~ e ~ o => t + h + e + o
    }

    def parseRoman(str:String): Int = parseAll(romanNumerals, str) match {
      case Success(num, next) => num
      case NoSuccess(errorMessage, next) => -1
    }
  }

  override def parseRoman(str: String): Int = RomanNumeralsParser.parseRoman(str)
}
