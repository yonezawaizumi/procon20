package com.wsf_lp.procon20.roman

trait RomanBase extends App {

  def parseRoman(str: String): Int = -1

  RomanData.data.foreach { t =>
    val value = parseRoman(t._2)
    if (t._1 != value) {
      println(s"illegal format ${t._1} (result $value)")
    }
  }
}