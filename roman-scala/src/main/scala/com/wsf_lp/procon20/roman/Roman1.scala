package com.wsf_lp.procon20.roman

object Roman1 extends RomanBase {

  sealed case class ParseResult(chrs: Seq[Char], num: Int) {
    def +(add: Int) = ParseResult(chrs, num + add)
  }

  private def parseRepeated(chrs: Seq[Char], chr: Char, mul: Int): Option[ParseResult] = {
    val next = chrs.indexWhere(_ != chr)
    val drop = if (next >= 0) next else chrs.length
    if (drop <= 3) {
      Some(ParseResult(chrs.drop(drop), drop * mul))
    } else {
      None
    }
  }

  private def parseThousand(chrs: Seq[Char]): Option[ParseResult] = parseRepeated(chrs, 'M', 1000)

  private def parseDigit(chrs: Seq[Char], chr1: Char, chr5: Char, chr10: Char, mul: Int): Option[ParseResult] =
    chrs.headOption match {
      case Some(c) if c == chr1 =>
        chrs.tail.headOption match {
          case Some(cc) if cc == chr10 =>
            Some(ParseResult(chrs.drop(2), mul * 9))
          case Some(cc) if cc == chr5 =>
            Some(ParseResult(chrs.drop(2), mul * 4))
          case Some(cc) if cc == chr1 =>
            parseRepeated(chrs, chr1, mul)
          case _ =>
            Some(ParseResult(chrs.tail, mul))
        }
      case Some(c) if c == chr5 =>
        parseRepeated(chrs.tail, chr1, mul).map(_ + mul * 5)
      case _ =>
        Some(ParseResult(chrs, 0))
    }

  override def parseRoman(str: String): Int = (for {
    t <- parseThousand(str)
    h <- parseDigit(t.chrs, 'C', 'D', 'M', 100)
    e <- parseDigit(h.chrs, 'X', 'L', 'C', 10)
    o <- parseDigit(e.chrs, 'I', 'V', 'X', 1)
  } yield {
    if (o.chrs.isEmpty) t.num + h.num + e.num + o.num else -1
  }).getOrElse(-1)
}
