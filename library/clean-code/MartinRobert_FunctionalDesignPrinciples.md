![](cover.jpeg)

[]{#titlepage.xhtml}

<div>

```{=html}
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" width="100%" height="100%" viewbox="0 0 800 1046" preserveaspectratio="none">
```
`<image width="800" height="1046" xlink:href="cover.jpeg">`{=html}`</image>`{=html}
```{=html}
</svg>
```

</div>

[]{#index_split_000.html}

![](images/00280.jpg){.calibre_1}

::: {#index_split_000.html#calibre_pb_0 .mbp_pagebreak}
:::

[]{#index_split_001.html}

[[[About This eBook]{.calibre_3}]{.bold}]{.calibre1}

ePUB is an open, industry-standard format for eBooks. However, support of ePUB and its many features varies across reading devices and applications. Use your device or app settings to customize the presentation to your liking. Settings that you can customize often include font, font size, single or double column, landscape or portrait mode, and figures that you can click or tap to enlarge. For additional information about the settings and features on your reading device or app, visit the device manufacturer's Web site.

Many titles include programming code or configuration examples. To optimize the presentation of these elements, view the eBook in single-column, landscape mode and adjust the font size to the smallest setting. In addition to presenting code and configurations in the reflowable text format, we have included images of the code that mimic the presentation found in the print book; therefore, where the reflowable format may compromise the presentation of the code listing, you will see a "Click here to view code image" link. Click the link to view the print-fidelity code image. To return to the previous page viewed, click the Back button on your device or app.

::: {#index_split_001.html#calibre_pb_1 .mbp_pagebreak}
:::

[]{#index_split_002.html}

[[Functional Design]{.calibre_3}]{.calibre2}

::: {#index_split_002.html#calibre_pb_2 .mbp_pagebreak}
:::

[]{#index_split_003.html}

![](images/00322.jpg){.calibre_7}

::: {#index_split_003.html#calibre_pb_3 .mbp_pagebreak}
:::

[]{#index_split_004.html}

[[Functional Design]{.calibre_3}]{.calibre2}

Principles, Patterns, and Practices

Robert C. Martin

![](images/00192.jpg){.calibre_9}

Hoboken, New Jersey

::: {#index_split_004.html#calibre_pb_4 .mbp_pagebreak}
:::

[]{#index_split_005.html}

Cover image courtesy of NASA, ESA, CSA, STScI, Webb ERO Production Team. Use of this image does not convey an endorsement of this or any content by the above credited.

[[[Page xxiii]{.underline}]{.calibre_10}](#index_split_011.html#filepos59777): Author photo courtesy of Robert C. Martin.

Many of the designations used by manufacturers and sellers to distinguish their products are claimed as trademarks. Where those designations appear in this book, and the publisher was aware of a trademark claim, the designations have been printed with initial capital letters or in all capitals.

The author and publisher have taken care in the preparation of this book, but make no expressed or implied warranty of any kind and assume no responsibility for errors or omissions. No liability is assumed for incidental or consequential damages in connection with or arising out of the use of the information or programs contained herein.

For information about buying this title in bulk quantities, or for special sales opportunities (which may include electronic versions; custom cover designs; and content particular to your business, training goals, marketing focus, or branding interests), please contact our corporate sales department at [[[corpsales@pearsoned.com]{.underline}]{.calibre_10}](mailto:corpsales@pearsoned.com) or (800) 382-3419.

For government sales inquiries, please contact [[[governmentsales@pearsoned.com]{.underline}]{.calibre_10}](mailto:governmentsales@pearsoned.com).

For questions about sales outside the U.S., please contact [[[intlcs@pearson.com]{.underline}]{.calibre_10}](mailto:intlcs@pearson.com).

Visit us on the Web: [[[informit.com/aw]{.underline}]{.calibre_10}](http://informit.com/aw)

Library of Congress Control Number: 2023940397

Copyright © 2024 Pearson Education, Inc.

All rights reserved. This publication is protected by copyright, and permission must be obtained from the publisher prior to any prohibited reproduction, storage in a retrieval system, or transmission in any form or by any means, electronic, mechanical, photocopying, recording, or likewise. For information regarding permissions, request forms and the appropriate contacts within the Pearson Education Global Rights & Permissions Department, please visit [[[www.pearson.com/permissions]{.underline}]{.calibre_10}](http://www.pearson.com/permissions).

ISBN-13: 978-0-13-817639-6

ISBN-10: 0-13-817639-6

::: {#index_split_005.html#calibre_pb_5 .mbp_pagebreak}
:::

[]{#index_split_006.html}

[[[Dedication]{.calibre_3}]{.bold}]{.calibre1}

To my family, my love for them explains everything I do.

First, to my wife of 50 years, the gorgeous 16-year-old with glistening brown eyes and long, flowing black hair who captured my heart and has held it for more than half a century. She remains as gorgeous as the day I met her. Those glistening brown eyes and flowing locks enrapture me every day. The mother of my children. The anchor of my life. My one and only love.

To Angela, my beautiful firstborn and ever-faithful daughter whose devastatingly contagious smile will melt your heart and convince you that all is right with the world. I once asked her what she wanted to be. Her answer was "Fun!" She went on to achieve, and far exceed, that goal. Her boundless enthusiasm for life infects everyone she encounters. She married Matt, a wonderful, hardworking, and honest (and fun) man. Together the two of them have turned the fun they share into a mountain-biking frenzy of gainful employment. They live on a wooded hilltop and have raised three beautiful, intelligent, and talented daughters for me to spoil.

To Micah, my second-born and passionately dedicated son. He inherited his mother's glistening brown eyes. I once asked him what he wanted to be. He said, "Rich!" I'm happy to report that he has done quite well. He spent the better part of a decade working with me and then founded his own software business, which he sold some years later. Then he spent a year building an airplane in his garage. Now he's running yet another software business. Much of his success is due to Angelique, the beautiful, hardworking, and deeply intelligent woman he married. They have raised two spectacular young men.

To Gina, my third-born and endlessly surprising daughter. If it is possible for a woman to be more beautiful than my wife, Gina is that woman. She became an accomplished chemical engineer, working with such pleasant substances as uranium, fluorine, and concentrated sodium hydroxide. She donned hard hats, climbed reaction vessels, and managed teams of chemical plant operators. She married Keith, a wonderful, hardworking, and honest mechanical engineer. The two of them swap stories about their adventures at big and complex chemical plants. They have produced three (2.9 as of this writing) of my grandsons. More than three years ago, struggling with the competing pressures of motherhood, work, and the pandemic, she asked me if I thought a career change to software engineer might be possible. Oh yeah, it was possible, all right. She's crushing it! And, by the way, her industrial experience is a big factor in just why she is crushing it.

To Justin, my last-born and confidently competent son. Justin is a deeply analytical soul for whom no problem is insoluble, no challenge is unmeetable, and no wrong is un-rightable. If that sounds a tad quixotic, be assured that he is also a pragmatist of the highest order. He chooses his battles well. He also has this annoying tendency to be . . . right. He called his mother and me in January of 2020 and told us a very serious pandemic was coming. He recommended getting into cryptocurrencies and made quite a nice nest egg with his speculations. He is a software engineer [par excellence]{.italic} and currently runs a software team for a company in Austin. He married Ela, a fiery, gorgeous young redhead whose intelligence and integrity are exceeded only by her courage. They have produced two beautiful children---a boy and a girl---the first of my children's families to enjoy that particular privilege.

Happy is the man who has his quiverful of children and grandchildren.

::: {#index_split_006.html#calibre_pb_6 .mbp_pagebreak}
:::

[]{#index_split_007.html}

[[[Contents]{.calibre_3}]{.bold}]{.calibre1}

::: calibre_11
 
:::

1.  [[[Foreword]{.underline}]{.calibre_10}](#index_split_008.html#filepos41757)

2.  [[[Preface]{.underline}]{.calibre_10}](#index_split_009.html#filepos45250)

3.  [[[Acknowledgments]{.underline}]{.calibre_10}](#index_split_010.html#filepos56782)

4.  [[[About the Author]{.underline}]{.calibre_10}](#index_split_011.html#filepos59777)

5.  [[[PART I Functional Basics]{.underline}]{.calibre_10}](#index_split_012.html#filepos60975)

    1.  [[[Chapter 1 Immutability]{.underline}]{.calibre_10}](#index_split_013.html#filepos61201)

        1.  [[[What Is Functional Programming?]{.underline}]{.calibre_10}](#index_split_013.html#filepos61537)

        2.  [[[The Problem with Assignment]{.underline}]{.calibre_10}](#index_split_013.html#filepos69578)

        3.  [[[So Why Is It Called Functional?]{.underline}]{.calibre_10}](#index_split_013.html#filepos77699)

        4.  [[[No Change of State?]{.underline}]{.calibre_10}](#index_split_013.html#filepos81640)

        5.  [[[Immutability]{.underline}]{.calibre_10}](#index_split_013.html#filepos88989)

    2.  [[[Chapter 2 Persistent Data]{.underline}]{.calibre_10}](#index_split_014.html#filepos89882)

        1.  [[[On Cheating]{.underline}]{.calibre_10}](#index_split_014.html#filepos92972)

        2.  [[[Making Copies]{.underline}]{.calibre_10}](#index_split_014.html#filepos95472)

        3.  [[[Structural Sharing]{.underline}]{.calibre_10}](#index_split_014.html#filepos100426)

    3.  [[[Chapter 3 Recursion and Iteration]{.underline}]{.calibre_10}](#index_split_015.html#filepos105855)

        1.  [[[Iteration]{.underline}]{.calibre_10}](#index_split_015.html#filepos106588)

            1.  [[[Very Brief Clojure Tutorial]{.underline}]{.calibre_10}](#index_split_015.html#filepos108794)

            2.  [[[Iteration]{.underline}]{.calibre_10}](#index_split_015.html#filepos119128)

            3.  [[[TCO, Clojure, and the JVM]{.underline}]{.calibre_10}](#index_split_015.html#filepos119825)

        2.  [[[Recursion]{.underline}]{.calibre_10}](#index_split_015.html#filepos120994)

    4.  [[[Chapter 4 Laziness]{.underline}]{.calibre_10}](#index_split_016.html#filepos129566)

        1.  [[[Lazy Accumulation]{.underline}]{.calibre_10}](#index_split_016.html#filepos136884)

        2.  [[[OK, but Why?]{.underline}]{.calibre_10}](#index_split_016.html#filepos138979)

        3.  [[[Coda]{.underline}]{.calibre_10}](#index_split_016.html#filepos142914)

    5.  [[[Chapter 5 Statefulness]{.underline}]{.calibre_10}](#index_split_017.html#filepos143328)

        1.  [[[When We MUST Mutate]{.underline}]{.calibre_10}](#index_split_017.html#filepos154519)

        2.  [[[Software Transactional Memory (STM)]{.underline}]{.calibre_10}](#index_split_017.html#filepos157690)

        3.  [[[Life Is Hard, Software Is Harder]{.underline}]{.calibre_10}](#index_split_017.html#filepos164921)

6.  [[[PART II Comparative Analysis]{.underline}]{.calibre_10}](#index_split_018.html#filepos165870)

    1.  [[[Chapter 6 Prime Factors]{.underline}]{.calibre_10}](#index_split_019.html#filepos168235)

        1.  [[[Java Version]{.underline}]{.calibre_10}](#index_split_019.html#filepos169449)

        2.  [[[Clojure Version]{.underline}]{.calibre_10}](#index_split_019.html#filepos181735)

        3.  [[[Conclusion]{.underline}]{.calibre_10}](#index_split_019.html#filepos192763)

    2.  [[[Chapter 7 Bowling Game]{.underline}]{.calibre_10}](#index_split_020.html#filepos195319)

        1.  [[[Java Version]{.underline}]{.calibre_10}](#index_split_020.html#filepos196374)

        2.  [[[Clojure Version]{.underline}]{.calibre_10}](#index_split_020.html#filepos209211)

        3.  [[[Conclusion]{.underline}]{.calibre_10}](#index_split_020.html#filepos223629)

    3.  [[[Chapter 8 Gossiping Bus Drivers]{.underline}]{.calibre_10}](#index_split_021.html#filepos226628)

        1.  [[[Java Solution]{.underline}]{.calibre_10}](#index_split_021.html#filepos229211)

            1.  [[[Driver]{.underline}]{.calibre_10}](#index_split_021.html#filepos239266)

            2.  [[[Route]{.underline}]{.calibre_10}](#index_split_021.html#filepos240919)

            3.  [[[Stop]{.underline}]{.calibre_10}](#index_split_021.html#filepos242081)

            4.  [[[Rumor]{.underline}]{.calibre_10}](#index_split_021.html#filepos243686)

            5.  [[[Simulation]{.underline}]{.calibre_10}](#index_split_021.html#filepos244226)

        2.  [[[Clojure]{.underline}]{.calibre_10}](#index_split_021.html#filepos246110)

        3.  [[[Conclusion]{.underline}]{.calibre_10}](#index_split_021.html#filepos261104)

    4.  [[[Chapter 9 Object-Oriented Programming]{.underline}]{.calibre_10}](#index_split_022.html#filepos262956)

        1.  [[[Functional Payroll]{.underline}]{.calibre_10}](#index_split_022.html#filepos269664)

        2.  [[[Namespaces and Source Files]{.underline}]{.calibre_10}](#index_split_022.html#filepos293399)

        3.  [[[Conclusion]{.underline}]{.calibre_10}](#index_split_022.html#filepos295167)

    5.  [[[Chapter 10 Types]{.underline}]{.calibre_10}](#index_split_023.html#filepos296573)

7.  [[[PART III Functional Design]{.underline}]{.calibre_10}](#index_split_024.html#filepos312349)

    1.  [[[Chapter 11 Data Flow]{.underline}]{.calibre_10}](#index_split_025.html#filepos312584)

    2.  [[[Chapter 12 SOLID]{.underline}]{.calibre_10}](#index_split_026.html#filepos328898)

        1.  [[[The Single Responsibility Principle (SRP)]{.underline}]{.calibre_10}](#index_split_026.html#filepos331488)

        2.  [[[The Open-Closed Principle (OCP)]{.underline}]{.calibre_10}](#index_split_026.html#filepos342577)

            1.  [[[Functions]{.underline}]{.calibre_10}](#index_split_026.html#filepos346402)

            2.  [[[Objects with Vtables]{.underline}]{.calibre_10}](#index_split_026.html#filepos349198)

            3.  [[[Multi-methods]{.underline}]{.calibre_10}](#index_split_026.html#filepos351742)

            4.  [[[Independent Deployability]{.underline}]{.calibre_10}](#index_split_026.html#filepos356776)

        3.  [[[The Liskov Substitution Principle (LSP)]{.underline}]{.calibre_10}](#index_split_026.html#filepos361161)

            1.  [[[The ISA Rule]{.underline}]{.calibre_10}](#index_split_026.html#filepos371521)

            2.  [[[Nope!]{.underline}]{.calibre_10}](#index_split_026.html#filepos381625)

            3.  [[[The Representative Rule]{.underline}]{.calibre_10}](#index_split_026.html#filepos383870)

        4.  [[[The Interface Segregation Principle (ISP)]{.underline}]{.calibre_10}](#index_split_026.html#filepos385384)

            1.  [[[Don't Depend on Things You Don't Need]{.underline}]{.calibre_10}](#index_split_026.html#filepos390621)

            2.  [[[Why?]{.underline}]{.calibre_10}](#index_split_026.html#filepos392701)

            3.  [[[Conclusion]{.underline}]{.calibre_10}](#index_split_026.html#filepos394628)

        5.  [[[The Dependency Inversion Principle (DIP)]{.underline}]{.calibre_10}](#index_split_026.html#filepos395094)

            1.  [[[A Blast from the Past]{.underline}]{.calibre_10}](#index_split_026.html#filepos403094)

            2.  [[[A DIP Violation]{.underline}]{.calibre_10}](#index_split_026.html#filepos426585)

            3.  [[[Conclusion]{.underline}]{.calibre_10}](#index_split_026.html#filepos461765)

8.  [[[PART IV Functional Pragmatics]{.underline}]{.calibre_10}](#index_split_027.html#filepos462337)

    1.  [[[Chapter 13 Tests]{.underline}]{.calibre_10}](#index_split_028.html#filepos462575)

        1.  [[[But What about the REPL?]{.underline}]{.calibre_10}](#index_split_028.html#filepos465087)

        2.  [[[What about Mocks?]{.underline}]{.calibre_10}](#index_split_028.html#filepos465557)

        3.  [[[Property-Based Testing]{.underline}]{.calibre_10}](#index_split_028.html#filepos470054)

        4.  [[[A Diagnostic Technique]{.underline}]{.calibre_10}](#index_split_028.html#filepos479009)

        5.  [[[Functional]{.underline}]{.calibre_10}](#index_split_028.html#filepos501217)

    2.  [[[Chapter 14 GUI]{.underline}]{.calibre_10}](#index_split_029.html#filepos501727)

        1.  [[[Turtle-Graphics in Quil]{.underline}]{.calibre_10}](#index_split_029.html#filepos504606)

    3.  [[[Chapter 15 Concurrency]{.underline}]{.calibre_10}](#index_split_030.html#filepos534355)

        1.  [[[Conclusion]{.underline}]{.calibre_10}](#index_split_030.html#filepos557725)

9.  [[[PART V Design Patterns]{.underline}]{.calibre_10}](#index_split_031.html#filepos559550)

    1.  [[[Chapter 16 Design Patterns Review]{.underline}]{.calibre_10}](#index_split_032.html#filepos560846)

        1.  [[[Patterns in Functional Programming]{.underline}]{.calibre_10}](#index_split_032.html#filepos569620)

        2.  [[[Abstract Server]{.underline}]{.calibre_10}](#index_split_032.html#filepos570391)

        3.  [[[Adapter]{.underline}]{.calibre_10}](#index_split_032.html#filepos576970)

            1.  [[[Is That Really an Adapter Object?]{.underline}]{.calibre_10}](#index_split_032.html#filepos587807)

        4.  [[[Command]{.underline}]{.calibre_10}](#index_split_032.html#filepos591904)

            1.  [[[Undo]{.underline}]{.calibre_10}](#index_split_032.html#filepos598182)

        5.  [[[Composite]{.underline}]{.calibre_10}](#index_split_032.html#filepos606990)

            1.  [[[Functional?]{.underline}]{.calibre_10}](#index_split_032.html#filepos617330)

        6.  [[[Decorator]{.underline}]{.calibre_10}](#index_split_032.html#filepos630536)

        7.  [[[Visitor]{.underline}]{.calibre_10}](#index_split_032.html#filepos641681)

            1.  [[[To Close, or to Clojure?]{.underline}]{.calibre_10}](#index_split_032.html#filepos650175)

            2.  [[[The 90-degree Problem]{.underline}]{.calibre_10}](#index_split_032.html#filepos658262)

        8.  [[[Abstract Factory]{.underline}]{.calibre_10}](#index_split_032.html#filepos666748)

            1.  [[[90 Degrees Again]{.underline}]{.calibre_10}](#index_split_032.html#filepos678513)

            2.  [[[Type Safety?]{.underline}]{.calibre_10}](#index_split_032.html#filepos684566)

        9.  [[[Conclusion]{.underline}]{.calibre_10}](#index_split_032.html#filepos686521)

        10. [[[Postscript: OO Poison?]{.underline}]{.calibre_10}](#index_split_032.html#filepos687147)

10. [[[PART VI Case Study]{.underline}]{.calibre_10}](#index_split_033.html#filepos691416)

    1.  [[[Chapter 17 Wa-Tor]{.underline}]{.calibre_10}](#index_split_034.html#filepos691643)

        1.  [[[Scratch That Itch]{.underline}]{.calibre_10}](#index_split_034.html#filepos746439)

        2.  [[[Showers Solve Problems]{.underline}]{.calibre_10}](#index_split_034.html#filepos753792)

        3.  [[[It's Time to Wildly Reproduce]{.underline}]{.calibre_10}](#index_split_034.html#filepos781959)

        4.  [[[What about the Sharks?]{.underline}]{.calibre_10}](#index_split_034.html#filepos788288)

        5.  [[[Conclusion]{.underline}]{.calibre_10}](#index_split_034.html#filepos821029)

11. [[[Afterword]{.underline}]{.calibre_10}](#index_split_035.html#filepos823070)

12. [[[Index]{.underline}]{.calibre_10}](#index_split_036.html#filepos830622)

::: {#index_split_007.html#calibre_pb_7 .mbp_pagebreak}
:::

[]{#index_split_008.html}

[[[Foreword]{.calibre_3}]{.bold}]{.calibre1}

Uncle Bob needs little introduction. A prominent figure in the software development industry, Bob has authored several books on software design and delivery. Some of his works are taught in computer science classrooms around the world.

I was a student in university when I started functional programming. I didn't attend an elite computer science program teaching Scheme and C, but I was hungry for all things computing. Nobody was talking about functional programming then. I saw a wave of programming coming in the future; a future where developers spent more time thinking about the problem they were solving, rather than how to manage it. After reading [Functional Design]{.italic}, I wish I had this book then and now, at every stage in my career, from student to professional.

[Functional Design]{.italic} exudes "classic-on-arrival." It feels like a book written exactly for the professional software developer. Bob touches on the foundations of software engineering and expands upon them, putting into succinct words the things I've experienced for years. He elegantly pulls back the curtain to reveal how functional programming elements make software design simple yet pragmatic. He does so without alienating []{#index_split_008.html#filepos43219}experienced object-oriented programmers coming from languages like C#, C++, or Java.

By introducing a comparative analysis to Java, [Functional Design]{.italic} introduces functional systems design with Clojure, a Lisp dialect. Clojure isn't so pure like Haskell where one must use pure functional programming concepts. Instead, Clojure strongly encourages it, making it a great first functional programming language. [Functional Design]{.italic} carefully points out the few pitfalls Clojure developers find themselves in from time to time. As a Clojure consultant myself, I can attest to this. This book teaches how to keep a language (and developer) out of the way, rather than seeking something that gets out of the way.

Clojure's critics will say that Clojure is unsuitable for any sufficiently large codebase. As you'll learn in the coming chapters, the design principles and patterns apply to Clojure just as they do to Java, C#, or C++. The design principles of SOLID will help you build better software with functional programming. Design patterns have long since been scoffed at by functional programmers, but [Functional Design]{.italic} deconstructs such criticism and shows exactly why developers need them, and how developers can implement them on their own.

I've written extensively online about classic design patterns in Clojure, so I was delighted to find that this book approaches design pattern usage with thoughtful diagrams before showing the reader code. By the time you reach those chapters, you'll already be able to picture the Clojure code just from the diagrams. Then, the code follows. Finally, [Functional Design]{.italic} ties it all together by walking you through an "enterprise" application in Clojure using the design principles and patterns.

---Janet A. Carr, Independent Clojure Consultant

::: {#index_split_008.html#calibre_pb_8 .mbp_pagebreak}
:::

[]{#index_split_009.html}

[[[Preface]{.calibre_3}]{.bold}]{.calibre1}

This is a book for programmers in the trenches who want to learn how to use functional programming languages to get real things done. As such, I will not spend any appreciable time on the more theoretical aspects of functional programming such as Monads, Monoids, Functors, Categories, and so on. Not that these ideas aren't valid, valuable, or relevant; rather, they do not often impact the day-to-day world of the programmer. This is because they have already been "baked into the cake" of the common languages, libraries, and frameworks. If you are interested in functional theory, I recommend the writings of Mark Seemann.

This book is about how---and why---to use functional programming in our day-to-day effort to build real systems for real customers. In the pages that follow, we will be comparing and contrasting the coding structures that are common in object-oriented languages like Java to those that are common in functional languages like Clojure.

I have chosen these two languages in particular because Java is very widely known and used, and Clojure is extraordinarily simple to learn.

[[[A Brief History of Functional and Procedural Programming]{.calibre_3}]{.bold}]{.calibre1}

In 1936, two mathematicians, Alan Turing and Alonzo Church, independently resolved one of David Hilbert's famous challenges: [The Decidability Problem]{.italic}. It is beyond the scope of this introduction to describe this problem in any detail, except to say it had to do with finding a general solution to formulae of integers.[]{#index_split_009.html#filepos47132}[[[[1]{.underline}]{.calibre_10}]{.calibre3}](#index_split_009.html#filepos47318) This is relevant to us because every program in a digital computer is an integer formula.

[[[1]{.underline}]{.calibre_10}](#index_split_009.html#filepos47132). Diophantine equations.

The two men independently proved that no such general solution exists by demonstrating that there were integers that could never be calculated by an integer formula smaller than the integer itself.

Another way to say this is that there are numbers that no computer program can compute. And indeed, that was the approach that Alan Turing took. In his famous 1936 paper,[]{#index_split_009.html#filepos47904}[[[[2]{.underline}]{.calibre_10}]{.calibre3}](#index_split_009.html#filepos48233) Turing invented a digital computer, and then showed that there were numbers that could not be computed---even given infinite time and space.[]{#index_split_009.html#filepos48137}[[[[3]{.underline}]{.calibre_10}]{.calibre3}](#index_split_009.html#filepos48445)

[[[2.]{.underline}]{.calibre_10}](#index_split_009.html#filepos47904) A. M. Turing, "On Computable Numbers, with an Application to the Entscheidungsproblem" (May 1936).

[[[3.]{.underline}]{.calibre_10}](#index_split_009.html#filepos48137) Given infinite time and space, a computer could calculate π or [∊]{.italic} or any other irrational or transcendental number for which a formula exists. What Turing and Church proved is that there were numbers for which no such formula can exist. Such numbers are "uncomputable."

Church, on the other hand, came to the same conclusion through his invention of lambda calculus, a mathematical formalism for manipulating functions. Using manipulations in the logic of his formalism, he was able to prove that there were logical problems that could not be solved.

Turing's invention was the forebear of all modern digital computers. Every digital computer is, for all intents and purposes, a (finite) Turing machine. Every program that has ever executed on a digital computer is, for all intents and purposes, a Turing Machine program.

Church and Turing later collaborated to show that Turing's and Church's approaches were equivalent. That every program in a Turing machine can be represented in lambda calculus, and vice versa.

Functional programming is, for all intents and purposes, programming in lambda calculus.

So these two styles of programming are equivalent in a mathematical sense. Any program can be written using either the procedural (Turing) style or the functional (Church) style. What we are going to examine in this book is not that equivalence, but rather, the ways that using the functional approach affects the structure and design of our programs. We will seek to determine whether those different structures and designs are in any sense superior, or inferior, to those that arise from using the Turing approach.

[[[On Clojure]{.calibre_3}]{.bold}]{.calibre1}

I chose Clojure for this book because learning a new language and a new paradigm is a doubly difficult task. Therefore, I sought to simplify that task by choosing a language that is simple enough to not get in the way of learning functional programming and functional design.

Clojure is semantically rich but syntactically trivial. What that means is that the language itself has a very simple syntax that requires very little effort to learn. The learning curve in Clojure is all on the semantic side. The libraries and idioms require a significant effort to internalize; but the language itself requires almost no effort at all. My hope is that this book will give you a way to learn and appreciate functional programming while not being distracted by the syntax of a new language.

Having said all that, this book is not a Clojure tutorial.[]{#index_split_009.html#filepos51507}[[[[4]{.underline}]{.calibre_10}]{.calibre3}](#index_split_009.html#filepos51996) I will explain some of the basics in the early chapters and use some explanatory footnotes throughout the text, but I will also rely upon you, gentle reader, to do your []{#index_split_009.html#filepos51769}homework and look things up. There are several Web sites that will help. One of my favorites is [[[https://clojure.org/api/cheatsheet]{.underline}]{.calibre_10}](https://clojure.org/api/cheatsheet).

[[[4.]{.underline}]{.calibre_10}](#index_split_009.html#filepos51507) By the end, you will think me a liar.

The test framework I used in this book is [` speclj `{.calibre4}]{.calibre_17}.[]{#index_split_009.html#filepos52277}[[[[5]{.underline}]{.calibre_10}]{.calibre3}](#index_split_009.html#filepos52592) As the chapters progress, you'll see more and more of it. It is very similar to other popular testing frameworks, so as the pages turn, you should not find it difficult to become familiar with its various facilities.

[[[5.]{.underline}]{.calibre_10}](#index_split_009.html#filepos52277)
[[[https://github.com/slagyr/speclj]{.underline}]{.calibre_10}](https://github.com/slagyr/speclj)

[[[On Architecture and Design]{.calibre_3}]{.bold}]{.calibre1}

A primary focus of this book is to describe the principles of design and architecture for systems built in a functional style. Toward that end, I will employ unified modeling language (UML) diagrams and make reference to the SOLID[]{#index_split_009.html#filepos53218}[[[[6]{.underline}]{.calibre_10}]{.calibre3}](#index_split_009.html#filepos53635) principles of software design, [Design Patterns]{.italic},[]{#index_split_009.html#filepos53365}[[[[7]{.underline}]{.calibre_10}]{.calibre3}](#index_split_009.html#filepos53811) and the concepts of [Clean Architecture]{.italic}. Fear not, I will be explaining things as we go along and will cite many external references should you need to look things up.

[[[6]{.underline}]{.calibre_10}](#index_split_009.html#filepos53218). Robert C. Martin, [Clean Architecture]{.italic} (Pearson 2017), p. 57.

[[[7]{.underline}]{.calibre_10}](#index_split_009.html#filepos53365). Erich Gamma, Richard Helm, Ralph Johnson, and John Vlissides, [Design Patterns: Elements of Reusable Object-Oriented Software]{.italic} (Addison-Wesley, 1994).

[[[On Object Orientation]{.calibre_3}]{.bold}]{.calibre1}

Many have expressed the opinion that object-oriented programming and functional programming are incompatible. These pages should prove otherwise. The programs, designs, and architectures that you see here will be an admixture of both functional and object-oriented concepts. It is my experience, and my strongly held opinion, that the two styles are entirely compatible and that good programmers can, and should, apply them together.

[[[On "Functional" ]{.calibre_3}]{.bold}]{.calibre1}

In this text, I will make use of the term [functional]{.italic}. I will define it and expound upon it. As the chapters roll by, I will also take some license with it. There will be examples that, while written in a functional language and in a functional style, will not be [purely]{.italic} functional. In most such cases, I will put quotation marks around the word [functional]{.italic} and use footnotes to point out the license I am taking.

Why take that license? Because this is a book about pragmatics, not theory. I am more interested in extracting the benefits from the functional [style]{.italic} than in strict adherence to an ideal. For example, as we'll see in the first chapter, "functions" that take input from the user are not purely functional. I will, however, make use of such "functions" as appropriate.

The source code for all the examples in all the chapters is in a single GitHub repository named [[[https://github.com/unclebob/FunctionalDesign]{.underline}]{.calibre_10}](https://github.com/unclebob/FunctionalDesign).

Register your copy of [Functional Design: Principles, Patterns, and Practices]{.italic} on the InformIT site for convenient access to updates and/or corrections as they become available. To start the registration process, go to [[[informit.com/functionaldesign]{.underline}]{.calibre_10}](http://informit.com/functionaldesign) and log in or create an account. The product ISBN (9780138176396) will already be populated. Look on the Registered Products tab for an Access Bonus Content link next to this product, and follow that link to access any available bonus materials. If you would like to be notified of exclusive offers on new editions and updates, please check the box to receive email from us.

::: {#index_split_009.html#calibre_pb_9 .mbp_pagebreak}
:::

[]{#index_split_010.html}

[[[Acknowledgments]{.calibre_3}]{.bold}]{.calibre1}

Thank you to the diligent and professional folks at Pearson for helping to guide this book to completion: Julie Phifer, my ever-helpful, ever-supportive publisher of long-standing; and her compatriots, Menka Mehta, Julie Nahil, Audrey Doyle, Maureen Forys, Mark Taber, and a host of others. It has always been a joy to work with you, and I look forward to many future such endeavors.

Thank you to Jennifer Kohnke, who has produced the vast majority of the gorgeous illustrations in my books over the last three decades. Back in 1995, up against a production deadline, Jennifer, Jim Newkirk, and I pulled an all-nighter to get the illustrations for my very first book formatted and organized just the way I wanted.

Thank you to Michael Feathers, who suggested 20 years ago that I investigate functional programming. He was learning Haskell at the time and was enthusiastic about the possibilities. I found his enthusiasm contagious.

Thank you to Mark Seemann (@ploeh) for his consistently insightful works, his keen and devastatingly rational reviews of my works, and also for his moral courage.

Thanks to Stuart Halloway, who wrote the first book I read about Clojure. It was more than a decade and a half ago that I started that adventure, and I have never looked back. Stuart was kind enough to coach me through my very first experiments with functional programming. Also to Stuart, an apology for once, long ago, speaking out of turn.

Thanks to Rich Hickey who debated with me in the early '90s regarding C++ and object-oriented design and then went on to create and masterfully guide the development of Clojure. Rich's insights into software continue to amaze me.

Though I have never met them, I owe a debt of gratitude to Harold Abelson, Gerald Jay Sussman, and Julie Sussman for the book that truly inspired me to pursue functional programming. That book, [The Structure and Interpretation of Computer Programs (SICP)]{.italic}, may be the most consequential of all the books on software that I have read. It is available for free online. Just search for "SICP."

Thank you to Janet Carr for her Foreword. I stumbled onto Janet's work while perusing Twitter one day and found that she had come to many of the same conclusions regarding functional programming and Clojure that I had.

And for writing the Afterword, thank you to Gina Martiny, my lovely daughter and an accomplished chemical and software engineer. More about her in my dedication.

::: {#index_split_010.html#calibre_pb_10 .mbp_pagebreak}
:::

[]{#index_split_011.html}

[[[About the Author]{.calibre_3}]{.bold}]{.calibre1}

![](images/00347.jpg){.calibre_18}

[Robert C. Martin (Uncle Bob)]{.bold} has been a programmer since 1970. He is founder of Uncle Bob Consulting, LLC, and cofounder with his son Micah Martin of The Clean Coders, LLC. Martin has published dozens of articles in various trade journals and is a regular speaker at international conferences and trade shows. He has authored and edited many books, including [Designing Object-Oriented C++ Applications Using the Booch Method, Pattern Languages of Program Design 3, More C++ Gems, Extreme Programming in Practice, Agile Software Development: Principles, Patterns, and Practices, UML for Java Programmers, Clean Code, The Clean Coder, Clean Architecture, Clean Craftsmanship]{.italic}, and [Clean Agile]{.italic}. A leader in the industry of software development, Martin served for three years as editor-in-chief of the [C++ Report]{.italic}, and he served as the first chairman of the Agile Alliance.

::: {#index_split_011.html#calibre_pb_11 .mbp_pagebreak}
:::

[]{#index_split_012.html}

[[I]{.calibre_3}]{.calibre2}

[[Functional Basics]{.calibre_3}]{.calibre2}

::: {#index_split_012.html#calibre_pb_12 .mbp_pagebreak}
:::

[]{#index_split_013.html}

[[[1]{.calibre_3}]{.bold}]{.calibre1}

[[[Immutability]{.calibre_3}]{.bold}]{.calibre1}

![](images/00182.jpg){.calibre_19}

[[[What Is Functional Programming?]{.calibre_3}]{.bold}]{.calibre1}

If you were to ask the average programmer what functional programming is, you might get any of the following answers.

::: calibre_11
 
:::

-   Programming with functions.

-   Functions are "first class" elements.

-   Programming with referential transparency.

-   A programming style based upon lambda calculus.

While these assertions might be true, they are not particularly helpful. I think a better answer is: [Programming without assignment statements]{.italic}.

Perhaps you don't think that definition is much better. Perhaps it even frightens you. After all, what do assignment statements have to do with functions; and how can you possibly program without them?

Good questions. Those are the questions that I intend to answer in this chapter.

Consider the following simple C program:

> > [[`int main(int ac, char** av) {`{.calibre4}\
> > `    while(!done())`{.calibre4}\
> > `        doSomething();`{.calibre4}\
> > `}`{.calibre4}]{.calibre_3}]{.calibre_17}

This program is the core loop of virtually every program ever written. It quite literally says: "Do something until you are done." What's more, this program has no visible assignment statements. Is it functional? And if so, does that mean every program ever written is functional?

Let's actually make this function do something. Let's have it compute the sum of the squares of the first ten integers \[1..10\]:

> > [[`int n=1;`{.calibre4}\
> > `int sum=0;`{.calibre4}\
> > `int done() {`{.calibre4}\
> > `  return n>10;`{.calibre4}\
> > `}`{.calibre4}\
> > \
> > `void doSomething() {`{.calibre4}\
> > `  sum+=n*n;`{.calibre4}\
> > `  ++n;`{.calibre4}\
> > `}`{.calibre4}\
> > \
> > `void sumFirstTenSquares() {`{.calibre4}\
> > `    while(!done())`{.calibre4}\
> > `        doSomething();`{.calibre4}\
> > `}`{.calibre4}]{.calibre_3}]{.calibre_17}

This program is not functional because it uses two assignment statements in the [` doSomething `{.calibre4}]{.calibre_17} function. It's also just plain ugly with those two global variables. Let's improve it:

> > [[`int sumFirstTenSquares() {`{.calibre4}\
> > `  int sum=0;`{.calibre4}\
> > `  int i=1;`{.calibre4}\
> > `loop:`{.calibre4}\
> > `  if (i>10)`{.calibre4}\
> > `    return sum;`{.calibre4}\
> > `  sum+=i*i;`{.calibre4}\
> > `  i++;`{.calibre4}\
> > `  goto loop;`{.calibre4}\
> > `}`{.calibre4}]{.calibre_3}]{.calibre_17}

This is better; the two globals have become local variables. But it's still not functional. Perhaps you are worried about that [` goto `{.calibre4}]{.calibre_17}. It is there for a good reason. Bear with me as you consider this small modification that uses a worker function to convert the local variables into function arguments:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_039.html#filepos956896)

> > [[`int sumFirstTenSquaresHelper(int sum, int i) {`{.calibre4}\
> > `loop:`{.calibre4}\
> > `  if (i>10)`{.calibre4}\
> > `    return sum;`{.calibre4}\
> > `  sum+=i*i;`{.calibre4}\
> > `  i++;`{.calibre4}\
> > `  goto loop;`{.calibre4}\
> > `}`{.calibre4}\
> > \
> > `int sumFirstTenSquares() {`{.calibre4}\
> > `  return sumFirstTenSquaresHelper(0, 1);`{.calibre4}\
> > `}`{.calibre4}]{.calibre_3}]{.calibre_17}

This program is still not functional; but it's an important [milestone]{.italic} that we'll refer to in a moment. But now, with one last change, something magical happens:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_040.html#filepos957042)

> > [[`int sumFirstTenSquaresHelper(int sum, int i) {`{.calibre4}\
> > `  if (i>10)`{.calibre4}\
> > `    return sum;`{.calibre4}\
> > `  return sumFirstTenSquaresHelper(sum+i*i, i+1);`{.calibre4}\
> > `}`{.calibre4}\
> > \
> > `int sumFirstTenSquares() {`{.calibre4}\
> > `  return sumFirstTenSquaresHelper(0, 1);`{.calibre4}\
> > `}`{.calibre4}]{.calibre_3}]{.calibre_17}

All the assignment statements are gone, and this program is functional. It's also recursive. That's no accident. If you want to get rid of assignment statements, you [have]{.italic} to use recursion. Recursion allows you to replace the assignment of local variables with the [initialization]{.italic} of function arguments.

It also burns up a lot of space on the stack. However, there is a little trick we can use to fix that problem.

Notice that the last call to [` sumFirstTenSquaresHelper `{.calibre4}]{.calibre_17} is also the last use of [` sum `{.calibre4}]{.calibre_17} and [` i `{.calibre4}]{.calibre_17} in that function. Holding those two variables on the stack after initializing the two arguments of the recursive call is pointless; they'll never be used. What if, instead of creating a new stack frame for the recursive call, we simply reused the current stack frame by jumping back to the top of the function with a [` goto `{.calibre4}]{.calibre_17}, as we did in the [milestone]{.italic} program?

This cute little trick is called [tail call optimization (TCO)]{.italic} and all functional languages make use of it.[]{#index_split_013.html#filepos68175}[[[[1]{.underline}]{.calibre_10}]{.calibre3}](#index_split_013.html#filepos68271)

[[[1.]{.underline}]{.calibre_10}](#index_split_013.html#filepos68175) In one way or another. The [Java virtual machine (JVM)]{.italic} complicates TCO a bit. C, of course, does not do TCO and so all my recursive examples in C will grow the stack.

Notice TCO effectively turns that last program into the [milestone]{.italic} program. The last three lines of [` sumFirstTenSquaresHelper `{.calibre4}]{.calibre_17} in the [milestone]{.italic} program are, in effect, the recursive function call. Does that mean the [milestone]{.italic} program is functional too? No, it just behaves identically. At the source code level, that program is not functional because it has assignment statements. But if we take one step back and ignore the fact that the local variables changed as opposed to being reinstantiated in a new stack frame, then the program [behaves]{.italic} as a functional program.

As we will discover in the next section, that is not a distinction without a difference. In the meantime, just remember when you use recursion to eliminate assignment statements, you are not necessarily wasting lots of space on the stack. The language you are using is almost certainly using TCO.

[[[The Problem with Assignment]{.calibre_3}]{.bold}]{.calibre1}

First let's define what we mean by [assignment]{.italic}. Assigning a value to a variable [changes]{.italic} the original value of the variable to the newly assigned value. It is the change that makes it assignment.

In C we initialize a variable this way:

> > [[`int x=0;`{.calibre4}]{.calibre_3}]{.calibre_17}

But we assign a variable this way:

> > [[`x=1;`{.calibre4}]{.calibre_3}]{.calibre_17}

In the first case, the variable [` x `{.calibre4}]{.calibre_17} comes into existence with the value [` 0 `{.calibre4}]{.calibre_17}; prior to the initialization, there was no variable [` x `{.calibre4}]{.calibre_17}. In the second case, the value of [` x `{.calibre4}]{.calibre_17} is changed to [` 1 `{.calibre4}]{.calibre_17}. This may not seem significant, but the implications are profound.

In the first case, we do not know if [` x `{.calibre4}]{.calibre_17} is actually a variable. It could be a constant. In the second case, there is no doubt. We are varying [` x `{.calibre4}]{.calibre_17} by assigning it a new value. Thus, we can say that functional programming is programming [without variables]{.italic}. The values in functional programs [do not vary]{.italic}.

Why is this desirable? Consider the following:

> > [[`.`{.calibre4}\
> > `//Block A`{.calibre4}\
> > `.`{.calibre4}\
> > `x=1;`{.calibre4}\
> > `.`{.calibre4}\
> > `//Block B`{.calibre4}\
> > `.`{.calibre4}]{.calibre_3}]{.calibre_17}

The [state of the system]{.italic} during the execution of [` Block A `{.calibre4}]{.calibre_17} is different from the state of the system in [` Block B `{.calibre4}]{.calibre_17}. This means that [` Block A `{.calibre4}]{.calibre_17} must execute [before]{.italic}
[` Block B `{.calibre4}]{.calibre_17}. If the position of the two blocks were swapped, the system would likely not execute correctly.

This is called a [sequential or temporal coupling]{.italic}---a coupling in time; and it is something you are probably quite familiar with. [` Open `{.calibre4}]{.calibre_17} must be called before [` close `{.calibre4}]{.calibre_17}. [` New `{.calibre4}]{.calibre_17} must be called before [` delete `{.calibre4}]{.calibre_17}. [` Malloc `{.calibre4}]{.calibre_17} must be called before [` free `{.calibre4}]{.calibre_17}. The list of pairs[]{#index_split_013.html#filepos72754}[[[[2]{.underline}]{.calibre_10}]{.calibre3}](#index_split_013.html#filepos72924) like this is endless. And in many ways, they are a bane of our existence.

[[[2.]{.underline}]{.calibre_10}](#index_split_013.html#filepos72754) They are like the Sith; always two there are.

How many []{#index_split_013.html#filepos73129}times have you forgotten to close a file, or release a block of memory, or close a graphics context, or release a semaphore? How many times have you debugged a pernicious problem only to find that you can fix it by swapping the position of two function calls?

And then there's garbage collection.

Garbage collection is a horrible[]{#index_split_013.html#filepos73557}[[[[3]{.underline}]{.calibre_10}]{.calibre3}](#index_split_013.html#filepos74036) hack that we have accepted into our languages because we are just so bad at managing temporal couplings. If we were adept at keeping track of allocated memory, we would not depend on some nasty background process to clean up after us. But the sad fact is we are so truly terrible at managing temporal couplings that we celebrate the crutches we build to protect ourselves from them.

[[[3.]{.underline}]{.calibre_10}](#index_split_013.html#filepos73557) And, no, reference counting isn't any better.

And that doesn't take into account multiple threads. When two or more threads are competing for the processor, keeping the temporal couplings in the correct order becomes a much more significant challenge. Those threads may get the order correct 99.99 percent of the time; but every once in a great while they may execute in the wrong order and cause all manner of mayhem. We call those situations [race conditions]{.italic}.

Temporal couplings and race conditions are the natural consequence of programming with variables---of using assignment. Without assignment, there are no temporal couplings and there are no race conditions.[]{#index_split_013.html#filepos74908}[[[[4]{.underline}]{.calibre_10}]{.calibre3}](#index_split_013.html#filepos75186) You cannot have a concurrent update problem if you never update anything. You cannot have an ordering issue within a function if the system state never changes within that function.

[[[4.]{.underline}]{.calibre_10}](#index_split_013.html#filepos74908) We'll see later that this is not entirely correct. As Spock was fond of saying: "There are always possibilities."

But perhaps it's time for a simple example. Here's our nonfunctional algorithm again; this time without the [` goto `{.calibre4}]{.calibre_17}:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_041.html#filepos957188)

> > [[`1: int sumFirstTenSquaresHelper(int sum, int i) {`{.calibre4}\
> > `2:   while (i<=10) {`{.calibre4}\
> > `3:     sum+=i*i;`{.calibre4}\
> > `4:     i++;`{.calibre4}\
> > `5:   }`{.calibre4}\
> > `6:   return sum;`{.calibre4}\
> > `7: }`{.calibre4}]{.calibre_3}]{.calibre_17}

Now let's say you'd like to log the progress of the algorithm with a statement like this:

> > [[`   log("i=%d, sum=%d", i, sum);`{.calibre4}]{.calibre_3}]{.calibre_17}

Where would you put that line? There are three possibilities. If you add the [` log `{.calibre4}]{.calibre_17} statement after line 2 or 4, then the logged data will be correct, and the difference will simply be whether you are logging before or after the computation. If you insert the [` log `{.calibre4}]{.calibre_17} statement after line 3, then the logged data will be incorrect. That is a temporal coupling---an ordering problem.

Now consider our functional solution, with one interesting cosmetic change:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_042.html#filepos957334)

> > [[`int sumFirstTenSquaresHelper(int sum, int i) {`{.calibre4}\
> > `  return (i>10) ? sum : sumFirstTenSquaresHelper(sum+i*i, i+1);`{.calibre4}\
> > `}`{.calibre4}]{.calibre_3}]{.calibre_17}

There is only one place we can put our [` log `{.calibre4}]{.calibre_17} statement, and it will log correct data.

[[[So Why Is It Called Functional?]{.calibre_3}]{.bold}]{.calibre1}

A function is a mathematical object that maps inputs to outputs. Given [y = f(x)]{.italic}, there is a value of [y]{.italic} for every value of [x]{.italic}. Nothing else matters to [f]{.italic}. If you give [x]{.italic} to [f]{.italic}, you will get [y]{.italic} every single time. The state of the system in which [f]{.italic} executes is irrelevant to [f]{.italic}.

Or to say that a different way, there are no temporal couplings with [f]{.italic}. There is no special order in which [f]{.italic} must be invoked. If you call [f]{.italic} with [x]{.italic}, you will get [y]{.italic} no matter what else may have changed.

Functional programs are true functions in this mathematical sense. If you decompose a functional program into many smaller functions, each of those will also be a true function in the same mathematical sense. This is called [referential transparency]{.italic}.

A function is referentially transparent if you can always replace the function call with its value. Let's try that with our functional algorithm for calculating the sum of the squares of the first ten integers:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_043.html#filepos957479)

> > [[`int sumFirstTenSquaresHelper(int sum, int i) {`{.calibre4}\
> > `  return (i>10) ? sum : sumFirstTenSquaresHelper(sum+i*i, i+1);`{.calibre4}\
> > `}`{.calibre4}\
> > \
> > `int sumFirstTenSquares() {`{.calibre4}\
> > `  return sumFirstTenSquaresHelper(0, 1);`{.calibre4}\
> > `}`{.calibre4}]{.calibre_3}]{.calibre_17}

When we replace the first call to [` sumFirstTenSquaresHelper `{.calibre4}]{.calibre_17} with its implementation, it becomes:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_044.html#filepos957625)

> > [[`int sumFirstTenSquares() {`{.calibre4}\
> > `  return (1>10) ? 0 : sumFirstTenSquaresHelper(0+1*1, 1+1);`{.calibre4}\
> > `}`{.calibre4}]{.calibre_3}]{.calibre_17}

When we replace the next function call, it becomes:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_045.html#filepos957770)

> > [[`int sumFirstTenSquares() {`{.calibre4}\
> > `  return`{.calibre4}\
> > `    (1>10) ? 0 :`{.calibre4}\
> > `      (2>10) ? 0+1*1`{.calibre4}\
> > `              : sumFirstTenSquaresHelper((0+1*1)+2*2,`{.calibre4}\
> > `                                         (1+1)+1);`{.calibre4}\
> > `}`{.calibre4}]{.calibre_3}]{.calibre_17}

I think you can see where this is going. Each call to [` sumFirstTenSquaresHelper `{.calibre4}]{.calibre_17} simply gets replaced with its implementation with the arguments properly replaced.

Notice that you cannot do this simple replacement with the nonfunctional version of the program. Oh, you can unwind the loop if you like; but that's not the same as simply replacing each function call with its implementation.

So, functional programs are composed of true mathematical, referentially transparent functions. And that's why this is called functional programming.

[[[No Change of State?]{.calibre_3}]{.bold}]{.calibre1}

If there are no variables in functional programs, then functional programs cannot change state. How can we expect a program to be useful if it cannot change state?

The answer is that functional programs compute a new state from an old state, [without changing the old state]{.italic}. If this sounds confusing, then the following example should clear it up:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_046.html#filepos957916)

> > [[`State system(State s) {`{.calibre4}\
> > `  return isFinal(s) ? s : system(s);`{.calibre4}\
> > `}`{.calibre4}]{.calibre_3}]{.calibre_17}

You can start the [` system `{.calibre4}]{.calibre_17} in some initial [` state `{.calibre4}]{.calibre_17}, and it will successively move the [` system `{.calibre4}]{.calibre_17} from [` state `{.calibre4}]{.calibre_17} to [` state `{.calibre4}]{.calibre_17} until the final [` state `{.calibre4}]{.calibre_17} is reached. The [` system `{.calibre4}]{.calibre_17} does not change a state variable. Instead, at each iteration, a new [` state `{.calibre4}]{.calibre_17} is created from the old [` state `{.calibre4}]{.calibre_17}.

If we turn TCO off and allow the stack to grow with each recursive call, then the stack will contain all the previous states, unchanged. Moreover, the [` system `{.calibre4}]{.calibre_17} functions as a true function in the mathematical sense. If you call [` system `{.calibre4}]{.calibre_17} with [` state1 `{.calibre4}]{.calibre_17}, it will return [` state2 `{.calibre4}]{.calibre_17} every single time.

If you look closely at our functional version of [` sumFirstTenSquares `{.calibre4}]{.calibre_17}, you will see that it uses precisely this approach to the changing of state. There are no variables, and no internal state. Rather, the algorithm moves from the initial state to the final state, one state change at a time.

Of course, our [` system `{.calibre4}]{.calibre_17} function does not appear to be able to respond to any inputs. It simply starts at some initial [` state `{.calibre4}]{.calibre_17} and then runs to completion. But with a simple modification we can create a "functional" program that responds quite nicely to input events:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_047.html#filepos958061)

> > [[`State system(State state, Event event) {`{.calibre4}\
> > `  return done(state) ? state : system(state, getEvent());`{.calibre4}\
> > `}`{.calibre4}]{.calibre_3}]{.calibre_17}

Now, the computed next [` state `{.calibre4}]{.calibre_17} of the [` system `{.calibre4}]{.calibre_17} is a function of the current [` state `{.calibre4}]{.calibre_17} and an incoming [` event `{.calibre4}]{.calibre_17}. And voila! We have created a very traditional finite state machine that can react to events in real time.

Notice the quotes I put around the word [functional]{.italic} above. That is because [` getEvent `{.calibre4}]{.calibre_17} is not referentially transparent. Every time you call it you will get a different result. Thus, you cannot replace the call with its return value. Does this mean that our program is not actually functional?

Strictly speaking, any program that takes input in this manner cannot be purely functional. But this is not a book about purely functional programs. This is a book about functional [programming]{.italic}. The style of the program above is "functional," even if the input is not pure; and it is that style we are interested in here.

So here, for your entertainment, is a simple little real-time finite state machine that is written in C and is "functional." It is the time-honored subway turnstile example. Have fun with it.

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_048.html#filepos958206)

> > [[`#include <stdio.h>`{.calibre4}\
> > \
> > `typedef enum {locked, unlocked, done} State;`{.calibre4}\
> > `typedef enum {coin, pass, quit} Event;`{.calibre4}\
> > \
> > `void lock() {`{.calibre4}\
> > `  printf("Locking.\n");`{.calibre4}\
> > `}`{.calibre4}\
> > \
> > `void unlock() {`{.calibre4}\
> > `  printf("Unlocking.\n");`{.calibre4}\
> > `}`{.calibre4}\
> > \
> > `void thankyou() {`{.calibre4}\
> > `  printf("Thanking.\n");`{.calibre4}\
> > `}`{.calibre4}\
> > \
> > `void alarm() {`{.calibre4}\
> > `  printf("Alarming.\n");`{.calibre4}\
> > `}`{.calibre4}\
> > \
> > `Event getEvent() {`{.calibre4}\
> > `  while (1) {`{.calibre4}\
> > `    int c = getchar();`{.calibre4}\
> > `    switch (c) {`{.calibre4}\
> > `      case 'c': return coin;`{.calibre4}\
> > `      case 'p': return pass;`{.calibre4}\
> > `      case 'q': return quit;`{.calibre4}\
> > `    }`{.calibre4}\
> > `  }`{.calibre4}\
> > `}`{.calibre4}\
> > \
> > `State turnstileFSM(State s, Event e) {`{.calibre4}\
> > `  switch (s) {`{.calibre4}\
> > `    case locked:`{.calibre4}\
> > `    switch (e) {`{.calibre4}\
> > `      case coin:`{.calibre4}\
> > `      unlock();`{.calibre4}\
> > `      return unlocked;`{.calibre4}\
> > \
> > `      case pass:`{.calibre4}\
> > `      alarm();`{.calibre4}\
> > `      return locked;`{.calibre4}\
> > \
> > `      case quit:`{.calibre4}\
> > `      return done;`{.calibre4}\
> > `    }`{.calibre4}\
> > \
> > `    case unlocked:`{.calibre4}\
> > `    switch (e) {`{.calibre4}\
> > `      case coin:`{.calibre4}\
> > `      thankyou();`{.calibre4}\
> > `      return unlocked;`{.calibre4}\
> > \
> > `      case pass:`{.calibre4}\
> > `      lock();`{.calibre4}\
> > `      return locked;`{.calibre4}\
> > \
> > `      case quit:`{.calibre4}\
> > `      return done;`{.calibre4}\
> > `    }`{.calibre4}\
> > `    case done:`{.calibre4}\
> > `    return done;`{.calibre4}\
> > `  }`{.calibre4}\
> > `}`{.calibre4}\
> > \
> > `State turnstileSystem(State s) {`{.calibre4}\
> > `  return (s==done)? 0`{.calibre4}\
> > `                  : turnstileSystem(`{.calibre4}\
> > `                      turnstileFSM(s, getEvent()));`{.calibre4}\
> > `}`{.calibre4}\
> > \
> > `int main(int ac, char** av) {`{.calibre4}\
> > `  turnstileSystem(locked);`{.calibre4}\
> > `  return 0;`{.calibre4}\
> > `}`{.calibre4}]{.calibre_3}]{.calibre_17}

Keep in mind that C does not use TCO, and so the stack will grow until it is exhausted---though that may require quite a few operations in this case.

[[[Immutability]{.calibre_3}]{.bold}]{.calibre1}

What all this means is that functional programs contain no variables. Nothing in a functional program changes state. State changes are passed from one invocation of a recursive function to the next, without altering any of the previous states. If those previous states aren't needed, TCO can []{#index_split_013.html#filepos89440}optimize them away; but in spirit they all still exist, unchanged, somewhere in a past stack frame.

If there are no variables in a functional program, then the values we name are all [constants]{.italic}. Once initialized, those constants never go away and never change. In spirit, the entire history of every one of those constants remains intact, unchanged, and immutable.

::: {#index_split_013.html#calibre_pb_13 .mbp_pagebreak}
:::

[]{#index_split_014.html}

[[[2]{.calibre_3}]{.bold}]{.calibre1}

[[[Persistent Data]{.calibre_3}]{.bold}]{.calibre1}

![](images/00036.jpg){.calibre_24}

So far this has seemed relatively simple. Programs written in the "functional" style are simply programs that have no variables. Rather than reassign values to variables, we use recursion to initialize new function arguments with new values. Simple.

But data elements are seldom as simple as we have so far imagined them to be. So let's take a look at a slightly more complicated problem, [The Sieve of Eratosthenes]{.italic}:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_051.html#filepos958629)

> > [[`package sieve;`{.calibre4}\
> > \
> > `import java.util.ArrayList;`{.calibre4}\
> > `import java.util.Arrays;`{.calibre4}\
> > `import java.util.List;`{.calibre4}\
> > \
> > `public class Sieve {`{.calibre4}\
> > `  boolean[] isComposite;`{.calibre4}\
> > \
> > `  static List<Integer> primesUpTo(int upTo) {`{.calibre4}\
> > `    return (new Sieve(upTo).getPrimes());`{.calibre4}\
> > `  }`{.calibre4}\
> > \
> > `  private Sieve(int upTo) {`{.calibre4}\
> > `    if (upTo<1)`{.calibre4}\
> > `      upTo=1;`{.calibre4}\
> > `    isComposite = new boolean[upTo+1];`{.calibre4}\
> > `    Arrays.fill(isComposite, false);`{.calibre4}\
> > `    isComposite[0]=isComposite[1] = true;`{.calibre4}\
> > `    for (int i=0; i<isComposite.length; i++)`{.calibre4}\
> > `      if (!isComposite[i])`{.calibre4}\
> > `        for (int c=i+i; c<isComposite.length; c+=i)`{.calibre4}\
> > `          isComposite[c] = true;`{.calibre4}\
> > `  }`{.calibre4}\
> > \
> > `  public List<Integer> getPrimes() {`{.calibre4}\
> > `    ArrayList<Integer> primes = new ArrayList<>();`{.calibre4}\
> > `    for (int i=0; i<isComposite.length; i++)`{.calibre4}\
> > `      if (!isComposite[i])`{.calibre4}\
> > `        primes.add(i);`{.calibre4}\
> > `    return primes;`{.calibre4}\
> > `  }`{.calibre4}\
> > `}`{.calibre4}]{.calibre_3}]{.calibre_17}

This cute little Java program computes the prime numbers up to a limit. Notice all the assignment statements. There are variables everywhere, so this program must not be functional.

But then again, look at the static function at the top. [` Sieve.primesUpTo `{.calibre4}]{.calibre_17} is a true mathematical function. Every time you call it with [` n `{.calibre4}]{.calibre_17}, it will return the prime numbers up to [` n `{.calibre4}]{.calibre_17}. So we can cheat and say that despite the fact that the underlying algorithm uses variables, the result of that algorithm is functional.

[[[On Cheating]{.calibre_3}]{.bold}]{.calibre1}

Our computers are, in some sense, finite [Turing machines]{.italic}; they are not based upon lambda calculus. The Church--Turing thesis tells us that Turing machines and lambda calculus are equivalent forms; but that doesn't mean you can easily translate from one to the other. A functional program is a program that [looks like]{.italic} lambda calculus but is implemented in a finite Turing machine. And that implementation requires that we cheat.

The first cheat we saw was TCO. We waved it away with an argument about pragmatics. After all, since we were never going to need all those historical stack frames, why should we keep them? But that's still a cheat. Under the hood, our implementation was changing the values of existing variables. From the Turing machine's point of view, all our supposed constants were actually variables.

We could continue to push that cheat upward. This lovely little [` Sieve `{.calibre4}]{.calibre_17} algorithm runs entirely in the constructor, so it's all initialization! And as we learned, initialization is not assignment. So the fact that this program has variables under the hood is no different from TCO. In the end, the result is still functional.

This is fun! We can keep pushing that cheat upward. We can push it up until it is outside our finite Turing machine of a computer. And then we could say to ourselves: "Every program that runs in this computer is functional because it will always produce the same outputs when given the same inputs. Never mind that the inputs and outputs include every single bit in the computer's memory. Never mind that. Yeah. That's the ticket."

Of course, if we take that view, then there's not much point in studying functional programming, is there? So let's back down from that highest-level cheat and keep pushing the cheats back down until we simply cannot practically escape them.

There is no reasonable escape from TCO. We don't have an infinite stack. We don't want our functional programs uselessly consuming gigabytes of stack space until they crash. So TCO is a practically unavoidable cheat.

[[[Making Copies]{.calibre_3}]{.bold}]{.calibre1}

So, what about that [` Sieve `{.calibre4}]{.calibre_17} algorithm: Can we push the cheating down lower than that? Can we write that algorithm so it does not use any assignment statements?

The problem, of course, is all those [` for `{.calibre4}]{.calibre_17} loops. We need to turn those into recursive functions in order to get rid of the assignment statements. We also need to do something about the two arrays. We can't be changing elements in existing arrays, can we? That would make those arrays variables. So we'll have to make copies of them whenever we need to change an element:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_052.html#filepos958775)

> > [[`package sieve;`{.calibre4}\
> > \
> > `import java.util.ArrayList;`{.calibre4}\
> > `import java.util.Arrays;`{.calibre4}\
> > `import java.util.List;`{.calibre4}\
> > \
> > `public class Sieve {`{.calibre4}\
> > `  static List<Integer> primesUpTo(int upTo) {`{.calibre4}\
> > `    return getPrimes(`{.calibre4}\
> > `      computeSieve(`{.calibre4}\
> > `        makeSieve(Math.max(upTo, 1)),`{.calibre4}\
> > `        0),`{.calibre4}\
> > `      new ArrayList<>(), 0);`{.calibre4}\
> > `  }`{.calibre4}\
> > \
> > `  private static boolean[] makeSieve(int upTo) {`{.calibre4}\
> > `    boolean[] sieve = new boolean[upTo+1];`{.calibre4}\
> > `    Arrays.fill(sieve, false);`{.calibre4}\
> > `    sieve[0] = sieve[1] = true;`{.calibre4}\
> > `    return sieve;`{.calibre4}\
> > `  }`{.calibre4}\
> > \
> > `  private static boolean[] computeSieve(boolean[] sieve, int n) {`{.calibre4}\
> > `    if (n>=sieve.length)`{.calibre4}\
> > `      return sieve;`{.calibre4}\
> > `    else if (!sieve[n])`{.calibre4}\
> > `      return computeSieve(markMultiples(sieve, n, 2), n+1);`{.calibre4}\
> > `    else return computeSieve(sieve, n+1);`{.calibre4}\
> > `  }`{.calibre4}\
> > \
> > `  private static boolean[] markMultiples(boolean[] sieve,`{.calibre4}\
> > `                                         int prime,`{.calibre4}\
> > `                                         int m) {`{.calibre4}\
> > `    int multiple = prime * m;`{.calibre4}\
> > `    if (multiple>=sieve.length)`{.calibre4}\
> > `      return sieve;`{.calibre4}\
> > `    else {`{.calibre4}\
> > `      var markedSieve = Arrays.copyOf(sieve, sieve.length);`{.calibre4}\
> > `      markedSieve[multiple] = true;`{.calibre4}\
> > `      return markMultiples(markedSieve, prime, m+1);`{.calibre4}\
> > `    }`{.calibre4}\
> > `  }`{.calibre4}\
> > \
> > `  public static List<Integer> getPrimes(boolean[] sieve,`{.calibre4}\
> > `                                        List<Integer> primes,`{.calibre4}\
> > `                                        int n) {`{.calibre4}\
> > `    if (n>=sieve.length)`{.calibre4}\
> > `      return primes;`{.calibre4}\
> > `    else if (!sieve[n]) {`{.calibre4}\
> > `      var newPrimes = new ArrayList<>(primes);`{.calibre4}\
> > `      newPrimes.add(n);`{.calibre4}\
> > `      return getPrimes(sieve, newPrimes, n+1);`{.calibre4}\
> > `    } else {`{.calibre4}\
> > `      return getPrimes(sieve, primes, n+1);`{.calibre4}\
> > `    }`{.calibre4}\
> > `  }`{.calibre4}\
> > `}`{.calibre4}]{.calibre_3}]{.calibre_17}
>
> []{#index_split_014.html#filepos99056}

That's not very pretty, is it? It is, however, pretty functional. You might complain about the assignments in [` makeSieve `{.calibre4}]{.calibre_17}, and I agree that's a bit of a cheat, but it looks close enough to an initialization to satisfy me.

So, yes, all the significant assignment operations have been eliminated. All the named entities are constants, and the stack (if not deleted by TCO) contains the history of each invocation of each recursive function.

But at what cost? Every time either of the two arrays is modified, a new array is created in order to prevent the previous one from being changed. The amount of memory used by this algorithm could be enormous. Imagine finding all the primes up to 100,000. How many [` sieve `{.calibre4}]{.calibre_17} arrays would be created? How many [` primes `{.calibre4}]{.calibre_17} arrays?

And what about execution time? Copying all those arrays over and over again must eat up a terrifying number of cycles.

Is that, then, the cost of functional programming? Must we live with such a huge extravagance of memory and time?

[[[Structural Sharing]{.calibre_3}]{.bold}]{.calibre1}

Fortunately, no. It turns out that there are data structures that behave very much like arrays but that also efficiently maintain the history of their past states. These data structures are [n]{.italic}-ary trees. The bigger the [n]{.italic}, the more efficient they are. But for the sake of simplicity, I will choose an [n]{.italic} of 2---binary trees---for the following examples.

Let us say that we wish to represent a simple array of integers from 1 to 8. The binary tree that achieves this is shown in [[[Figure 2.1]{.underline}]{.calibre_10}](#index_split_014.html#filepos101250).

![](images/00185.jpg){#filepos101250 .calibre_25}

[[Figure 2.1.]{.bold}]{.calibre3}[ A binary tree representing an array of integers \[1..8\]]{.calibre3}

If you look at the leaves and ignore the branches, you will see that the leaves form an array. The branches simply provide a way to traverse to each leaf in some ordered way. That order is the index of the array!

To get to the element at index 0 of the array, simply take the leftmost branch of each node. To get to the element at index 1, go left at each node but right at the last node.

I won't belabor this point. I'm sure you all understand binary trees.

Now, let's say we want to append a 42 on the end of this array while preserving the existence of the previous array. The binary tree that achieves this is shown in [[[Figure 2.2]{.underline}]{.calibre_10}](#index_split_014.html#filepos102410).

![](images/00155.jpg){#filepos102410 .calibre_27}

[[Figure 2.2.]{.bold}]{.calibre3}[ A binary tree that represents \[1..8, 42\] but also preserves the original \[1..8\] array]{.calibre3}

Now the tree has [two roots]{.italic}. The root at the top left still represents the array from 1..8. The root at the top right represents the new array with a 42 appended after the 8.

Stop now and think carefully about this. It should be clear that representing linear arrays as trees, in the manner shown, will allow us to represent additions, insertions, and deletions while preserving all previous arrangements, without massive copying of the array.

Oh, there is some copying going on. We may have to copy a leaf node, or some of the branch nodes, depending on what operation we are performing. But the amount of memory and the number of cycles are drastically less than simply maintaining copies of all the past versions of the array.

In the end, every past version of the array will be represented by a new root node connected to a small number of additional branch nodes, allowing the majority of the elements of the array to be shared among all the versions.

Now consider what happens if we use 32-ary trees instead of binary trees. For arrays of a million elements, the tree depth is on the order of four or five branches. Copying five nodes of 32 elements each is [a lot]{.italic} faster and []{#index_split_014.html#filepos104091}requires [a lot]{.italic} less memory than copying a million elements. Indeed, the cost, while not zero, is so small as to be inconsequential for most applications.

So we have a way to represent an indexable linear array that can be versioned over time while preserving all past versions. We call this [persistence]{.italic}.[]{#index_split_014.html#filepos104460}[[[[1]{.underline}]{.calibre_10}]{.calibre3}](#index_split_014.html#filepos104665) A persistent data structure has the ability to undergo change while remembering all past versions of itself.

[[[1.]{.underline}]{.calibre_10}](#index_split_014.html#filepos104460) Not to be confused with the overloaded term used to describe data in offline storage.

But what about higher-level data structures like hash maps, sets, stacks, and queues? How do we make all of them as persistent as our linear indexed array? Of course, all those data structures can be implemented using indexed arrays. Indeed, since the memory of the computer is nothing more than one big indexed linear array, every data structure that you can represent within a computer can also be represented in a persistent array.

And so the problem we confronted at the start of this chapter, the problem of copying, can be set aside. The cost of functional programming, in memory and cycles, need not dissuade us from further study and pursuit of the benefits of functional programming.

And with that problem solved, all future examples will be written in Clojure, a language that intrinsically supports persistent data structures.

::: {#index_split_014.html#calibre_pb_14 .mbp_pagebreak}
:::

[]{#index_split_015.html}

[[[3]{.calibre_3}]{.bold}]{.calibre1}

[[[Recursion and Iteration]{.calibre_3}]{.bold}]{.calibre1}

![](images/00061.jpg){.calibre_28}

In [[[Chapter 1]{.underline}]{.calibre_10}](#index_split_013.html#filepos61201), Immutability, I stated that functional programming makes use of recursion in order to eliminate assignment. In this chapter, we will look at the two different varieties of recursion; one we will call iteration and the other will retain the original name: recursion.

[[[Iteration]{.calibre_3}]{.bold}]{.calibre1}

TCO is the remedy for the infinite stack depth implied by infinite recursive loops. However, TCO is only applicable if the recursive call is the very last thing to be executed within the function. Such functions are often called [tail call functions]{.italic}.

Here is a very traditional implementation of a function to create a list of Fibonacci numbers:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_054.html#filepos959052)

> > [[`(defn fibs-work [n i fs]`{.calibre4}\
> > `  (if (= i n)`{.calibre4}\
> > `    fs`{.calibre4}\
> > `    (fibs-work n (inc i) (conj fs (apply + (take-last 2 fs))))))`{.calibre4}\
> > \
> > `(defn fibs [n]`{.calibre4}\
> > `  (cond`{.calibre4}\
> > `    (< n 1) []`{.calibre4}\
> > `    (= n 1) [1]`{.calibre4}\
> > `    :else (fibs-work n 2 [1 1])))`{.calibre4}]{.calibre_3}]{.calibre_17}

This program is written in Clojure, which is a variant of Lisp. You call this function like this:

> > [[`(fibs 15)`{.calibre4}]{.calibre_3}]{.calibre_17}

And it returns an array of the first 15 Fibonacci numbers:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_055.html#filepos959198)

> > [[`[1 1 2 3 5 8 13 21 34 55 89 144 233 377 610]`{.calibre4}]{.calibre_3}]{.calibre_17}

Many programmers experience eyestrain headaches the first few times they look at Lisp, mostly because the parentheses don't seem to make any sense. So let me give you a very brief tutorial about those parentheses.

[[Very Brief Clojure Tutorial]{.calibre_3}]{.bold}

::: calibre_11
 
:::

1.  This is a typical function call in C, C++, C#, and Java: [` f(x) `{.calibre4}]{.calibre_17};.

2.  Here is the same function in Lisp: [` (f x) `{.calibre4}]{.calibre_17}.

3.  Now you know Lisp. Here ends the tutorial.

That's not much of an exaggeration. The syntax of Lisp is really that simple.

The syntax of Clojure is just a bit more complicated. So let's take the above program apart, one statement at a time.

First there's [` defn `{.calibre4}]{.calibre_17}, which looks like it is being called as a function. Let's go with that for now. The truth is mostly compatible with that view. So the [` defn `{.calibre4}]{.calibre_17} "function" defines a new function from its arguments. The functions being defined are named [` fibs-work `{.calibre4}]{.calibre_17} and [` fibs `{.calibre4}]{.calibre_17}. The square brackets after the function name enclose the names of the arguments of the function.[]{#index_split_015.html#filepos110424}[[[[1]{.underline}]{.calibre_10}]{.calibre3}](#index_split_015.html#filepos110909) So the [` fibs `{.calibre4}]{.calibre_17} function takes a single argument named [` n `{.calibre4}]{.calibre_17}, while the [` fibs-work `{.calibre4}]{.calibre_17} function takes three arguments named [` n `{.calibre4}]{.calibre_17}, [` i `{.calibre4}]{.calibre_17}, and [` fs `{.calibre4}]{.calibre_17}.

[[[1.]{.underline}]{.calibre_10}](#index_split_015.html#filepos110424) Actually, the square brackets are Clojure syntax for a "vector" (an array). In this case, that vector contains the symbols that represent the arguments.

Following the argument list is the body of the function. So the body of the [` fibs `{.calibre4}]{.calibre_17} function is a call to the [` cond `{.calibre4}]{.calibre_17} function. Think of [` cond `{.calibre4}]{.calibre_17} like a switch statement that returns a value. The [` fibs `{.calibre4}]{.calibre_17} function returns the value returned by [` cond `{.calibre4}]{.calibre_17}.

The arguments to [` cond `{.calibre4}]{.calibre_17} are a set of pairs. The first element in each pair is a predicate, and the second is the value that [` cond `{.calibre4}]{.calibre_17} will return if that predicate is [` true `{.calibre4}]{.calibre_17}. The [` cond `{.calibre4}]{.calibre_17} function walks down the list of pairs until it sees a true predicate, and then it returns the corresponding value.

The predicates are just function calls. The [` (< n 1) `{.calibre4}]{.calibre_17} predicate simply calls the [` < `{.calibre4}]{.calibre_17} function with [` n `{.calibre4}]{.calibre_17} and [` 1 `{.calibre4}]{.calibre_17}. It returns [` true `{.calibre4}]{.calibre_17} if [` n `{.calibre4}]{.calibre_17} is less than 1. The [` (= n 1) `{.calibre4}]{.calibre_17} predicate calls the [` = `{.calibre4}]{.calibre_17} function, which returns [` true `{.calibre4}]{.calibre_17} if its arguments are equal. The [` :else `{.calibre4}]{.calibre_17} predicate is considered [` true `{.calibre4}]{.calibre_17}.

The value returned by [` cond `{.calibre4}]{.calibre_17} for the [` (< n 1) `{.calibre4}]{.calibre_17} predicate is [` [] `{.calibre4}]{.calibre_17}, an empty vector. If [` (= n 1) `{.calibre4}]{.calibre_17}, then [` cond `{.calibre4}]{.calibre_17} returns a vector containing 1. Otherwise, [` cond `{.calibre4}]{.calibre_17} returns the value produced by the [` fibs-work `{.calibre4}]{.calibre_17} function.

So, the [` fibs `{.calibre4}]{.calibre_17} function returns [` [] `{.calibre4}]{.calibre_17} if [` n `{.calibre4}]{.calibre_17} is less than 1, [` [1] `{.calibre4}]{.calibre_17} if [` n `{.calibre4}]{.calibre_17} is equal to 1, and [` (fibs-work n 2 [1 1]) `{.calibre4}]{.calibre_17} in every other case.

Got it? Make sure you do. Go back over it until you do.

The [` ))) `{.calibre4}]{.calibre_17} at the end of the [` fibs `{.calibre4}]{.calibre_17} function are just the closing parentheses of the [` defn `{.calibre4}]{.calibre_17}, [` cond `{.calibre4}]{.calibre_17}, and [` fibs-work `{.calibre4}]{.calibre_17} function calls. I could have written [` fibs `{.calibre4}]{.calibre_17} like this:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_056.html#filepos959343)

> > [[`(defn fibs [n]`{.calibre4}\
> > `  (cond`{.calibre4}\
> > `    (< n 1) []`{.calibre4}\
> > `    (= n 1) [1]`{.calibre4}\
> > `    :else (fibs-work n 2 [1 1])`{.calibre4}\
> > `  )`{.calibre4}\
> > `)`{.calibre4}]{.calibre_3}]{.calibre_17}

Perhaps that makes you feel better. Perhaps that relieves the eyestrain headache you felt coming on. And indeed, many new Lisp programmers use this technique to reduce their parentheses anxiety. That's certainly what I did a decade and a half ago when I first started learning Clojure.

After a few years, however, it becomes obvious that there is no reason to put trailing parentheses on their own lines, and the technique simply becomes an annoyance. Trust me. You'll see.

Anyway, that brings us to the heart of the matter, the [` fibs-work `{.calibre4}]{.calibre_17} function. If you have gotten comfortable with the [` fibs `{.calibre4}]{.calibre_17} function, you have probably already worked out most of the details of the [` fibs-work `{.calibre4}]{.calibre_17} function. But let's go through it step by step just to be sure.

First, the arguments: [` [n i fs] `{.calibre4}]{.calibre_17}. The [` n `{.calibre4}]{.calibre_17} argument tells us how many Fibonacci numbers to return. The [` i `{.calibre4}]{.calibre_17} argument is the index of the next Fibonacci number to compute. The [` fs `{.calibre4}]{.calibre_17} argument is the current list of Fibonacci numbers.

The [` if `{.calibre4}]{.calibre_17} function is a lot like the [` cond `{.calibre4}]{.calibre_17} function. Think of [` (if p a b) `{.calibre4}]{.calibre_17} as [` (cond p a :else b) `{.calibre4}]{.calibre_17}. The [` if `{.calibre4}]{.calibre_17} function takes three arguments. It evaluates the first as a predicate. If the predicate is true, it returns the second argument; otherwise, it returns the third.

So, if [` (= i n) `{.calibre4}]{.calibre_17}, then we return [` fs `{.calibre4}]{.calibre_17}. Otherwise... Well, let's walk through that one carefully.

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_057.html#filepos959489)

> > [[`(fibs-work n (inc i) (conj fs (apply + (take-last 2 fs))))`{.calibre4}]{.calibre_3}]{.calibre_17}

This is a recursive call to [` fibs-work `{.calibre4}]{.calibre_17}, passing in [` n `{.calibre4}]{.calibre_17} unchanged, [` i `{.calibre4}]{.calibre_17} incremented by one, and [` fs `{.calibre4}]{.calibre_17} with a new Fibonacci number appended.

It is the [` conj `{.calibre4}]{.calibre_17} function that does the appending. It takes two arguments: a vector and the value to append to that vector. Vectors are a kind of list. We'll talk about them later.

The [` take-last `{.calibre4}]{.calibre_17} function takes two arguments: a number [` n `{.calibre4}]{.calibre_17} and a list. It returns a list containing the last [` n `{.calibre4}]{.calibre_17} elements of the list argument.

The [` apply `{.calibre4}]{.calibre_17} function takes two arguments: a function and a list. It calls the function with the list as its arguments. So, [` (apply + [3 4]) `{.calibre4}]{.calibre_17} is equivalent to [` (+ 3 4) `{.calibre4}]{.calibre_17}.

OK, so now you should have a good working grasp of Clojure. There's more to the language that we'll encounter as we go along. But for now, let's get back to the topic of iteration and recursion.

[[Iteration]{.calibre_3}]{.bold}

Notice the recursive call to [` fibs-work `{.calibre4}]{.calibre_17} is a tail call. The very last thing done by the [` fibs-work `{.calibre4}]{.calibre_17} function is to call itself. Therefore, the language can employ TCO to eliminate previous stack frames and turn the recursive call into a [` goto `{.calibre4}]{.calibre_17}, effectively converting the recursion to pure iteration.

So, then, functions that employ tail calls are, for all intents and purposes, iterative.

[[TCO, Clojure, and the JVM]{.calibre_3}]{.bold}

The [Java virtual machine (JVM)]{.italic} does not make it easy for languages to employ TCO. Indeed, the code I just showed you does not use TCO and therefore grows the stack throughout the iteration. Thus, in Clojure, we [explicitly]{.italic} invoke TCO by using the [` recur `{.calibre4}]{.calibre_17} function as follows:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_058.html#filepos959634)

> > [[`(defn fibs-work [n i fs]`{.calibre4}\
> > `  (if (= i n)`{.calibre4}\
> > `    fs`{.calibre4}\
> > `    (recur n (inc i) (conj fs (apply + (take-last 2 fs))))))`{.calibre4}]{.calibre_3}]{.calibre_17}

The [` recur `{.calibre4}]{.calibre_17} function can only be called from a tail position, and it effectively reinvokes the enclosing function without growing the stack.

[[[Recursion]{.calibre_3}]{.bold}]{.calibre1}

There is a much more natural and elegant way to write the Fibonacci algorithm using true recursion:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_059.html#filepos959779)

> > [[`(defn fib [n]`{.calibre4}\
> > `  (cond`{.calibre4}\
> > `    (< n 1) nil`{.calibre4}\
> > `    (<= n 2) 1`{.calibre4}\
> > `    :else (+ (fib (dec n)) (fib (- n 2)))))`{.calibre4}\
> > \
> > `(defn fibs [n]`{.calibre4}\
> > `  (map fib (range 1 (inc n))))`{.calibre4}]{.calibre_3}]{.calibre_17}
>
> []{#index_split_015.html#filepos121785}

The [` fib `{.calibre4}]{.calibre_17} function should be self-explanatory by now. After all, [fib(n)]{.italic} is just [fib(n−1) + fib(n−2)]{.italic}. Notice, however, the calls to [` fib `{.calibre4}]{.calibre_17} are not on the tail of the function. The last thing executed by the [` :else `{.calibre4}]{.calibre_17} clause is the [` + `{.calibre4}]{.calibre_17} function. This means we cannot use the [` recur `{.calibre4}]{.calibre_17} function and that TCO is not possible. This also means that the stack will grow as the algorithm proceeds.

The [` range `{.calibre4}]{.calibre_17} function takes two arguments, [a]{.italic} and [b]{.italic}, and returns a list of all the integers from [a]{.italic} to [b−1]{.italic}. The [` map `{.calibre4}]{.calibre_17} function takes two arguments, [f]{.italic} and [l]{.italic}. The [f]{.italic} argument must be a function and the [l]{.italic} argument must be a list. It calls [f]{.italic} with each member of [l]{.italic} and returns a list containing the results.

This version of [` fib `{.calibre4}]{.calibre_17} is extraordinarily inefficient. Consider this execution profile:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_060.html#filepos959925)

> > [[`fib 20 = 6765`{.calibre4}\
> > `"Elapsed time: 1.459277 msecs"`{.calibre4}\
> > `fib 25 = 75025`{.calibre4}\
> > `"Elapsed time: 11.735279 msecs"`{.calibre4}\
> > `fib 30 = 832040`{.calibre4}\
> > `"Elapsed time: 106.490355 msecs"`{.calibre4}\
> > `fib 34 = 5702887`{.calibre4}\
> > `"Elapsed time: 735.689834 msecs"`{.calibre4}]{.calibre_3}]{.calibre_17}

I didn't bother to analyze the algorithm. But a quick curve fit suggests that the algorithm is [` O(n `{.calibre4}]{.calibre_17}[3]{.calibre3}[` ) `{.calibre4}]{.calibre_17}. So, as elegant as the implementation appears, it will never do.

We can vastly improve the performance by using iteration as follows:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_061.html#filepos960071)

> > [[`(defn ifib`{.calibre4}\
> > `  ([n a b]`{.calibre4}\
> > `   (if (= 0 n)`{.calibre4}\
> > `     b`{.calibre4}\
> > `     (recur (dec n) b (+ a b))))`{.calibre4}\
> > \
> > `  ([n]`{.calibre4}\
> > `   (cond`{.calibre4}\
> > `     (< n 1) nil`{.calibre4}\
> > `     (<= n 2) 1`{.calibre4}\
> > `     :else (ifib (- n 2) 1 1)))`{.calibre4}\
> > `  )`{.calibre4}]{.calibre_3}]{.calibre_17}
>
> []{#index_split_015.html#filepos124752}

The [` ifib `{.calibre4}]{.calibre_17} function has two overloads: [` [n a b] `{.calibre4}]{.calibre_17} and [` [n] `{.calibre4}]{.calibre_17}. Since it is iterative, it does not grow the stack, and it is also much faster than the previous recursive version. Indeed, I believe most of that time was spent in printing rather than true computation.

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_015.html#filepos126390)

> > [[`ifib 20 = 6765`{.calibre4}\
> > `"Elapsed time: 0.185508 msecs"`{.calibre4}\
> > `ifib 25 = 75025`{.calibre4}\
> > `"Elapsed time: 0.177111 msecs"`{.calibre4}\
> > `ifib 30 = 832040`{.calibre4}\
> > `"Elapsed time: 0.14596 msecs"`{.calibre4}\
> > `ifib 34 = 5702887`{.calibre4}\
> > `"Elapsed time: 0.148221 msecs"`{.calibre4}]{.calibre_3}]{.calibre_17}

Of course, we've lost a lot of the expressive power of the recursive algorithm. We can reclaim that by remembering [referential transparency]{.italic}: In a functional language, functions always return the same values given the same inputs. Thus, it is never necessary to reevaluate a function. Once we have computed the value of [` (fib 20) `{.calibre4}]{.calibre_17}, we can remember it instead of recomputing it.

We do this by using the [` memoize `{.calibre4}]{.calibre_17} function as follows:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_063.html#filepos960363)

> > [[`(declare fib)`{.calibre4}\
> > \
> > `(defn fib-w [n]`{.calibre4}\
> > `  (cond`{.calibre4}\
> > `    (< n 1) nil`{.calibre4}\
> > `    (<= n 2) 1`{.calibre4}\
> > `    :else (+ (fib (dec n)) (fib (- n 2)))))`{.calibre4}\
> > \
> > `(def fib (memoize fib-w))`{.calibre4}]{.calibre_3}]{.calibre_17}
>
> []{#index_split_015.html#filepos126924}

The [` declare `{.calibre4}]{.calibre_17} function creates an unbound symbol, which can be used by other functions so long as it is bound before its use. I used [` declare `{.calibre4}]{.calibre_17} in this case because the definition of [` fib `{.calibre4}]{.calibre_17} comes after [` fib-w `{.calibre4}]{.calibre_17}, and Clojure wants all names declared or defined before they are used.

The [` memoize `{.calibre4}]{.calibre_17} function takes an argument [f]{.italic}, which must be a function, and returns a new function [g]{.italic}. Calls to [g]{.italic} with argument [x]{.italic} will call [f]{.italic} with [x]{.italic} if, and only if, [g]{.italic} has never been called with [x]{.italic} before. It then remembers those arguments and the return value. Any subsequent call to [g]{.italic} with [x]{.italic} will return the remembered value.

This version of the algorithm is just as fast as the iterative version because we have short-circuited the vast majority of the recursion without sacrificing the elegance of the algorithm. We pay for that with a little extra memory, but that seems a small price to pay.

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_064.html#filepos960509)

> > [[`fib 20 = 6765`{.calibre4}\
> > `"Elapsed time: 0.168678 msecs"`{.calibre4}\
> > `fib 25 = 75025`{.calibre4}\
> > `"Elapsed time: 0.16232 msecs"`{.calibre4}\
> > `fib 30 = 832040`{.calibre4}\
> > `"Elapsed time: 0.151619 msecs"`{.calibre4}\
> > `fib 34 = 5702887`{.calibre4}\
> > `"Elapsed time: 0.15134 msecs"`{.calibre4}]{.calibre_3}]{.calibre_17}

What we have learned here is that iteration and recursion are very different approaches. Iterative functions must use tail calls to drive the iteration and should use TCO to prevent the growth of the stack. Recursive functions do not use tail calls and therefore will grow the stack. Truly recursive functions can be quite elegant, and memoization can be used to prevent that elegance from significantly affecting performance.

Although Clojure was used as the language in this chapter, the concepts are the same in virtually every other functional language, and could even be implemented in nonfunctional languages, though with a substantial loss of elegance. ;-)

::: {#index_split_015.html#calibre_pb_15 .mbp_pagebreak}
:::

[]{#index_split_016.html}

[[[4]{.calibre_3}]{.bold}]{.calibre1}

[[[Laziness]{.calibre_3}]{.bold}]{.calibre1}

![](images/00073.jpg){.calibre_29}

Consider the following boldfaced change to our program that calculates a list of Fibonacci numbers:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_065.html#filepos960640)

> > [[`(declare fib)`{.calibre4}\
> > \
> > `(defn fib-w [n]`{.calibre4}\
> > `  (cond`{.calibre4}\
> > `    (< n 1) nil`{.calibre4}\
> > `    (<= n 2) 1`{.calibre4}\
> > `    :else (+ (fib (dec n)) (fib (- n 2)))))`{.calibre4}\
> > \
> > `(def fib (memoize fib-w))`{.calibre4}\
> > \
> > \
> > ]{.calibre_3}]{.calibre_17}[[`(defn lazy-fibs []`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `  `{.calibre4}]{.calibre_3}]{.calibre_17}[[`(map fib (rest (range)))`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `  )`{.calibre4}]{.calibre_3}]{.calibre_17}

The [` lazy-fibs `{.calibre4}]{.calibre_17} function may look a little strange to you. Let's walk through it. You already understand the [` map `{.calibre4}]{.calibre_17} function. The [` rest `{.calibre4}]{.calibre_17} function takes a list and returns that list without the first element. And that brings us to the [` range `{.calibre4}]{.calibre_17} function.

The [` range `{.calibre4}]{.calibre_17} function, as called here, returns a list of integers starting at zero. How many integers, you ask? As many as you need. The [` range `{.calibre4}]{.calibre_17} function is [lazy]{.italic}. Or, rather, the range function returns a [lazy]{.italic} list.

What is a lazy list? A lazy list is an object that knows how to compute its next value. In Java, C++, and C#, we called such objects [iterators]{.italic}. A lazy list is an iterator masquerading as a list.

Clojure is friends with lazy lists. Most of the library functions return lazy lists if possible. So, in the above program, [` rest `{.calibre4}]{.calibre_17} and [` map `{.calibre4}]{.calibre_17} both return a lazy list. And that means [` lazy-fibs `{.calibre4}]{.calibre_17} also returns a lazy list.

How would you use [` lazy-fibs `{.calibre4}]{.calibre_17}? Like so:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_066.html#filepos960786)

> > [[`(take 10 (lazy-fibs))`{.calibre4}\
> > `returns: (1 1 2 3 5 8 13 21 34 55)`{.calibre4}]{.calibre_3}]{.calibre_17}

The [` take `{.calibre4}]{.calibre_17} function takes two arguments: a number [` n `{.calibre4}]{.calibre_17} and a list. It returns a list that contains the first [` n `{.calibre4}]{.calibre_17} elements of the argument list. Actually, that's not quite right, but I'll get to that in a minute.

So, now let's walk through [` lazy-fibs `{.calibre4}]{.calibre_17} again. The [` range `{.calibre4}]{.calibre_17} function returns a lazy list of integers starting at zero. The [` rest `{.calibre4}]{.calibre_17} function takes that list, drops the first element, and then returns a lazy list of the remaining integers, which in this instance, are the integers starting at one. The [` map `{.calibre4}]{.calibre_17} function applies each of those integers to the [` fib `{.calibre4}]{.calibre_17} function returning a lazy list of the Fibonacci numbers starting at [` (fib 1) `{.calibre4}]{.calibre_17}.

You can have as many Fibonacci numbers as you like, so long as there are no overflows or other machine limitations. So, for example:

> > [[`(nth (lazy-fibs) 50)`{.calibre4}\
> > `returns: 20365011074`{.calibre4}]{.calibre_3}]{.calibre_17}

The [` nth `{.calibre4}]{.calibre_17} function takes a list and an integer [` n `{.calibre4}]{.calibre_17} and returns the [` n `{.calibre4}]{.calibre_17}th element of the list. So this returns the 50th Fibonacci number.

Now consider this:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_067.html#filepos960931)

> > [[`(def list-of-fibs (lazy-fibs))`{.calibre4}]{.calibre_3}]{.calibre_17}

The [` def `{.calibre4}]{.calibre_17} function (it's not really a function, but pretend that it is) creates a new symbol and associates it with a value. So the symbol [` list-of-fibs `{.calibre4}]{.calibre_17} refers to a lazy list of Fibonacci numbers, as you can see from the following:

> > [[`(take 5 list-of-fibs)`{.calibre4}\
> > `returns: (1 1 2 3 5)`{.calibre4}]{.calibre_3}]{.calibre_17}

Now note: When we executed the [` def `{.calibre4}]{.calibre_17} that created [` list-of-fibs `{.calibre4}]{.calibre_17}, no Fibonacci numbers were calculated, and no memory was allocated []{#index_split_016.html#filepos135902}for Fibonacci numbers. The calculations only take place, and the memory is only allocated, as the elements of the list are accessed. Remember, behind the scenes, the lazy lists are really just iterators that know how to calculate their next element. Once that calculation takes place, the memory is allocated and the value is placed into a real list.[]{#index_split_016.html#filepos136259}[[[[1]{.underline}]{.calibre_10}]{.calibre3}](#index_split_016.html#filepos136355)

[[[1]{.underline}]{.calibre_10}](#index_split_016.html#filepos136259). That's a convenient way to think of it for now. Actually, as we'll see shortly, the memory is only allocated and the list only grows, if the program needs to hold those values.

It is tempting to think of lazy lists as being infinite. Of course they are not. They are simply unbounded. You can walk through as many items as you like, but that number will always be finite.

[[[Lazy Accumulation]{.calibre_3}]{.bold}]{.calibre1}

It should be clear that if you continue to pass lazy lists through functions like [` map `{.calibre4}]{.calibre_17}, [` rest `{.calibre4}]{.calibre_17}, and [` take `{.calibre4}]{.calibre_17} (yes, [` take `{.calibre4}]{.calibre_17} actually returns a lazy list), you will accumulate a long chain of iterators behind the scenes. Each of those iterators must hold on to the function that calculates its next value. It must also hold on to all the data required for that calculation.

I have written applications that have lists with thousands of elements, each of which holds on to other lists with thousands of other elements; and all these lists are lazy. Now remember, we are [deferring]{.italic} calculations. None of the calculations take place until the final results are accessed. So a huge backlog of deferred iterators can get chained through all those lists.

This works fine until you run out of the memory allocated for holding all those deferred iterators. So, from time to time, it might be a good idea to convert your lazy lists into real lists. In Clojure, we do that with the [` doall `{.calibre4}]{.calibre_17} function:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_068.html#filepos961076)

> > [[`(def real-list-of-fibs (doall (take 50 (lazy-fibs))))`{.calibre4}]{.calibre_3}]{.calibre_17}

The [` doall `{.calibre4}]{.calibre_17} function makes [` real-list-of-fibs `{.calibre4}]{.calibre_17} a real list that occupies memory and contains no deferred iterators. All calculations have been done.

[[[OK, but Why?]{.calibre_3}]{.bold}]{.calibre1}

Good question! Laziness is not free. It requires memory and cycles to defer calculations. Then there's the problem of accumulation that can lead to memory exhaustion.

Yet despite these costs, laziness is a common---if not universal---feature in functional languages. Some languages, like Haskell, are intrinsically lazy. Clojure is not intrinsically lazy, but so many of the library functions are lazy that you cannot easily avoid the laziness. F# and Scala allow laziness, but you must be explicit about it.

Why? Why do all these languages accept the costs of laziness?

Because laziness decouples [what]{.italic} you need to do from [how much]{.italic} you need to do. You can write a program that creates a lazy sequence without knowing how big a sequence your users are going to want. Your users can determine how much of your sequence they need.

So, for example:

> > [[`(nth (lazy-fibs) 500)`{.calibre4}]{.calibre_3}]{.calibre_17}

returns [` 22559151616193633087251269503607207204601132491375819058863 `{.calibre4}]{.calibre_17}➥[` 8866418474627738686883405015987052796968498626N `{.calibre4}]{.calibre_17}

Since [` lazy-fibs `{.calibre4}]{.calibre_17} puts no limit on the number of Fibonacci numbers it creates, you can ask for as many as you like.

Or, consider this example. I could create a list of 51 integers like this:

> > [[`(range 51)`{.calibre4}]{.calibre_3}]{.calibre_17}

Or like this:

> > [[`(take 51 (range))`{.calibre4}]{.calibre_3}]{.calibre_17}

Notice in the first example, the [` 51 `{.calibre4}]{.calibre_17} is far more coupled than in the second. In the first, I have to get that [` 51 `{.calibre4}]{.calibre_17} into the [` range `{.calibre4}]{.calibre_17} function somehow. I might be able to pass it as an argument, but that's a pretty strong coupling. In the second example, the [` range `{.calibre4}]{.calibre_17} function doesn't care at all. That [` 51 `{.calibre4}]{.calibre_17} could be way out in some other part of the code, far removed from the call to [` range `{.calibre4}]{.calibre_17}.

By the way, you might be interested to know that in the [` lazy-fibs `{.calibre4}]{.calibre_17} example above, [` (fib 1) `{.calibre4}]{.calibre_17} through [` (fib 499) `{.calibre4}]{.calibre_17} have likely been garbage-collected. Since I'm not holding on to the list itself, the runtime system is free to dispose of the previously calculated elements. Thus, it would be possible to create and traverse a lazy list with trillions of elements and yet never hold more than one[]{#index_split_016.html#filepos142551}[[[[2]{.underline}]{.calibre_10}]{.calibre3}](#index_split_016.html#filepos142676) of them in memory at a time.

[[[2]{.underline}]{.calibre_10}](#index_split_016.html#filepos142551). Or at least some [` n `{.calibre4}]{.calibre_17}, where n is small and is the "chunk" size of the lazy engine.

[[[Coda]{.calibre_3}]{.bold}]{.calibre1}

There is much more to learn about laziness. My purpose here has been to make you aware of it because it is so common in functional languages. We will be seeing much more of it in the pages to come, but it will almost always be in the background.

::: {#index_split_016.html#calibre_pb_16 .mbp_pagebreak}
:::

[]{#index_split_017.html}

[[[5]{.calibre_3}]{.bold}]{.calibre1}

[[[Statefulness]{.calibre_3}]{.bold}]{.calibre1}

![](images/00127.jpg){.calibre_30}

In the end, every program ever written is just a form of [y = f(x)]{.italic}, where [x]{.italic} is all the input you give to the program and [y]{.italic} is all the output it delivers in response.

This definition is sufficient for all batch jobs. For example, in a payroll system, the input [x]{.italic} is all the employee records and timecards and the output [y]{.italic} is all the paychecks and reports.

But perhaps this batch definition is too simplistic. After all, in interactive applications, the input you give to the program is often based on the output it just gave you. So perhaps we should think of interactive software systems as:

> > [[`void p(Input x) {`{.calibre4}\
> > `  while (x != DONE)`{.calibre4}\
> > `    x = (getInput(f(x))`{.calibre4}\
> > `}`{.calibre4}]{.calibre_3}]{.calibre_17}

In other words, our program is a loop that computes [y = f(x)]{.italic} and then hands [y]{.italic} to some source of input that is passed back into [f]{.italic} until [f]{.italic} finally returns [` DONE `{.calibre4}]{.calibre_17}.

In some very real sense, the state of this program during each iteration is [x]{.italic}. If you were debugging some malfunction, you would want to know the value of [x]{.italic} and would likely call [x]{.italic} the state of the system.

And indeed, in the program above, there is a variable named [` x `{.calibre4}]{.calibre_17} that holds the state of the system and is updated upon each iteration.

However, we can eliminate that variable by writing the program "functionally" as follows:

> > [[`void p(Input x) {`{.calibre4}\
> > `  if (x!=DONE)`{.calibre4}\
> > `    p(getInput(f(x)));`{.calibre4}\
> > `}`{.calibre4}]{.calibre_3}]{.calibre_17}

Now this program has no variable that is updated to hold the state of the system. Instead, that state is passed as an argument from one invocation of [` p `{.calibre4}]{.calibre_17} to the next.

A few years ago I wrote a functional program in Clojure that looked very much like this. It was a version of the old computer game [Spacewar!]{.italic}. You can see (and play) this program at [[[https://github.com/unclebob/spacewar]{.underline}]{.calibre_10}](https://github.com/unclebob/spacewar). The game is visual and interactive, and it is written in the "functional" style.

The internal state of the [` spacewar `{.calibre4}]{.calibre_17} program is enormously complex. It consists of the [Enterprise]{.italic}, dozens of Klingons, hundreds of stars, many dozens of torpedoes, phaser blasts, kinetic projectiles, bases, transports, and a plethora of other entities and attributes. All that complexity is maintained within a single object that I called [` world `{.calibre4}]{.calibre_17}. And the flow of [` spacewar `{.calibre4}]{.calibre_17} is, for all intents and purposes:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_069.html#filepos961206)

> > [[`(defn spacewar [world]`{.calibre4}\
> > `  (when (:done? world)`{.calibre4}\
> > `    (System/exit 0))`{.calibre4}\
> > `  (recur (update-world world (get-input world))))`{.calibre4}]{.calibre_3}]{.calibre_17}

In other words, the [` spacewar `{.calibre4}]{.calibre_17} program is a loop that exits if the :[` done? `{.calibre4}]{.calibre_17}[]{#index_split_017.html#filepos147755}[[[[1]{.underline}]{.calibre_10}]{.calibre3}](#index_split_017.html#filepos148153) attribute of the [` world `{.calibre4}]{.calibre_17} is [` true `{.calibre4}]{.calibre_17}, and otherwise presents the [` world `{.calibre4}]{.calibre_17} to the user and gets input that it uses to update the [` world `{.calibre4}]{.calibre_17}.

[[[1]{.underline}]{.calibre_10}](#index_split_017.html#filepos147755). Keywords in Clojure are prefixed with colons. So [` :done? `{.calibre4}]{.calibre_17} is a keyword, which is just a constant that can be used as an identifier. Often, they are used as keys into hash maps. When used as a function, a keyword behaves like an accessor into a hash map. Thus, [` (:done? world) `{.calibre4}]{.calibre_17} simply returns the [` :done? `{.calibre4}]{.calibre_17} element of the [` world `{.calibre4}]{.calibre_17} hash map.

Here is the actual [` update-world `{.calibre4}]{.calibre_17} function as it currently exists within [` spacewar `{.calibre4}]{.calibre_17}:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_070.html#filepos961351)

> > [[`(defn update-world [ms world]`{.calibre4}\
> > `  ;{:pre [(valid-world? world)]`{.calibre4}\
> > `  ; :post [(valid-world? %)]}`{.calibre4}\
> > `  (->> world`{.calibre4}\
> > `       (game-won ms)`{.calibre4}\
> > `       (game-over ms)`{.calibre4}\
> > `       (ship/update-ship ms)`{.calibre4}\
> > `       (shots/update-shots ms)`{.calibre4}\
> > `       (explosions/update-explosions ms)`{.calibre4}\
> > `       (clouds/update-clouds ms)`{.calibre4}\
> > `       (klingons/update-klingons ms)`{.calibre4}\
> > `       (bases/update-bases ms)`{.calibre4}\
> > `       (romulans/update-romulans ms)`{.calibre4}\
> > `       (view-frame/update-messages ms)`{.calibre4}\
> > `       (add-messages)`{.calibre4}\
> > `       ))`{.calibre4}]{.calibre_3}]{.calibre_17}
>
> []{#index_split_017.html#filepos149963}

The threading macro ([` ->> `{.calibre4}]{.calibre_17}) simply passes the argument [` world `{.calibre4}]{.calibre_17} into [` game-won `{.calibre4}]{.calibre_17}, the output of which gets passed to [` game-over `{.calibre4}]{.calibre_17}, the output of which gets passed to [` ship/update-ship `{.calibre4}]{.calibre_17}, and so on. Each of those functions returns an updated version of the [` world `{.calibre4}]{.calibre_17}.

Note the [` ms `{.calibre4}]{.calibre_17} argument. It contains the number of milliseconds since the last update and is the primary input to the game as a whole. As an object moves across the screen, its position is updated based upon its velocity vector and the number of milliseconds that have transpired since its position was last updated.

I'm showing this to you to give you a glimpse of the complexity being managed by this program. Keep in mind that the [` world `{.calibre4}]{.calibre_17} is not a mutable variable. Each of those threaded functions into which the [` world `{.calibre4}]{.calibre_17} is being passed is returning a new version of the [` world `{.calibre4}]{.calibre_17} and passing it to the next. It is not being held in a variable and being mutated.

Let me give you one more glimpse of the complexity:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_071.html#filepos961497)

> > [[`(s/def ::ship (s/keys :req-un`{.calibre4}\
> > `                      [::x ::y ::warp ::warp-charge`{.calibre4}\
> > `                       ::impulse ::heading ::velocity`{.calibre4}\
> > `                       ::selected-view ::selected-weapon`{.calibre4}\
> > `                       ::selected-engine ::target-bearing`{.calibre4}\
> > `                       ::engine-power-setting`{.calibre4}\
> > `                       ::weapon-number-setting`{.calibre4}\
> > `                       ::weapon-spread-setting`{.calibre4}\
> > `                       ::heading-setting`{.calibre4}\
> > `                       ::antimatter ::core-temp`{.calibre4}\
> > `                       ::dilithium ::shields`{.calibre4}\
> > `                       ::kinetics ::torpedos`{.calibre4}\
> > \
> > `                       ::life-support-damage ::hull-damage`{.calibre4}\
> > `                       ::sensor-damage ::impulse-damage`{.calibre4}\
> > `                       ::warp-damage ::weapons-damage`{.calibre4}\
> > `                       ::strat-scale`{.calibre4}\
> > `                       ::destroyed`{.calibre4}\
> > `                       ::corbomite-device-installed]))`{.calibre4}]{.calibre_3}]{.calibre_17}
>
> []{#index_split_017.html#filepos153273}

What you are looking at is a small portion of the type specification of the [Enterprise]{.italic}, the player's ship. Clojure provides a mechanism called [` clojure.spec `{.calibre4}]{.calibre_17} that give us the ability to very specifically design our data structures with even more precision and control than most statically typed languages.

All this complexity of state is managed within the [` spacewar `{.calibre4}]{.calibre_17} program by passing the [` world `{.calibre4}]{.calibre_17} from function to function to function, and then recursively passing it back to [` spacewar `{.calibre4}]{.calibre_17}. The [` world `{.calibre4}]{.calibre_17} is never held in a variable.

And, the game operates on a large screen at 30 frames per second.

The bottom line here is that there is no level of complexity that demands that we abandon immutability and deviate from the functional style. On the other hand, there are other factors that do, from time to time, make that demand.

[[[When We MUST Mutate]{.calibre_3}]{.bold}]{.calibre1}

The [` spacewar `{.calibre4}]{.calibre_17} program uses a graphical user interface (GUI) framework called [Quil]{.italic}.[]{#index_split_017.html#filepos154816}[[[[2]{.underline}]{.calibre_10}]{.calibre3}](#index_split_017.html#filepos155132) This framework allows the programs that use it to be written in a "functional" style. It may not actually be functional in its internals, but from the outside looking in, there need not be any visible mutable state.

[[[2]{.underline}]{.calibre_10}](#index_split_017.html#filepos154816). See [[[www.quil.info]{.underline}]{.calibre_10}](http://www.quil.info). Quil uses [Processing]{.italic} behind the scenes. [Processing]{.italic} is a Java framework that is certainly not functional. Quil pretends to be functional by hiding the mutable variables, or at least by not forcing you to mutate those variables.

On the other hand, I am currently writing an application in Clojure named [` more-speech `{.calibre4}]{.calibre_17}[]{#index_split_017.html#filepos155742}[[[[3]{.underline}]{.calibre_10}]{.calibre3}](#index_split_017.html#filepos156014) that uses Java's Swing framework. Swing [is not functional]{.italic}. Mutable state drips from every appendage of the framework. It is a definitionally mutable object framework.

[[[3]{.underline}]{.calibre_10}](#index_split_017.html#filepos155742). [[[https://github.com/unclebob/more-speech]{.underline}]{.calibre_10}](https://github.com/unclebob/more-speech)

This makes it a challenge to use with Clojure and maintain a "functional" style. To make matters worse, Swing uses a model-view approach, and the models are defined and controlled by Swing. So building an immutable model is virtually impossible.

Swing is not the only framework that forces you into the mutable world. There are many others. So, even if you are determined to use the "functional" style, you must be able to deal with the fact that a large panoply of existing software frameworks will force you out of that style.

Worse, many such frameworks also force you into the multithreaded world. Swing, for example, runs in its own special thread. Programmers should not use that thread for regular processing but must specifically enter that thread when mutating Swing data structures.

This puts the users of such frameworks into the double jeopardy of mutating state from within multiple threads. The dreaded result of that, of course, is race conditions and concurrent update anomalies.

Fortunately, there are functional languages that provide facilities that reduce the problems of mutation and allow the functional style to interface tolerably well with the multithreaded, nonfunctional style.

[[[Software Transactional Memory (STM)]{.calibre_3}]{.bold}]{.calibre1}

[STM]{.italic} is a set of mechanisms that treat internal memory as though it were a transactional commit/rollback database. The transactions are functions that are protected from concurrent update by a [compare-and-swap]{.italic} protocol.

If that was too much of a word salad, perhaps an example would be clarifying.

Let us say that we have an object [o]{.italic} and a function [f]{.italic} that mutates [o]{.italic}. So [o]{.italic}[[f]{.italic}]{.calibre3} = [f(o)]{.italic} where [o]{.italic}[[f]{.italic}]{.calibre3} is the original [o]{.italic} mutated by [f]{.italic}.

The problem is that [f]{.italic} takes time to do its work, and there is a chance that some other thread will interrupt [f]{.italic} and apply its own operation [g]{.italic} on [o]{.italic}: [o]{.italic}[[g]{.italic}]{.calibre3} = [g(o)]{.italic}. When [f]{.italic} finally completes, what is the state of [o]{.italic}? Is it [o]{.italic}[[f]{.italic}]{.calibre3}? Or is it [o]{.italic}[[g]{.italic}]{.calibre3}? Or have both mutations been applied, giving us [o]{.italic}[[f g]{.italic}]{.calibre3}?

The typical concurrent update problem would most often yield [o]{.italic}[[f]{.italic}]{.calibre3}, causing the operation of [g]{.italic} to be lost. Programmers often resolve this kind of problem by [locking o]{.italic} so that [g]{.italic} cannot interrupt [f]{.italic}, and vice versa. The lock forces the interrupting thread to wait until [o]{.italic} is unlocked. The problem, however, is that this can lead to the dreaded [deadly embrace]{.italic}.[]{#index_split_017.html#filepos159506}[[[[4]{.underline}]{.calibre_10}]{.calibre3}](#index_split_017.html#filepos159602)

[[[4]{.underline}]{.calibre_10}](#index_split_017.html#filepos159506). Sometimes known as [deadlock]{.italic}.

Imagine that we have two objects [o]{.italic} and [p]{.italic} and two functions [f(o, p)]{.italic} and [g(p, o)]{.italic}. These functions lock their arguments before operating on them. Suppose [f]{.italic} and [g]{.italic} are executing in different threads and [g]{.italic} interrupts [f]{.italic} just after [f]{.italic} locks [o]{.italic}. Now [g]{.italic} locks [p]{.italic} but cannot lock [o]{.italic} because [o]{.italic} is locked by [f]{.italic}, so [g]{.italic} waits. Now [f]{.italic} wakes up and tries to lock [p]{.italic} but cannot because [p]{.italic} is locked by [g]{.italic}---and nothing can proceed. The functions [f]{.italic} and [g]{.italic} are in a deadly embrace.

The problem of deadly embrace can be avoided by locking everything in the same order every time. If [f]{.italic} and [g]{.italic} agree to lock [o]{.italic} first and [p]{.italic} second, then the embrace cannot happen. However, these agreements are hard to enforce, and as systems get more and more complicated, a correct locking order can be very difficult to divine.

STM solves this problem by [not]{.italic} locking, and instead using a commit/rollback technique. Let's call this technique [swap]{.italic}. We can enact it with [swap(o, f)]{.italic}, which will hold the current value of [o]{.italic} in [o]{.italic}[[h]{.italic}]{.calibre3}, compute []{#index_split_017.html#filepos161108}[o]{.italic}[[f]{.italic}]{.calibre3} = [f(o)]{.italic}, and then, in an [atomic]{.italic}[]{#index_split_017.html#filepos161198}[[[[5]{.underline}]{.calibre_10}]{.calibre3}](#index_split_017.html#filepos161601) operation, compare the current value of [o]{.italic} with [o]{.italic}[[h]{.italic}]{.calibre3} and, if they are the same, swap [o]{.italic} with [o]{.italic}[[f]{.italic}]{.calibre3}. If the compare fails, then the operation is repeated from the beginning and will continue repeating until the compare succeeds.

[[[5]{.underline}]{.calibre_10}](#index_split_017.html#filepos161198). Atomic operations cannot be interrupted.

There are several ways to use STM in Clojure, but the simplest is the [` atom `{.calibre4}]{.calibre_17}. An [` atom `{.calibre4}]{.calibre_17} is an [atomic]{.italic} value that can be altered using the [` swap! `{.calibre4}]{.calibre_17} function. Here's an example:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_072.html#filepos961643)

> > [[`(def counter (atom 0))`{.calibre4}\
> > \
> > `(defn add-one [x]`{.calibre4}\
> > `  (let [y (inc x)]`{.calibre4}\
> > `    (print (str "(" x ")"))`{.calibre4}\
> > `    y))`{.calibre4}\
> > \
> > `(defn increment [n id]`{.calibre4}\
> > `  (dotimes [_ n]`{.calibre4}\
> > `    (print id)`{.calibre4}\
> > `    (swap! counter add-one)))`{.calibre4}\
> > \
> > `(defn -main []`{.calibre4}\
> > `  (let [ta (future (increment 10 "a"))`{.calibre4}\
> > `        tx (future (increment 10 "x"))`{.calibre4}\
> > `        _ @ta`{.calibre4}\
> > `        _ @tx]`{.calibre4}\
> > `    (println "\nCounter is: " @counter)))`{.calibre4}]{.calibre_3}]{.calibre_17}

The first line creates the [` atom `{.calibre4}]{.calibre_17} named [` counter `{.calibre4}]{.calibre_17}. The [` -main `{.calibre4}]{.calibre_17} program starts two threads, using [` future `{.calibre4}]{.calibre_17}, both of which call the [` increment `{.calibre4}]{.calibre_17} function. The [` @ta `{.calibre4}]{.calibre_17} and [` @tx `{.calibre4}]{.calibre_17} expressions wait for the respective threads to complete.

The [` add-one `{.calibre4}]{.calibre_17} function adds one to its argument, but that [` print `{.calibre4}]{.calibre_17} function can allow another thread to jump in; and that's exactly what happens. Here's an example of the output:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_073.html#filepos961789)

> > [[`a(0)a(1)a(2)a(3)a(4)xa(5)x(5)(6)(6)x(7)(7)a(8)(8)`{.calibre4}\
> > `x(9)(9)a(10)(10)x(11)a(11)(12)(12)a(13)x(13)(14)(14)`{.calibre4}\
> > `x(15)(15)(16)x(17)x(18)x(19)`{.calibre4}\
> > `Counter is:  20`{.calibre4}]{.calibre_3}]{.calibre_17}

At first, thread [` a `{.calibre4}]{.calibre_17} runs without interruption for a while. But at the fifth increment, the [` x `{.calibre4}]{.calibre_17} thread jumps in, and the two fight each other. Notice the repeated values as the [` swap! `{.calibre4}]{.calibre_17} detects the collisions and repeats. Finally, thread [` a `{.calibre4}]{.calibre_17} finishes and thread [` x `{.calibre4}]{.calibre_17} experiences no further interruptions. The end count of 20 is correct.

[[[Life Is Hard, Software Is Harder]{.calibre_3}]{.bold}]{.calibre1}

It would be nice to live, full time, in a functional world. Multiple threads in a functional world generally do not have race conditions.[]{#index_split_017.html#filepos165235}[[[[6]{.underline}]{.calibre_10}]{.calibre3}](#index_split_017.html#filepos165629) After all, if you never update, you can't have concurrent update problems. But all too often we are forced back into the multithreaded, nonfunctional world by frameworks, or legacy code. And when that happens, the mechanisms of STM can help us avoid the worst of an otherwise horrific situation.

[[[6]{.underline}]{.calibre_10}](#index_split_017.html#filepos165235). See [[[Chapter 15]{.underline}]{.calibre_10}](#index_split_030.html#filepos534355), Concurrency, for when they do.

::: {#index_split_017.html#calibre_pb_17 .mbp_pagebreak}
:::

[]{#index_split_018.html}

[[II]{.calibre_3}]{.calibre2}

[[Comparative Analysis]{.calibre_3}]{.calibre2}

What follows is a comparative analysis of a series of exercises written in traditional [object-oriented (OO)]{.italic} style and in "functional" style. The first two exercises may appear familiar to you; the OO portions come from examples that I published in [Clean Craftsmanship]{.italic}.[]{#index_split_018.html#filepos166411}[[[[1]{.underline}]{.calibre_10}]{.calibre3}](#index_split_018.html#filepos166507)

[[[1.]{.underline}]{.calibre_10}](#index_split_018.html#filepos166411) Robert C. Martin, [Clean Craftsmanship]{.italic} (Addison-Wesley, 2021).

Both versions of each of the examples were created using the discipline of [test-driven development (TDD)]{.italic}. The tests are shown with the code in an incremental fashion. You'll see how the first test was passed, then the second, then the third, and so on.

The point of this part of the book is to explore and examine the differences between OO implementations and functional implementations.

The exercises increase in complexity from one to the next. Prime Factors is pretty simple. Bowling Game is a bit more complicated and Gossiping Bus Drivers is more complicated still. The last exercise, Payroll, is the most complex of the examples. I explored it in great detail in Section 3 of [Agile Software Development: Principles, Patterns, and Practices]{.italic}.[]{#index_split_018.html#filepos167579}[[[[2]{.underline}]{.calibre_10}]{.calibre3}](#index_split_018.html#filepos167737) So to save space I've only included the functional version.

[[[2.]{.underline}]{.calibre_10}](#index_split_018.html#filepos167579) Robert C. Martin, [Agile Software Development: Principles, Patterns, and Practices]{.italic} (Pearson, 2002).

As the complexity increases, the differences between the approaches become more apparent. You should find this educational. But you should also be prepared for a few surprises; this may not end the way you think it should.

::: {#index_split_018.html#calibre_pb_18 .mbp_pagebreak}
:::

[]{#index_split_019.html}

[[[6]{.calibre_3}]{.bold}]{.calibre1}

[[[Prime Factors]{.calibre_3}]{.bold}]{.calibre1}

![](images/00138.jpg){.calibre_31}

Is functional programming better than programming with mutable variables? Let's do a comparative analysis of some familiar exercises. Here, for example, is the traditional Java derivation of the Prime Factors kata using TDD, roughly as it was presented in [[[Chapter 2]{.underline}]{.calibre_10}](#index_split_014.html#filepos89882) of [Clean Craftsmanship]{.italic}.[]{#index_split_019.html#filepos168973}[[[[3]{.underline}]{.calibre_10}]{.calibre3}](#index_split_019.html#filepos169297) A related video, [Prime Factors]{.italic}, is also available. You can access the video by registering at [[[https://informit.com/functionaldesign]{.underline}]{.calibre_10}](https://informit.com/functionaldesign).

[[[3]{.underline}]{.calibre_10}](#index_split_019.html#filepos168973). Martin, [Clean Craftsmanship]{.italic}, p. 52.

[[[Java Version]{.calibre_3}]{.bold}]{.calibre1}

We begin with a simple test:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_074.html#filepos961919)

> > [[`public class PrimeFactorsTest {`{.calibre4}\
> > `  @Test`{.calibre4}\
> > `  public void factors() throws Exception {`{.calibre4}\
> > `    assertThat(factorsOf(1), is(empty()));`{.calibre4}\
> > `  }`{.calibre4}\
> > `}`{.calibre4}]{.calibre_3}]{.calibre_17}

And we make it pass in this simple way:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_075.html#filepos962065)

> > [[`private List<Integer> factorsOf(int n) {`{.calibre4}\
> > `  return new ArrayList<>();`{.calibre4}\
> > `}`{.calibre4}]{.calibre_3}]{.calibre_17}

Of course, this passes. So the next most degenerate test is 2:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_076.html#filepos962210)

> > [[`assertThat(factorsOf(2), contains(2));`{.calibre4}]{.calibre_3}]{.calibre_17}

We make this pass with some trivial and obvious code:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_077.html#filepos962355)

> > [[`private List<Integer> factorsOf(int n) {`{.calibre4}\
> > `  ArrayList<Integer> factors = new ArrayList<>();`{.calibre4}\
> > `  if (n>1)`{.calibre4}\
> > `    factors.add(2);`{.calibre4}\
> > `  return factors;`{.calibre4}\
> > `}`{.calibre4}]{.calibre_3}]{.calibre_17}

Next comes 3,

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_078.html#filepos962501)

> > [[`assertThat(factorsOf(3), contains(3));`{.calibre4}]{.calibre_3}]{.calibre_17}

which we make pass by being a bit clever and replacing the [` 2 `{.calibre4}]{.calibre_17} with [` n `{.calibre4}]{.calibre_17}:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_079.html#filepos962646)

> > [[`private List<Integer> factorsOf(int n) {`{.calibre4}\
> > `  ArrayList<Integer> factors = new ArrayList<>();`{.calibre4}\
> > `  if (n>1)`{.calibre4}\
> > `    factors.add(`{.calibre4}]{.calibre_3}]{.calibre_17}[[`n`{.calibre4}]{.calibre_3}]{.bold}[[`);`{.calibre4}\
> > `  return factors;`{.calibre4}\
> > `}`{.calibre4}]{.calibre_3}]{.calibre_17}

Next comes 4, which is the first time our list will have more than one factor in it:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_080.html#filepos962792)

> > [[`assertThat(factorsOf(4), contains(2, 2));`{.calibre4}]{.calibre_3}]{.calibre_17}

And we make it pass with what appears to be a pretty awful hack:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_081.html#filepos962937)

> > [[`private List<Integer> factorsOf(int n) {`{.calibre4}\
> > `  ArrayList<Integer> factors = new ArrayList<>();`{.calibre4}\
> > `  if (n>1) {`{.calibre4}\
> > `    `{.calibre4}]{.calibre_3}]{.calibre_17}[[`if (n % 2 == 0) {`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `       `{.calibre4}]{.calibre_3}]{.calibre_17}[[`factors.add(2);`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `      `{.calibre4}]{.calibre_3}]{.calibre_17}[[`n /= 2;`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `    `{.calibre4}]{.calibre_3}]{.calibre_17}[[`}`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `  `{.calibre4}]{.calibre_3}]{.calibre_17}[[`}`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `  `{.calibre4}]{.calibre_3}]{.calibre_17}[[`if (n>1)`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `    `{.calibre4}]{.calibre_3}]{.calibre_17}[[`factors.add(n);`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `  return factors;`{.calibre4}\
> > `}`{.calibre4}]{.calibre_3}]{.calibre_17}

The next three tests pass without any changes:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_082.html#filepos963083)

> > [[`assertThat(factorsOf(5), contains(5));`{.calibre4}\
> > `assertThat(factorsOf(6), contains(2,3));`{.calibre4}\
> > `assertThat(factorsOf(7), contains(7));`{.calibre4}]{.calibre_3}]{.calibre_17}

The 8 case is the first time we've seen more than two elements in the list of factors:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_083.html#filepos963228)

> > [[`assertThat(factorsOf(8), contains(2, 2, 2));`{.calibre4}]{.calibre_3}]{.calibre_17}

And we pass this with the elegant transformation of one of the [` if `{.calibre4}]{.calibre_17} statements into a [` while `{.calibre4}]{.calibre_17}:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_084.html#filepos963373)

> > [[`private List<Integer> factorsOf(int n) {`{.calibre4}\
> > `  ArrayList<Integer> factors = new ArrayList<>();`{.calibre4}\
> > `  if (n>1) {`{.calibre4}\
> > `    `{.calibre4}]{.calibre_3}]{.calibre_17}[[`while`{.calibre4}]{.calibre_3}]{.bold}[[` (n % 2 == 0) {`{.calibre4}\
> > `      factors.add(2);`{.calibre4}\
> > `      n /= 2;`{.calibre4}\
> > `    }`{.calibre4}\
> > `  }`{.calibre4}\
> > `  if (n>1)`{.calibre4}\
> > `    factors.add(n);`{.calibre4}\
> > `  return factors;`{.calibre4}\
> > `}`{.calibre4}]{.calibre_3}]{.calibre_17}

The next test, 9, must also fail because nothing in our solution factors out 3:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_085.html#filepos963519)

> > [[`assertThat(factorsOf(9), contains(3, 3));`{.calibre4}]{.calibre_3}]{.calibre_17}

To solve it, we need to factor out 3's. We could do that as follows:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_086.html#filepos963664)

> > [[`private List<Integer> factorsOf(int n) {`{.calibre4}\
> > `  ArrayList<Integer> factors = new ArrayList<>();`{.calibre4}\
> > `  if (n>1) {`{.calibre4}\
> > `    while (n % 2 == 0) {`{.calibre4}\
> > `      factors.add(2);`{.calibre4}\
> > `      n /= 2;`{.calibre4}\
> > `    }`{.calibre4}\
> > `    `{.calibre4}]{.calibre_3}]{.calibre_17}[[`while (n % 3 == 0) {`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `      `{.calibre4}]{.calibre_3}]{.calibre_17}[[`factors.add(3);`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `      `{.calibre4}]{.calibre_3}]{.calibre_17}[[`n /= 3;`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `    `{.calibre4}]{.calibre_3}]{.calibre_17}[[`}`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `  }`{.calibre4}\
> > `  if (n>1)`{.calibre4}\
> > `    factors.add(n);`{.calibre4}\
> > `  return factors;`{.calibre4}\
> > `}`{.calibre4}]{.calibre_3}]{.calibre_17}

But this is horrific because it implies endless duplication. We can solve that by changing another [` if `{.calibre4}]{.calibre_17} to a [` while `{.calibre4}]{.calibre_17}:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_087.html#filepos963810)

> > [[`private List<Integer> factorsOf(int n) {`{.calibre4}\
> > `  ArrayList<Integer> factors = new ArrayList<>();`{.calibre4}\
> > `  `{.calibre4}]{.calibre_3}]{.calibre_17}[[`int divisor = 2;`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `  `{.calibre4}]{.calibre_3}]{.calibre_17}[[`while`{.calibre4}]{.calibre_3}]{.bold}[[` (n>1) {`{.calibre4}\
> > `    while (n % `{.calibre4}]{.calibre_3}]{.calibre_17}[[`divisor`{.calibre4}]{.calibre_3}]{.bold}[[` == 0) {`{.calibre4}\
> > `      factors.add(`{.calibre4}]{.calibre_3}]{.calibre_17}[[`divisor`{.calibre4}]{.calibre_3}]{.bold}[[`);`{.calibre4}\
> > `      n /= `{.calibre4}]{.calibre_3}]{.calibre_17}[[`divisor`{.calibre4}]{.calibre_3}]{.bold}[[`;`{.calibre4}\
> > `    }`{.calibre4}\
> > `    `{.calibre4}]{.calibre_3}]{.calibre_17}[[`divisor++;`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `  }`{.calibre4}\
> > `  if (n>1)`{.calibre4}\
> > `    factors.add(n);`{.calibre4}\
> > `  return factors;`{.calibre4}\
> > `}`{.calibre4}]{.calibre_3}]{.calibre_17}

Just a little bit of refactoring and we get this:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_088.html#filepos963956)

> > [[`private List<Integer> factorsOf(int n) {`{.calibre4}\
> > `  ArrayList<Integer> factors = new ArrayList<>();`{.calibre4}\
> > \
> > `  for (int divisor = 2; n > 1; divisor++)`{.calibre4}\
> > `    for (; n % divisor == 0; n /= divisor)`{.calibre4}\
> > `      factors.add(divisor);`{.calibre4}\
> > `  return factors;`{.calibre4}\
> > `}`{.calibre4}]{.calibre_3}]{.calibre_17}
>
> []{#index_split_019.html#filepos181363}

And that algorithm is sufficient to compute the prime factors of any[]{#index_split_019.html#filepos181492}[[[[4]{.underline}]{.calibre_10}]{.calibre3}](#index_split_019.html#filepos181597) integer.

[[[4.]{.underline}]{.calibre_10}](#index_split_019.html#filepos181492) Given enough time and space.

[[[Clojure Version]{.calibre_3}]{.bold}]{.calibre1}

OK, so what does this look like in Clojure?

As before, we begin with a simple degenerate test:[]{#index_split_019.html#filepos182034}[[[[5]{.underline}]{.calibre_10}]{.calibre3}](#index_split_019.html#filepos182130)

[[[5.]{.underline}]{.calibre_10}](#index_split_019.html#filepos182034) Using the [` speclj `{.calibre4}]{.calibre_17} testing framework.

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_089.html#filepos964102)

> > [[`(should= [] (prime-factors-of 1))`{.calibre4}]{.calibre_3}]{.calibre_17}

And we make that pass as one might expect, by returning an empty list:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_090.html#filepos964247)

> > [[`(defn prime-factors-of [n] [])`{.calibre4}]{.calibre_3}]{.calibre_17}

The next test follows the Java version pretty closely:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_091.html#filepos964392)

> > [[`(should= [2] (prime-factors-of 2))`{.calibre4}]{.calibre_3}]{.calibre_17}

So does the solution:

> > [[`(defn prime-factors-of [n]`{.calibre4}\
> > `  `{.calibre4}]{.calibre_3}]{.calibre_17}[[`(if (> n 1) [2]`{.calibre4}]{.calibre_3}]{.bold}[[` []`{.calibre4}]{.calibre_3}]{.calibre_17}[[`)`{.calibre4}]{.calibre_3}]{.bold}[[`)`{.calibre4}]{.calibre_3}]{.calibre_17}

And the solution to the third test employs the same clever replacement of [` 2 `{.calibre4}]{.calibre_17} by [` n `{.calibre4}]{.calibre_17}:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_092.html#filepos964537)

> > [[`(should= [3] (prime-factors-of 3))`{.calibre4}\
> > \
> > `(defn prime-factors-of [n]`{.calibre4}\
> > `  (if (> n 1) [`{.calibre4}]{.calibre_3}]{.calibre_17}[[`n`{.calibre4}]{.calibre_3}]{.bold}[[`] []))`{.calibre4}]{.calibre_3}]{.calibre_17}

But with the test for 4, the Clojure and Java solutions begin to diverge:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_093.html#filepos964682)

> > [[`(should= [2 2] (prime-factors-of 4))`{.calibre4}\
> > \
> > `(defn prime-factors-of [n]`{.calibre4}\
> > `  (if (> n 1)`{.calibre4}\
> > `    `{.calibre4}]{.calibre_3}]{.calibre_17}[[`(if (zero? (rem n 2))`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `      `{.calibre4}]{.calibre_3}]{.calibre_17}[[`(cons 2 (prime-factors-of (quot n 2)))`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `      `{.calibre4}]{.calibre_3}]{.calibre_17}[[`[n])`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `    []))`{.calibre4}]{.calibre_3}]{.calibre_17}

The solution is recursive. The [` cons `{.calibre4}]{.calibre_17} function prepends a [` 2 `{.calibre4}]{.calibre_17} onto the beginning of the list returned by [` prime-factors-of `{.calibre4}]{.calibre_17}. Convince yourself that you understand why! The [` rem `{.calibre4}]{.calibre_17} and [` quot `{.calibre4}]{.calibre_17} functions are just the integer remainder and quotient operations, respectively.

At this point in the Java program, there was no iteration. The two [` if(n>1) `{.calibre4}]{.calibre_17} segments were a tantalizing hint of the iteration that was to come, but the solution was still just straight linear logic.

In the functional version, however, we see full-blown recursion. It's not even tail-called.

The next four tests pass outright, even the test for 8:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_094.html#filepos964828)

> > [[`(should= [5] (prime-factors-of 5))`{.calibre4}\
> > `(should= [2 3] (prime-factors-of 6))`{.calibre4}\
> > `(should= [7] (prime-factors-of 7))`{.calibre4}\
> > `(should= [2 2 2] (prime-factors-of 8))`{.calibre4}]{.calibre_3}]{.calibre_17}

In some ways, this is a shame since it was the test for 8 that caused us to transform an [` if `{.calibre4}]{.calibre_17} to a [` while `{.calibre4}]{.calibre_17} in the Java solution. No such elegant transformation takes place in the Clojure solution; though I have to say that the recursion is the better solution---so far.

Next comes the test for 9. And here the Java and Clojure versions face the similar dilemma of duplicated code:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_095.html#filepos964973)

> > [[`(should= [3 3] (prime-factors-of 9))`{.calibre4}\
> > \
> > `(defn prime-factors-of [n]`{.calibre4}\
> > `  (if (> n 1)`{.calibre4}\
> > `    (if (zero? (rem n 2))`{.calibre4}\
> > `      (cons 2 (prime-factors-of (quot n 2)))`{.calibre4}\
> > `      `{.calibre4}]{.calibre_3}]{.calibre_17}[[`(if (zero? (rem n 3))`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `        `{.calibre4}]{.calibre_3}]{.calibre_17}[[`(cons 3 (prime-factors-of (quot n 3)))`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `        [n]`{.calibre4}]{.calibre_3}]{.calibre_17}[[`)`{.calibre4}]{.calibre_3}]{.bold}[[`)`{.calibre4}\
> > `    []))`{.calibre4}]{.calibre_3}]{.calibre_17}

This solution is not sustainable. It would force us to add the 5, 7, 11, 13... cases all the way up to the maximum prime that our language could hold. But this solution does imply an interesting iterative/recursive solution:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_096.html#filepos965119)

> > [[`(defn prime-factors-of [n]`{.calibre4}\
> > `    `{.calibre4}]{.calibre_3}]{.calibre_17}[[`(loop [n n`{.calibre4}]{.calibre_3}]{.bold}[[` `{.calibre4}\
> > `           `{.calibre4}]{.calibre_3}]{.calibre_17}[[`divisor 2`{.calibre4}]{.calibre_3}]{.bold}[[` `{.calibre4}\
> > `           `{.calibre4}]{.calibre_3}]{.calibre_17}[[`factors []]`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `      (if (> n 1)`{.calibre4}\
> > `        (if (zero? (rem n `{.calibre4}]{.calibre_3}]{.calibre_17}[[`divisor`{.calibre4}]{.calibre_3}]{.bold}[[`))`{.calibre4}\
> > `          `{.calibre4}]{.calibre_3}]{.calibre_17}[[`(recur`{.calibre4}]{.calibre_3}]{.bold}[[` (quot n `{.calibre4}]{.calibre_3}]{.calibre_17}[[`divisor`{.calibre4}]{.calibre_3}]{.bold}[[`) divisor `{.calibre4}]{.calibre_3}]{.calibre_17}[[`(conj factors divisor))`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `          `{.calibre4}]{.calibre_3}]{.calibre_17}[[`(recur n (inc divisor) factors))`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `        factors)))`{.calibre4}]{.calibre_3}]{.calibre_17}

The [` loop `{.calibre4}]{.calibre_17} function creates a new anonymous function in situ. The [` recur `{.calibre4}]{.calibre_17} function, when nested inside a [` loop `{.calibre4}]{.calibre_17} expression, causes the in situ function to be reinvoked with TCO. The arguments to the in situ function are [` n `{.calibre4}]{.calibre_17}, [` divisor `{.calibre4}]{.calibre_17}, and [` factors `{.calibre4}]{.calibre_17}. Each is followed by its initializer. So the [` n `{.calibre4}]{.calibre_17} within the loop is initialized to the value of [` n `{.calibre4}]{.calibre_17} outside the loop (the two [` n `{.calibre4}]{.calibre_17} identifiers are distinct), [` divisor `{.calibre4}]{.calibre_17} is initialized to [` 2 `{.calibre4}]{.calibre_17}, and [` factors `{.calibre4}]{.calibre_17} is initialized to [` [] `{.calibre4}]{.calibre_17}.

The recursion in this solution is iterative because the recursive calls are at the tail. Note that the [` cons `{.calibre4}]{.calibre_17} has been changed to a [` conj `{.calibre4}]{.calibre_17} because the ordering []{#index_split_019.html#filepos192234}of the list construction has changed. The [` conj `{.calibre4}]{.calibre_17} function appends[]{#index_split_019.html#filepos192348}[[[[6]{.underline}]{.calibre_10}]{.calibre3}](#index_split_019.html#filepos192568) to [` factors `{.calibre4}]{.calibre_17}. Convince yourself that you understand why the ordering has changed!

[[[6.]{.underline}]{.calibre_10}](#index_split_019.html#filepos192348) In this case because [` factors `{.calibre4}]{.calibre_17} is a vector.

[[[Conclusion]{.calibre_3}]{.bold}]{.calibre1}

There are several things to note about this example. First, the sequence of tests is the same between the Java and Clojure versions. This is significant because it implies that the change to functional programming has little to no impact on the way we express our tests. Tests are somehow more basic, more abstract, or more essential than the programming style.

Second, the solution strategy between the two deviated even before any iteration was required. In Java, the test for 4 did not require iteration; but in Clojure, it caused us to use recursion. This implies that recursion is somehow more semantically essential than standard looping with [` while `{.calibre4}]{.calibre_17} statements.

Third, the derivation in Java was relatively straightforward; there were few, if any, surprises from one test to the next. But the Clojure derivation took a U-turn once we got to the test for 9. This was because we chose to use non-tail recursion instead of the iterative [` loop `{.calibre4}]{.calibre_17} construct to solve the test for 4. This implies that, when we have a choice, we should prefer tail-recursive constructs to non-tail recursion.

The end result is an algorithm that is similar to the Java solution but has at least one surprising difference: It is not a doubly nested loop. The Java solution has one loop that increments the divisor and another that repeatedly adds the current divisor as a factor. The Clojure solution replaces that doubly nested loop with two independent recursions.

Which solution is better? The Java solution is a lot faster because Java is a lot faster than Clojure. But otherwise, I see no particular benefit to either. To those who know both languages well, neither is easier than the []{#index_split_019.html#filepos194852}other to read or understand. Neither is riskier or better structured than the other. From my point of view, it's a wash. Other than the intrinsic speed of Java, there is no advantage to either style that overrides the other.

However, this is the last example for which the results will be ambiguous. As we proceed from example to example, the differences will become more and more significant.

::: {#index_split_019.html#calibre_pb_19 .mbp_pagebreak}
:::

[]{#index_split_020.html}

[[[7]{.calibre_3}]{.bold}]{.calibre1}

[[[Bowling Game]{.calibre_3}]{.bold}]{.calibre1}

![](images/00161.jpg){.calibre_32}

Now let's look at another traditional TDD exercise: the Bowling Game kata. What follows is a much-abbreviated version of that kata that appeared in [Clean Craftsmanship]{.italic}.[]{#index_split_020.html#filepos195873}[[[[1]{.underline}]{.calibre_10}]{.calibre3}](#index_split_020.html#filepos196196) A related video, [Bowling Game]{.italic}, is also available. You can access the video by registering at [[[https://informit.com/functionaldesign]{.underline}]{.calibre_10}](https://informit.com/functionaldesign).

[[[1]{.underline}]{.calibre_10}](#index_split_020.html#filepos195873). Robert C. Martin, [Clean Craftsmanship]{.italic} (Addison-Wesley, 2021).

[[[Java Version]{.calibre_3}]{.bold}]{.calibre1}

We begin, as always, with a test that does nothing, just to prove we can compile and execute:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_097.html#filepos965250)

> > [[`public class BowlingTest {`{.calibre4}\
> > `  @Test`{.calibre4}\
> > `  public void nothing() throws Exception {`{.calibre4}\
> > `  }`{.calibre4}\
> > `}`{.calibre4}]{.calibre_3}]{.calibre_17}

Next, we assert that we can create an instance of the [` Game `{.calibre4}]{.calibre_17} class:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_098.html#filepos965396)

> > [[`@Test`{.calibre4}\
> > `public void canCreateGame() throws Exception {`{.calibre4}\
> > `  Game g = new Game();`{.calibre4}\
> > `}`{.calibre4}]{.calibre_3}]{.calibre_17}

And then we make that compile and pass by directing the integrated development environment (IDE) to create the missing class:

> > [[`public class Game {`{.calibre4}\
> > `}`{.calibre4}]{.calibre_3}]{.calibre_17}

Next, we see if we can roll one ball:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_099.html#filepos965541)

> > [[`@Test`{.calibre4}\
> > `public void canRoll() throws Exception {`{.calibre4}\
> > `  Game g = new Game();`{.calibre4}\
> > `  g.roll(0);`{.calibre4}\
> > `}`{.calibre4}]{.calibre_3}]{.calibre_17}
>
> []{#index_split_020.html#filepos198476}

And then we make that compile and pass by directing the IDE to create the [` roll `{.calibre4}]{.calibre_17} function, and we give the argument a reasonable name:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_100.html#filepos965687)

> > [[`public class Game {`{.calibre4}\
> > `  public void roll(int pins) {`{.calibre4}\
> > `  }`{.calibre4}\
> > `}`{.calibre4}]{.calibre_3}]{.calibre_17}

There's a bit of duplication in the tests already. We should get rid of it. So we factor out the creation of the game into the [` setup `{.calibre4}]{.calibre_17} function:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_101.html#filepos965832)

> > [[`public class BowlingTest {`{.calibre4}\
> > `  private Game g;`{.calibre4}\
> > \
> > `  @Before`{.calibre4}\
> > `  public void setUp() throws Exception {`{.calibre4}\
> > `    g = new Game();`{.calibre4}\
> > `  }`{.calibre4}\
> > `}`{.calibre4}]{.calibre_3}]{.calibre_17}

This makes the first test completely empty. So we delete it. The second test is also pretty useless since it doesn't assert anything, so we delete it as well.

Next, we want to assert that we can score a game. But to do that we need to roll a complete game:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_102.html#filepos965978)

> > [[`@Test`{.calibre4}\
> > `public void gutterGame() throws Exception {`{.calibre4}\
> > `  for (int i=0; i<20; i++)`{.calibre4}\
> > `    g.roll(0);`{.calibre4}\
> > `  assertEquals(0, g.score());`{.calibre4}\
> > `}`{.calibre4}\
> > \
> > ]{.calibre_3}]{.calibre_17}[[`public int score() {`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `  `{.calibre4}]{.calibre_3}]{.calibre_17}[[`return 0;`{.calibre4}]{.calibre_3}]{.bold}[[\
> > ]{.calibre_3}]{.calibre_17}[[`}`{.calibre4}]{.calibre_3}]{.bold}

Next come all ones:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_103.html#filepos966124)

> > [[`@Test`{.calibre4}\
> > `public void allOnes() throws Exception {`{.calibre4}\
> > `  for (int i=0; i<20; i++)`{.calibre4}\
> > `    g.roll(1);`{.calibre4}\
> > `  assertEquals(20, g.score());`{.calibre4}\
> > `}`{.calibre4}\
> > \
> > `public class Game {`{.calibre4}\
> > `  `{.calibre4}]{.calibre_3}]{.calibre_17}[[`private int score;`{.calibre4}]{.calibre_3}]{.bold}[[\
> > \
> > `  public void roll(int pins) {`{.calibre4}\
> > `    `{.calibre4}]{.calibre_3}]{.calibre_17}[[`score += pins;`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `  }`{.calibre4}\
> > \
> > `  public int score() {`{.calibre4}\
> > `    return `{.calibre4}]{.calibre_3}]{.calibre_17}[[`score;`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `  }`{.calibre4}\
> > `}`{.calibre4}]{.calibre_3}]{.calibre_17}

The duplication in the tests can be eliminated by extracting a function called [` rollMany `{.calibre4}]{.calibre_17}:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_104.html#filepos966270)

> > [[`public class BowlingTest {`{.calibre4}\
> > `  private Game g;`{.calibre4}\
> > \
> > `  @Before`{.calibre4}\
> > `  public void setUp() throws Exception {`{.calibre4}\
> > `    g = new Game();`{.calibre4}\
> > `  }`{.calibre4}\
> > \
> > `  `{.calibre4}]{.calibre_3}]{.calibre_17}[[`private void rollMany(int n, int pins) {`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `    `{.calibre4}]{.calibre_3}]{.calibre_17}[[`for (int i=0; i<n; i++) {`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `      `{.calibre4}]{.calibre_3}]{.calibre_17}[[`g.roll(pins);`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `    `{.calibre4}]{.calibre_3}]{.calibre_17}[[`}`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `  `{.calibre4}]{.calibre_3}]{.calibre_17}[[`}`{.calibre4}]{.calibre_3}]{.bold}[[\
> > \
> > `  @Test`{.calibre4}\
> > `  public void gutterGame() throws Exception {`{.calibre4}\
> > `    `{.calibre4}]{.calibre_3}]{.calibre_17}[[`rollMany(20, 0);`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `    assertEquals(0, g.score());`{.calibre4}\
> > `  }`{.calibre4}\
> > \
> > `  @Test`{.calibre4}\
> > `  public void allOnes() throws Exception {`{.calibre4}\
> > `    `{.calibre4}]{.calibre_3}]{.calibre_17}[[`rollMany(20, 1);`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `    assertEquals(20, g.score());`{.calibre4}\
> > `  }`{.calibre4}\
> > `}`{.calibre4}]{.calibre_3}]{.calibre_17}

OK, next test. One spare, with one extra bonus ball, and all the rest gutter balls:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_105.html#filepos966416)

> > [[`@Test`{.calibre4}\
> > `public void oneSpare() throws Exception {`{.calibre4}\
> > `  rollMany(2, 5);`{.calibre4}\
> > `  g.roll(7);`{.calibre4}\
> > `  rollMany(17, 0);`{.calibre4}\
> > `  assertEquals(24, g.score());`{.calibre4}\
> > `}`{.calibre4}]{.calibre_3}]{.calibre_17}

This test fails, of course. We have to refactor the algorithm in order to get this to pass. We move the computation of the score out of the [` roll `{.calibre4}]{.calibre_17} method and into the [` score `{.calibre4}]{.calibre_17} method, and we walk through the [` rolls `{.calibre4}]{.calibre_17} array two balls (one frame) at a time:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_106.html#filepos966562)

> > [[`public int score() {`{.calibre4}\
> > `  int score = 0;`{.calibre4}\
> > `  int frameIndex = 0;`{.calibre4}\
> > `  for (int frame = 0; frame < 10; frame++) {`{.calibre4}\
> > `    if (isSpare(frameIndex)) {`{.calibre4}\
> > `      score += 10 + rolls[frameIndex + 2];`{.calibre4}\
> > `      frameIndex += 2;`{.calibre4}\
> > `    } else {`{.calibre4}\
> > `      score += rolls[frameIndex] + rolls[frameIndex + 1];`{.calibre4}\
> > `      frameIndex += 2;`{.calibre4}\
> > `    }`{.calibre4}\
> > `  }`{.calibre4}\
> > `  return score;`{.calibre4}\
> > `}`{.calibre4}\
> > \
> > `private boolean isSpare(int frameIndex) {`{.calibre4}\
> > `  return rolls[frameIndex] + rolls[frameIndex + 1] == 10;`{.calibre4}\
> > `}`{.calibre4}]{.calibre_3}]{.calibre_17}

One strike is next:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_107.html#filepos966708)

> > [[`@Test`{.calibre4}\
> > `public void oneStrike() throws Exception {`{.calibre4}\
> > `  g.roll(10);`{.calibre4}\
> > `  g.roll(2);`{.calibre4}\
> > `  g.roll(3);`{.calibre4}\
> > `  rollMany(16, 0);`{.calibre4}\
> > `  assertEquals(20, g.score());`{.calibre4}\
> > `}`{.calibre4}]{.calibre_3}]{.calibre_17}

Passing it is just a matter of adding the strike condition, and then we refactor a bit:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_108.html#filepos966854)

> > [[`public int score() {`{.calibre4}\
> > `  int score = 0;`{.calibre4}\
> > `  int frameIndex = 0;`{.calibre4}\
> > `  for (int frame = 0; frame < 10; frame++) {`{.calibre4}\
> > `    `{.calibre4}]{.calibre_3}]{.calibre_17}[[`if (isStrike(frameIndex)) {`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `      `{.calibre4}]{.calibre_3}]{.calibre_17}[[`score += 10 + strikeBonus(frameIndex);`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `      `{.calibre4}]{.calibre_3}]{.calibre_17}[[`frameIndex++;`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `    `{.calibre4}]{.calibre_3}]{.calibre_17}[[`} else`{.calibre4}]{.calibre_3}]{.bold}[[` if (isSpare(frameIndex)) {`{.calibre4}\
> > `      score += 10 + `{.calibre4}]{.calibre_3}]{.calibre_17}[[`spareBonus(frameIndex)`{.calibre4}]{.calibre_3}]{.bold}[[`;`{.calibre4}\
> > `      frameIndex += 2;`{.calibre4}\
> > `    } else {`{.calibre4}\
> > `      score += `{.calibre4}]{.calibre_3}]{.calibre_17}[[`twoBallsInFrame(frameIndex)`{.calibre4}]{.calibre_3}]{.bold}[[`;`{.calibre4}\
> > `      frameIndex += 2;`{.calibre4}\
> > `    }`{.calibre4}\
> > `  }`{.calibre4}\
> > `  return score;`{.calibre4}\
> > `}`{.calibre4}]{.calibre_3}]{.calibre_17}
>
> []{#index_split_020.html#filepos208585}

Lastly, we test for a perfect game:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_020.html#filepos206963)

> > [[`@Test`{.calibre4}\
> > `public void perfectGame() throws Exception {`{.calibre4}\
> > `  rollMany(12, 10);`{.calibre4}\
> > `  assertEquals(300, g.score());`{.calibre4}\
> > `}`{.calibre4}]{.calibre_3}]{.calibre_17}

And this passes without change.

[[[Clojure Version]{.calibre_3}]{.bold}]{.calibre1}

Things start out quite differently in Clojure. We have no classes to create, and there is no need for a [` roll `{.calibre4}]{.calibre_17} method. So our first test is the gutter game:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_110.html#filepos967146)

> > [[`(should= 0 (score (repeat`{.calibre4}]{.calibre_3}]{.calibre_17}[[[[2]{.underline}]{.calibre_10}]{.calibre3}](#index_split_020.html#filepos210118)[[` 20 0)))`{.calibre4}\
> > \
> > `(defn score [rolls] 0)`{.calibre4}]{.calibre_3}]{.calibre_17}
>
> []{#index_split_020.html#filepos210098}

[[[2]{.underline}]{.calibre_10}](#index_split_020.html#filepos210098). The [` repeat `{.calibre4}]{.calibre_17} function returns a sequence of repeating values. In this case, it is a sequence of 20 zeros.

Followed quickly by all ones:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_111.html#filepos967291)

> > [[`(should= 20 (score (repeat 20 1)))`{.calibre4}\
> > \
> > `(defn score [rolls]`{.calibre4}\
> > `  (reduce + rolls))`{.calibre4}]{.calibre_3}]{.calibre_17}

No surprises here. The [` reduce `{.calibre4}]{.calibre_17}[]{#index_split_020.html#filepos210976}[[[[3]{.underline}]{.calibre_10}]{.calibre3}](#index_split_020.html#filepos211210) function simply applies the [` + `{.calibre4}]{.calibre_17} function across the entire list. So our next test is one spare:

[[[3]{.underline}]{.calibre_10}](#index_split_020.html#filepos210976). You will want to look this function up. It does much more than this paragraph suggests. But you'll see that soon enough.

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_112.html#filepos967436)

> > [[`(should= 24 (score (concat [5 5 7] (repeat 17 0)))))`{.calibre4}]{.calibre_3}]{.calibre_17}

To make this pass, we go through several steps. The first is to break the [` rolls `{.calibre4}]{.calibre_17} array up into frames and sum up the frames. At first, we assume that frames have just two rolls:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_113.html#filepos967581)

> > [[`(defn to-frames [rolls]`{.calibre4}\
> > `  (partition`{.calibre4}]{.calibre_3}]{.calibre_17}[[[[4]{.underline}]{.calibre_10}]{.calibre3}](#index_split_020.html#filepos212783)[[` 2 rolls))`{.calibre4}\
> > \
> > `(defn add-frame [score frame]`{.calibre4}\
> > `  (+ score (reduce + frame)))`{.calibre4}\
> > \
> > `(defn score [rolls]`{.calibre4}\
> > `  (reduce add-frame 0 (to-frames rolls)))`{.calibre4}]{.calibre_3}]{.calibre_17}
>
> []{#index_split_020.html#filepos212763}

[[[4]{.underline}]{.calibre_10}](#index_split_020.html#filepos212763). The [` partition `{.calibre4}]{.calibre_17} function breaks the [` rolls `{.calibre4}]{.calibre_17} list into a list of pairs. So [` [1 2 3 4 5 6] `{.calibre4}]{.calibre_17} becomes [` [[1 2][3 4][5 6]] `{.calibre4}]{.calibre_17}.

Now the [` reduce `{.calibre4}]{.calibre_17} function has come into its own. It cycles through the pairs of rolls, accumulating them into a score.

This change keeps all the previous tests passing, but it still fails the spare test. To pass that we have to add special processing to the [` to-frames `{.calibre4}]{.calibre_17} and [` add-frame `{.calibre4}]{.calibre_17} functions. Our goal is to put all the rolls needed to calculate a frame into the frame data.

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_114.html#filepos967727)

> > [[`(defn to-frames [rolls]`{.calibre4}\
> > `  (let [frames (partition 2 rolls)`{.calibre4}\
> > `        possible-bonuses (map #(take 1 %)`{.calibre4}]{.calibre_3}]{.calibre_17}[[[[5]{.underline}]{.calibre_10}]{.calibre3}](#index_split_020.html#filepos215206)[[` (rest frames))`{.calibre4}\
> > `        possible-bonuses`{.calibre4}]{.calibre_3}]{.calibre_17}[[[[6]{.underline}]{.calibre_10}]{.calibre3}](#index_split_020.html#filepos215805)[[` (concat`{.calibre4}]{.calibre_3}]{.calibre_17}[[[[7]{.underline}]{.calibre_10}]{.calibre3}](#index_split_020.html#filepos216184)[[` possible-bonuses [[0]])]`{.calibre4}\
> > `    (map concat frames possible-bonuses)))`{.calibre4}\
> > \
> > `(defn add-frame [score frame-and-bonus]`{.calibre4}\
> > `  (let [frame (take 2 frame-and-bonus)]`{.calibre4}\
> > `    (if (= 10 (reduce + frame))`{.calibre4}\
> > `      (+ score (reduce + frame-and-bonus))`{.calibre4}\
> > `      (+ score (reduce + frame)))))`{.calibre4}\
> > \
> > `(defn score [rolls]`{.calibre4}\
> > `  (reduce add-frame 0 (to-frames rolls)))`{.calibre4}]{.calibre_3}]{.calibre_17}
>
> []{#index_split_020.html#filepos215186}

[[[5]{.underline}]{.calibre_10}](#index_split_020.html#filepos215186). The [` #(…) `{.calibre4}]{.calibre_17} form creates an anonymous function. The [` % `{.calibre4}]{.calibre_17} symbol is the argument to that function. You can also use [` %n `{.calibre4}]{.calibre_17}, where [` n `{.calibre4}]{.calibre_17} is an integer representing the [n]{.italic}th argument. So [` #(take 1 %) `{.calibre4}]{.calibre_17} is a function that returns a list containing the first element of its argument.

[[[6]{.underline}]{.calibre_10}](#index_split_020.html#filepos215186). This is not a reassignment, or even a reinitialization. The second [` possible-bonuses `{.calibre4}]{.calibre_17} value is distinct from the first. Think of it like a local variable in Java hiding a function argument or a member variable of the same name.

[[[7]{.underline}]{.calibre_10}](#index_split_020.html#filepos215186). The [` concat `{.calibre4}]{.calibre_17} function concatenates lists together. So [` (concat [1 2] [3 4]) `{.calibre4}]{.calibre_17} returns [` [1 2 3 4] `{.calibre4}]{.calibre_17}.

Look closely at this code. There are lots of little tricks and workarounds in it. Why? Because Clojure is full of lots of lovely, tempting little tools that you can use to get data into [almost]{.italic} the form you want, and then use little tricks to maneuver the data into [exactly]{.italic} the form you want. If you aren't careful, those little tricks can start to dominate the code.

So, for example, see if you can figure out why I am passing [` [[0]] `{.calibre4}]{.calibre_17} into the [` concat `{.calibre4}]{.calibre_17} function in [` to-frames `{.calibre4}]{.calibre_17}.[]{#index_split_020.html#filepos217222}[[[[8]{.underline}]{.calibre_10}]{.calibre3}](#index_split_020.html#filepos217577) As another example, ask yourself why I used [` #(take 1 %) `{.calibre4}]{.calibre_17} instead of just [` first `{.calibre4}]{.calibre_17}.[]{#index_split_020.html#filepos217481}[[[[9]{.underline}]{.calibre_10}]{.calibre3}](#index_split_020.html#filepos217932)

[[[8]{.underline}]{.calibre_10}](#index_split_020.html#filepos217222). Since bonuses are based on the next frame, [` possible-bonuses `{.calibre4}]{.calibre_17} had one too few elements. That would have terminated the final call to [` map `{.calibre4}]{.calibre_17} one element too early.

[[[9]{.underline}]{.calibre_10}](#index_split_020.html#filepos217481). [` (take 1 x) `{.calibre4}]{.calibre_17} returns a list containing the first element in [` x `{.calibre4}]{.calibre_17}. [` first `{.calibre4}]{.calibre_17} returns the first element.

Because of the trickiness in this code, don't be too concerned if you are struggling to understand it. I struggled too when looking back over it. And so...

When these little tricks proliferate it's time to rethink the solution. So I refactored the solution into a simple [` loop `{.calibre4}]{.calibre_17}:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_115.html#filepos967873)

> > [[`(defn to-frames [rolls]`{.calibre4}\
> > `  (loop [remaining-rolls rolls`{.calibre4}\
> > `         frames []]`{.calibre4}\
> > `    (cond`{.calibre4}\
> > `      (empty? remaining-rolls)`{.calibre4}\
> > `      frames`{.calibre4}\
> > \
> > `      (= 10 (reduce + (take 2 remaining-rolls)))`{.calibre4}\
> > `      (recur (drop 2 remaining-rolls)`{.calibre4}\
> > `             (conj frames (take 3 remaining-rolls)))`{.calibre4}\
> > `      :else`{.calibre4}\
> > `      (recur (drop 2 remaining-rolls)`{.calibre4}\
> > `             (conj frames (take 2 remaining-rolls))))))`{.calibre4}\
> > \
> > `(defn add-frames [score frame]`{.calibre4}\
> > `  (+ score (reduce + frame)))`{.calibre4}\
> > \
> > `(defn score [rolls]`{.calibre4}\
> > `  (reduce add-frames 0 (to-frames rolls)))`{.calibre4}]{.calibre_3}]{.calibre_17}

This is looking a lot better. Moreover, it's starting to look a bit like the Java solution. The next test is one strike:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_116.html#filepos968019)

> > [[`(should= 20 (score (concat [10 2 3] (repeat 16 0)))))`{.calibre4}]{.calibre_3}]{.calibre_17}

And we make that pass by adding one more case to the [` cond `{.calibre4}]{.calibre_17}:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_117.html#filepos968164)

> > [[`(defn to-frames [rolls]`{.calibre4}\
> > `  (loop [remaining-rolls rolls`{.calibre4}\
> > `         frames []]`{.calibre4}\
> > `    (cond`{.calibre4}\
> > `      (empty? remaining-rolls)`{.calibre4}\
> > `      frames`{.calibre4}\
> > \
> > `      `{.calibre4}]{.calibre_3}]{.calibre_17}[[`(= 10 (first remaining-rolls))`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `      `{.calibre4}]{.calibre_3}]{.calibre_17}[[`(recur (rest remaining-rolls)`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `             `{.calibre4}]{.calibre_3}]{.calibre_17}[[`(conj frames (take 3 remaining-rolls)))`{.calibre4}]{.calibre_3}]{.bold}[[\
> > \
> > `      (= 10 (reduce + (take 2 remaining-rolls)))`{.calibre4}\
> > `      (recur (drop 2 remaining-rolls)`{.calibre4}\
> > `             (conj frames (take 3 remaining-rolls)))`{.calibre4}\
> > `      :else`{.calibre4}\
> > `      (recur (drop 2 remaining-rolls)`{.calibre4}\
> > `             (conj frames (take 2 remaining-rolls))))))`{.calibre4}\
> > \
> > `(defn add-frames [score frame]`{.calibre4}\
> > `  (+ score (reduce + frame)))`{.calibre4}\
> > \
> > `(defn score [rolls]`{.calibre4}\
> > `  (reduce add-frames 0 (to-frames rolls)))`{.calibre4}]{.calibre_3}]{.calibre_17}
>
> []{#index_split_020.html#filepos222018}

Trivial, right? So all that's left is the perfect game. And if this goes like the Java version, this test should just pass without modification:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_118.html#filepos968310)

> > [[`(should= 300 (score (repeat 12 10))))`{.calibre4}]{.calibre_3}]{.calibre_17}

But it doesn't! Can you see why? Perhaps the fix will elucidate that for you:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_119.html#filepos968455)

> > [[`(defn score [rolls]`{.calibre4}\
> > `  (reduce add-frames 0 `{.calibre4}]{.calibre_3}]{.calibre_17}[[`(take 10`{.calibre4}]{.calibre_3}]{.bold}[[` (to-frames rolls)`{.calibre4}]{.calibre_3}]{.calibre_17}[[`)`{.calibre4}]{.calibre_3}]{.bold}[[`))`{.calibre4}]{.calibre_3}]{.calibre_17}

The [` to-frames `{.calibre4}]{.calibre_17} function happily creates more than ten frames. It just runs to the end of the [` rolls `{.calibre4}]{.calibre_17} list making as many frames as it can. But a game of bowling is only ten frames.

[[[Conclusion]{.calibre_3}]{.bold}]{.calibre1}

There are quite a few interesting differences between the Java and Clojure versions of this problem. First, the Clojure version has no [` Game `{.calibre4}]{.calibre_17} class. So all the machinations we used to create that class in the Java version simply don't occur in the Clojure version.

You might think that the loss of the [` Game `{.calibre4}]{.calibre_17} class is a weakness of the Clojure version. After all, it's convenient to be able to just create a [` Game `{.calibre4}]{.calibre_17}, toss it a bunch of rolls, and then get the score. However, the Clojure version has decoupled the accumulation of the rolls from the computation of the score. Those concepts are not bound together in the Clojure version. And that makes me think that the Java version has a subtle violation of the Single Responsibility Principle.[]{#index_split_020.html#filepos224703}[[[[10]{.underline}]{.calibre_10}]{.calibre3}](#index_split_020.html#filepos224800)

[[[10]{.underline}]{.calibre_10}](#index_split_020.html#filepos224703). See Robert C. Martin, [Clean Architecture]{.italic} (Pearson, 2017).

Second, as we tried to solve the one spare case, we saw how the Clojure version got polluted with all those nasty little tricks. This is a real problem with Clojure programs (or perhaps Clojure programmers). It's just too easy to add one more nasty little trick to get things to work.

Third, the Clojure solution is significantly different from the Java solution. Oh, there are some points of similarity, to be sure. That [` cond `{.calibre4}]{.calibre_17} structure in the Clojure version is very reminiscent of the [` if/else `{.calibre4}]{.calibre_17} structure in the Java version. However, those two similar structures produced radically different results. The Java version produced the score. The Clojure version produced a frame that included the bonus balls for spares and strikes.

This is an interesting separation of concerns. It is a fact that computing the score forces both versions to identify all the rolls that impact each frame. However, the Java version does this in situ, whereas the Clojure version nicely separates those two concerns.

Which of these versions is better? The Java version ended up a bit simpler than the Clojure version; but it was also a bit more coupled. The separation of concerns in the Clojure version convinces me that between the two, it would be more flexible and useful.

But, of course, we are only talking about a dozen lines of code.

::: {#index_split_020.html#calibre_pb_20 .mbp_pagebreak}
:::

[]{#index_split_021.html}

[[[8]{.calibre_3}]{.bold}]{.calibre1}

[[[Gossiping Bus Drivers]{.calibre_3}]{.bold}]{.calibre1}

![](images/00216.jpg){.calibre_34}

So far in this comparative analysis we haven't found a strong reason to prefer functional programming over OO programming. So let's examine a slightly more interesting problem.

Object orientation was born in 1966 when Ole-Johan Dahl and Kristen Nygaard added some modifications to the ALGOL-60 language in order to make the language more amenable to discrete event simulation.[]{#index_split_021.html#filepos227439}[[[[1]{.underline}]{.calibre_10}]{.calibre3}](#index_split_021.html#filepos227637) The new language was called SIMULA-67 and is considered to be the first true OO programming language.

[[[1]{.underline}]{.calibre_10}](#index_split_021.html#filepos227439). Legend has it that they were simulating Norwegian ocean shipping.

So let's do a comparative analysis of a simple discrete event simulator. That should keep the problem squarely in the OO wheelhouse. A nice problem to choose is the Gossiping Bus Drivers kata.[]{#index_split_021.html#filepos228047}[[[[2]{.underline}]{.calibre_10}]{.calibre3}](#index_split_021.html#filepos228143)

[[[2]{.underline}]{.calibre_10}](#index_split_021.html#filepos228047). [[[https://kata-log.rocks/gossiping-bus-drivers-kata]{.underline}]{.calibre_10}](https://kata-log.rocks/gossiping-bus-drivers-kata)

Given [n]{.italic} drivers, each with their own circular route of stops, determine how many steps are required until all gossip known to each bus driver is known by all. Drivers only gossip if they arrive together at the same stop.

So, let's say that Bob knows rumor X and drives route \[p,q,r\]. Jim knows rumor Y and drives route \[s,t,u,p\]. When will Bob and Jim be able to share their gossip? If they start at time 0, then at time 3 they will both be at stop p; remember, the routes are circular.

The process is limited to 480 steps.

This problem gets more interesting when there are more than two drivers and more complex routes.

[[[Java Solution]{.calibre_3}]{.bold}]{.calibre1}

I wrote a solution to this problem in Java. I started out with a very traditional kind of OO analysis and design (see [[[Figure 8.1]{.underline}]{.calibre_10}](#index_split_021.html#filepos229609)).

![](images/00056.jpg){#filepos229609 .calibre_35}

[[Figure 8.1.]{.bold}]{.calibre3}[ Simple object model for the Java version]{.calibre3}

The Simulator holds many Drivers. Each Driver has a Route, and each Route contains many Stops. Each Stop has many Drivers, and each Driver has many Rumors.

This is a fairly simple object model. There's not even any inheritance or polymorphism implied. So it should be a pretty straightforward implementation.

I wrote the Java code using TDD, of course. Here are the tests. As you can see, they are fairly wordy; but at least they all fit into a single test class:[]{#index_split_021.html#filepos230426}[[[[3]{.underline}]{.calibre_10}]{.calibre3}](#index_split_021.html#filepos230523).

[[[3]{.underline}]{.calibre_10}](#index_split_021.html#filepos230426). If you read my book [Clean Craftsmanship]{.italic} (Addison-Wesley, 2021), you'll understand why this is a good thing.

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_120.html#filepos968585)

> > [[`package gossipingBusDrivers;`{.calibre4}\
> > \
> > `import org.junit.Before;`{.calibre4}\
> > `import org.junit.Test;`{.calibre4}\
> > \
> > `import static org.hamcrest.MatcherAssert.assertThat;`{.calibre4}\
> > `import static org.hamcrest.collection.IsEmptyCollection.empty;`{.calibre4}\
> > \
> > `import static org.hamcrest.collection.`{.calibre4}\
> > `  IsIterableContainingInAnyOrder.containsInAnyOrder;`{.calibre4}\
> > `import static org.junit.Assert.assertEquals;`{.calibre4}\
> > \
> > `public class GossipTest {`{.calibre4}\
> > `  private Stop stop1;`{.calibre4}\
> > `  private Stop stop2;`{.calibre4}\
> > `  private Stop stop3;`{.calibre4}\
> > `  private Route route1;`{.calibre4}\
> > `  private Route route2;`{.calibre4}\
> > `  private Rumor rumor1;`{.calibre4}\
> > `  private Rumor rumor2;`{.calibre4}\
> > `  private Rumor rumor3;`{.calibre4}\
> > `  private Driver driver1;`{.calibre4}\
> > `  private Driver driver2;`{.calibre4}\
> > \
> > `  @Before`{.calibre4}\
> > `  public void setUp() {`{.calibre4}\
> > `    stop1 = new Stop("stop1");`{.calibre4}\
> > `    stop2 = new Stop("stop2");`{.calibre4}\
> > `    stop3 = new Stop("stop3");`{.calibre4}\
> > `    route1 = new Route(stop1, stop2);`{.calibre4}\
> > `    route2 = new Route(stop1, stop2, stop3);`{.calibre4}\
> > `    rumor1 = new Rumor("Rumor1");`{.calibre4}\
> > `    rumor2 = new Rumor("Rumor2");`{.calibre4}\
> > `    rumor3 = new Rumor("Rumor3");`{.calibre4}\
> > `    driver1 = new Driver("Driver1", route1, rumor1);`{.calibre4}\
> > `    driver2 = new Driver("Driver2", route2, rumor2, rumor3);`{.calibre4}\
> > `  }`{.calibre4}\
> > \
> > `  @Test`{.calibre4}\
> > `  public void driverStartsAtFirstStopInRoute() throws Exception {`{.calibre4}\
> > `    assertEquals(stop1, driver1.getStop());`{.calibre4}\
> > `  }`{.calibre4}\
> > \
> > `  @Test`{.calibre4}\
> > `  public void driverDrivesToNextStop() throws Exception {`{.calibre4}\
> > `    driver1.drive();`{.calibre4}\
> > `    assertEquals(stop2, driver1.getStop());`{.calibre4}\
> > `  }`{.calibre4}\
> > \
> > `  @Test`{.calibre4}\
> > `  public void driverReturnsToStartAfterLastStop()`{.calibre4}\
> > `  throws Exception {`{.calibre4}\
> > `    driver1.drive();`{.calibre4}\
> > `    driver1.drive();`{.calibre4}\
> > `    assertEquals(stop1, driver1.getStop());`{.calibre4}\
> > `  }`{.calibre4}\
> > \
> > `  @Test`{.calibre4}\
> > `  public void firstStopHasDriversAtStart() throws Exception {`{.calibre4}\
> > `    assertThat(stop1.getDrivers(), containsInAnyOrder(driver1,`{.calibre4}\
> > `                                                      driver2));`{.calibre4}\
> > `    assertThat(stop2.getDrivers(), empty());`{.calibre4}\
> > `  }`{.calibre4}\
> > \
> > `  @Test`{.calibre4}\
> > `  public void multipleDriversEnterAndLeaveStops()`{.calibre4}\
> > `  throws Exception {`{.calibre4}\
> > `    assertThat(stop1.getDrivers(), containsInAnyOrder(driver1,`{.calibre4}\
> > `                                                      driver2));`{.calibre4}\
> > `    assertThat(stop2.getDrivers(), empty());`{.calibre4}\
> > `    assertThat(stop3.getDrivers(), empty());`{.calibre4}\
> > `    driver1.drive();`{.calibre4}\
> > `    driver2.drive();`{.calibre4}\
> > `    assertThat(stop1.getDrivers(), empty());`{.calibre4}\
> > `    assertThat(stop2.getDrivers(), containsInAnyOrder(driver1,`{.calibre4}\
> > `                                                      driver2));`{.calibre4}\
> > `    assertThat(stop3.getDrivers(), empty());`{.calibre4}\
> > `    driver1.drive();`{.calibre4}\
> > `    driver2.drive();`{.calibre4}\
> > `    assertThat(stop1.getDrivers(), containsInAnyOrder(driver1));`{.calibre4}\
> > `    assertThat(stop2.getDrivers(), empty());`{.calibre4}\
> > `    assertThat(stop3.getDrivers(), containsInAnyOrder(driver2));`{.calibre4}\
> > `    driver1.drive();`{.calibre4}\
> > `    driver2.drive();`{.calibre4}\
> > `    assertThat(stop1.getDrivers(), containsInAnyOrder(driver2));`{.calibre4}\
> > `    assertThat(stop2.getDrivers(), containsInAnyOrder(driver1));`{.calibre4}\
> > `    assertThat(stop3.getDrivers(), empty());`{.calibre4}\
> > `  }`{.calibre4}\
> > \
> > `  @Test`{.calibre4}\
> > `  public void driversHaveRumorsAtStart() throws Exception {`{.calibre4}\
> > `    assertThat(driver1.getRumors(), containsInAnyOrder(rumor1));`{.calibre4}\
> > `    assertThat(driver2.getRumors(), containsInAnyOrder(rumor2,`{.calibre4}\
> > `                                                       rumor3));`{.calibre4}\
> > `  }`{.calibre4}\
> > \
> > `  @Test`{.calibre4}\
> > `  public void noDriversGossipAtEmptyStop() throws Exception {`{.calibre4}\
> > `    stop2.gossip();`{.calibre4}\
> > `    assertThat(driver1.getRumors(), containsInAnyOrder(rumor1));`{.calibre4}\
> > `    assertThat(driver2.getRumors(), containsInAnyOrder(rumor2,`{.calibre4}\
> > `                                                       rumor3));`{.calibre4}\
> > `  }`{.calibre4}\
> > \
> > `  @Test`{.calibre4}\
> > `  public void driversGossipAtStop() throws Exception {`{.calibre4}\
> > `    stop1.gossip();`{.calibre4}\
> > `    assertThat(driver1.getRumors(), containsInAnyOrder(rumor1,`{.calibre4}\
> > `                                                       rumor2,`{.calibre4}\
> > `                                                       rumor3));`{.calibre4}\
> > \
> > `    assertThat(driver2.getRumors(), containsInAnyOrder(rumor1,`{.calibre4}\
> > `                                                       rumor2,`{.calibre4}\
> > `                                                       rumor3));`{.calibre4}\
> > `  }`{.calibre4}\
> > \
> > `  @Test`{.calibre4}\
> > `  public void gossipIsNotDuplicated() throws Exception {`{.calibre4}\
> > `    stop1.gossip();`{.calibre4}\
> > `    stop1.gossip();`{.calibre4}\
> > `    assertThat(driver1.getRumors(), containsInAnyOrder(rumor1,`{.calibre4}\
> > `                                                       rumor2,`{.calibre4}\
> > `                                                       rumor3));`{.calibre4}\
> > \
> > `    assertThat(driver2.getRumors(), containsInAnyOrder(rumor1,`{.calibre4}\
> > `                                                       rumor2,`{.calibre4}\
> > `                                                       rumor3));`{.calibre4}\
> > `  }`{.calibre4}\
> > \
> > `  @Test`{.calibre4}\
> > `  public void driveTillEqualTest() throws Exception {`{.calibre4}\
> > `    assertEquals(1, Simulation.driveTillEqual(driver1,`{.calibre4}\
> > `                                              driver2));`{.calibre4}\
> > `  }`{.calibre4}\
> > \
> > `  @Test`{.calibre4}\
> > `  public void acceptanceTest1() throws Exception {`{.calibre4}\
> > `    Stop s1 = new Stop("s1");`{.calibre4}\
> > `    Stop s2 = new Stop("s2");`{.calibre4}\
> > `    Stop s3 = new Stop("s3");`{.calibre4}\
> > `    Stop s4 = new Stop("s4");`{.calibre4}\
> > `    Stop s5 = new Stop("s5");`{.calibre4}\
> > `    Route r1 = new Route(s3, s1, s2, s3);`{.calibre4}\
> > `    Route r2 = new Route(s3, s2, s3, s1);`{.calibre4}\
> > `    Route r3 = new Route(s4, s2, s3, s4, s5);`{.calibre4}\
> > `    Driver d1 = new Driver("d1", r1, new Rumor("1"));`{.calibre4}\
> > `    Driver d2 = new Driver("d2", r2, new Rumor("2"));`{.calibre4}\
> > `    Driver d3 = new Driver("d3", r3, new Rumor("3"));`{.calibre4}\
> > `    assertEquals(6, Simulation.driveTillEqual(d1, d2, d3));`{.calibre4}\
> > `  }`{.calibre4}\
> > \
> > `  @Test`{.calibre4}\
> > `  public void acceptanceTest2() throws Exception {`{.calibre4}\
> > `    Stop s1 = new Stop("s1");`{.calibre4}\
> > `    Stop s2 = new Stop("s2");`{.calibre4}\
> > `    Stop s5 = new Stop("s5");`{.calibre4}\
> > `    Stop s8 = new Stop("s8");`{.calibre4}\
> > `    Route r1 = new Route(s2, s1, s2);`{.calibre4}\
> > `    Route r2 = new Route(s5, s2, s8);`{.calibre4}\
> > `    Driver d1 = new Driver("d1", r1, new Rumor("1"));`{.calibre4}\
> > `    Driver d2 = new Driver("d2", r2, new Rumor("2"));`{.calibre4}\
> > `    assertEquals(480, Simulation.driveTillEqual(d1, d2));`{.calibre4}\
> > `  }`{.calibre4}\
> > `}`{.calibre4}]{.calibre_3}]{.calibre_17}

The solution code is broken up into several small files.

[[Driver]{.calibre_3}]{.bold}

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_125.html#filepos969315)

> > [[`package gossipingBusDrivers;`{.calibre4}\
> > \
> > `import java.util.Arrays;`{.calibre4}\
> > `import java.util.HashSet;`{.calibre4}\
> > `import java.util.Set;`{.calibre4}\
> > \
> > `public class Driver {`{.calibre4}\
> > `  private String name;`{.calibre4}\
> > `  private Route route;`{.calibre4}\
> > `  private int stopNumber = 0;`{.calibre4}\
> > `  private Set<Rumor> rumors;`{.calibre4}\
> > \
> > `  public Driver(String name, Route theRoute,`{.calibre4}\
> > `                Rumor... theRumors) {`{.calibre4}\
> > `    this.name = name;`{.calibre4}\
> > `    route = theRoute;`{.calibre4}\
> > `    rumors = new HashSet<>(Arrays.asList(theRumors));`{.calibre4}\
> > `    route.stopAt(this, stopNumber);`{.calibre4}\
> > `  }`{.calibre4}\
> > \
> > `  public Stop getStop() {`{.calibre4}\
> > `    return route.get(stopNumber);`{.calibre4}\
> > `  }`{.calibre4}\
> > \
> > `  public void drive() {`{.calibre4}\
> > `    route.leave(this, stopNumber);`{.calibre4}\
> > `    stopNumber = route.getNextStop(stopNumber);`{.calibre4}\
> > `    route.stopAt(this, stopNumber);`{.calibre4}\
> > `  }`{.calibre4}\
> > \
> > `  public Set<Rumor> getRumors() {`{.calibre4}\
> > `    return rumors;`{.calibre4}\
> > `  }`{.calibre4}\
> > \
> > `  public void addRumors(Set<Rumor> newRumors) {`{.calibre4}\
> > `    rumors.addAll(newRumors);`{.calibre4}\
> > `  }`{.calibre4}\
> > `}`{.calibre4}]{.calibre_3}]{.calibre_17}

[[Route]{.calibre_3}]{.bold}

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_126.html#filepos969461)

> > [[`package gossipingBusDrivers;`{.calibre4}\
> > \
> > `public class Route {`{.calibre4}\
> > `  private Stop[] stops;`{.calibre4}\
> > \
> > `  public Route(Stop... stops) {`{.calibre4}\
> > `    this.stops = stops;`{.calibre4}\
> > `  }`{.calibre4}\
> > \
> > `  public Stop get(int stopNumber) {`{.calibre4}\
> > `    return stops[stopNumber];`{.calibre4}\
> > `  }`{.calibre4}\
> > \
> > `  public int getNextStop(int stopNumber) {`{.calibre4}\
> > `    return (stopNumber + 1) % stops.length;`{.calibre4}\
> > `  }`{.calibre4}\
> > \
> > `  public void stopAt(Driver driver, int stopNumber) {`{.calibre4}\
> > `    stops[stopNumber].addDriver(driver);`{.calibre4}\
> > `  }`{.calibre4}\
> > \
> > `  public void leave(Driver driver, int stopNumber) {`{.calibre4}\
> > `    stops[stopNumber].removeDriver(driver);`{.calibre4}\
> > `  }`{.calibre4}\
> > `}`{.calibre4}]{.calibre_3}]{.calibre_17}

[[Stop]{.calibre_3}]{.bold}

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_127.html#filepos969607)

> > [[`package gossipingBusDrivers;`{.calibre4}\
> > \
> > `import java.util.ArrayList;`{.calibre4}\
> > `import java.util.HashSet;`{.calibre4}\
> > `import java.util.List;`{.calibre4}\
> > `import java.util.Set;`{.calibre4}\
> > \
> > `public class Stop {`{.calibre4}\
> > `  private String name;`{.calibre4}\
> > `  private List<Driver> drivers = new ArrayList<>();`{.calibre4}\
> > \
> > `  public Stop(String name) {`{.calibre4}\
> > `    this.name = name;`{.calibre4}\
> > `  }`{.calibre4}\
> > \
> > `  public String toString() {`{.calibre4}\
> > `    return name;`{.calibre4}\
> > `  }`{.calibre4}\
> > \
> > `  public List<Driver> getDrivers() {`{.calibre4}\
> > `    return drivers;`{.calibre4}\
> > `  }`{.calibre4}\
> > \
> > `  public void addDriver(Driver driver) {`{.calibre4}\
> > `    drivers.add(driver);`{.calibre4}\
> > `  }`{.calibre4}\
> > \
> > `  public void removeDriver(Driver driver) {`{.calibre4}\
> > `    drivers.remove(driver);`{.calibre4}\
> > `  }`{.calibre4}\
> > \
> > `  public void gossip() {`{.calibre4}\
> > `    Set<Rumor> rumorsAtStop = new HashSet<>();`{.calibre4}\
> > `    for (Driver d : drivers)`{.calibre4}\
> > `      rumorsAtStop.addAll(d.getRumors());`{.calibre4}\
> > `    for (Driver d : drivers)`{.calibre4}\
> > `      d.addRumors(rumorsAtStop);`{.calibre4}\
> > `  }`{.calibre4}\
> > `}`{.calibre4}]{.calibre_3}]{.calibre_17}

[[Rumor]{.calibre_3}]{.bold}

> > [[`package gossipingBusDrivers;`{.calibre4}\
> > \
> > `public class Rumor {`{.calibre4}\
> > `  private String name;`{.calibre4}\
> > `  public Rumor(String name) {`{.calibre4}\
> > `    this.name = name;`{.calibre4}\
> > `  }`{.calibre4}\
> > \
> > `  public String toString() {`{.calibre4}\
> > `    return name;`{.calibre4}\
> > `  }`{.calibre4}\
> > `}`{.calibre4}]{.calibre_3}]{.calibre_17}

[[Simulation]{.calibre_3}]{.bold}

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_128.html#filepos969754)

> > [[`package gossipingBusDrivers;`{.calibre4}\
> > \
> > `import java.util.HashSet;`{.calibre4}\
> > `import java.util.Set;`{.calibre4}\
> > \
> > `public class Simulation {`{.calibre4}\
> > `  public static int driveTillEqual(Driver... drivers) {`{.calibre4}\
> > `    int time;`{.calibre4}\
> > `    for (time = 0; notAllRumors(drivers) && time < 480; time++)`{.calibre4}\
> > `      driveAndGossip(drivers);`{.calibre4}\
> > `    return time;`{.calibre4}\
> > `  }`{.calibre4}\
> > \
> > `  private static void driveAndGossip(Driver[] drivers) {`{.calibre4}\
> > `    Set<Stop> stops = new HashSet<>();`{.calibre4}\
> > `    for (Driver d : drivers) {`{.calibre4}\
> > `      d.drive();`{.calibre4}\
> > `      stops.add(d.getStop());`{.calibre4}\
> > `    }`{.calibre4}\
> > `    for (Stop stop : stops)`{.calibre4}\
> > `      stop.gossip();`{.calibre4}\
> > `  }`{.calibre4}\
> > \
> > `  private static boolean notAllRumors(Driver[] drivers) {`{.calibre4}\
> > `    Set<Rumor> rumors = new HashSet<>();`{.calibre4}\
> > `    for (Driver d : drivers)`{.calibre4}\
> > `      rumors.addAll(d.getRumors());`{.calibre4}\
> > `    for (Driver d : drivers) {`{.calibre4}\
> > `      if (!d.getRumors().equals(rumors))`{.calibre4}\
> > `        return true;`{.calibre4}\
> > `    }`{.calibre4}\
> > `    return false;`{.calibre4}\
> > `  }`{.calibre4}\
> > `}`{.calibre4}]{.calibre_3}]{.calibre_17}
>
> []{#index_split_021.html#filepos245883}

A quick perusal of this code will convince you that it is written in a very traditional OO style and that the objects encapsulate their own state relatively well.

[[[Clojure]{.calibre_3}]{.bold}]{.calibre1}

When writing the Clojure version I did not start out with a design sketch. Rather, I depended upon my TDD tests to help me with the design. The tests are as follows:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_129.html#filepos969900)

> > [[`(ns gossiping-bus-drivers-clojure.core-spec`{.calibre4}\
> > `  (:require [speclj.core :refer :all]`{.calibre4}\
> > `            [gossiping-bus-drivers-clojure.core :refer :all]))`{.calibre4}\
> > \
> > `(describe "gossiping bus drivers"`{.calibre4}\
> > `  (it "drives one bus at one stop"`{.calibre4}\
> > `    (let [driver (make-driver "d1" [:s1] #{:r1}`{.calibre4}]{.calibre_3}]{.calibre_17}[[[[4]{.underline}]{.calibre_10}]{.calibre3}](#index_split_021.html#filepos250724)[[`)`{.calibre4}\
> > `          world [driver]`{.calibre4}\
> > `          new-world (drive world)]`{.calibre4}\
> > `      (should= 1 (count new-world))`{.calibre4}\
> > `      (should= :s1 (-> new-world first :route first))))`{.calibre4}\
> > \
> > `  (it "drives one bus at two stops"`{.calibre4}\
> > `    (let [driver (make-driver "d1" [:s1 :s2] #{:r1})`{.calibre4}\
> > `          world [driver]`{.calibre4}\
> > `          new-world (drive world)]`{.calibre4}\
> > `      (should= 1 (count new-world))`{.calibre4}\
> > `      (should= :s2 (-> new-world first :route first))))`{.calibre4}\
> > \
> > `  (it "drives two buses at some stops"`{.calibre4}\
> > `    (let [d1 (make-driver "d1" [:s1 :s2] #{:r1})`{.calibre4}\
> > `          d2 (make-driver "d2" [:s1 :s3 :s2] #{:r2})`{.calibre4}\
> > `          world [d1 d2]`{.calibre4}\
> > `          new-1 (drive world)`{.calibre4}\
> > `          new-2 (drive new-1)]`{.calibre4}\
> > `      (should= 2 (count new-1))`{.calibre4}\
> > `      (should= :s2 (-> new-1 first :route first))`{.calibre4}\
> > `      (should= :s3 (-> new-1 second :route first))`{.calibre4}\
> > `      (should= 2 (count new-2))`{.calibre4}\
> > `      (should= :s1 (-> new-2 first :route first))`{.calibre4}\
> > `      (should= :s2 (-> new-2 second :route first))))`{.calibre4}\
> > \
> > `  (it "gets stops"`{.calibre4}\
> > `    (let [drivers #{{:name "d1" :route [:s1]}`{.calibre4}\
> > `                    {:name "d2" :route [:s1]}`{.calibre4}\
> > `                    {:name "d3" :route [:s2]}}]`{.calibre4}\
> > `      (should= {:s1 [{:name "d1" :route [:s1]}`{.calibre4}\
> > `                     {:name "d2" :route [:s1]}]`{.calibre4}\
> > `                :s2 [{:name "d3", :route [:s2]}]}`{.calibre4}\
> > `               (get-stops drivers)))`{.calibre4}\
> > `    )`{.calibre4}\
> > \
> > `  (it "merges rumors"`{.calibre4}\
> > `    (should= [{:name "d1" :rumors #{:r2 :r1}}`{.calibre4}\
> > `              {:name "d2" :rumors #{:r2 :r1}}]`{.calibre4}\
> > `             (merge-rumors [{:name "d1" :rumors #{:r1}}`{.calibre4}\
> > `                            {:name "d2" :rumors #{:r2}}])))`{.calibre4}\
> > \
> > \
> > `  (it "shares gossip when drivers are at same stop"`{.calibre4}\
> > `    (let [d1 (make-driver "d1" [:s1 :s2] #{:r1})`{.calibre4}\
> > `          d2 (make-driver "d2" [:s1 :s2] #{:r2})`{.calibre4}\
> > `          world [d1 d2]`{.calibre4}\
> > `          new-world (drive world)]`{.calibre4}\
> > `      (should= 2 (count new-world))`{.calibre4}\
> > `      (should= #{:r1 :r2} (-> new-world first :rumors))`{.calibre4}\
> > `      (should= #{:r1 :r2} (-> new-world second :rumors))))`{.calibre4}\
> > \
> > `  (it "passes acceptance test 1"`{.calibre4}\
> > `    (let [world [(make-driver "d1" [3 1 2 3] #{1})`{.calibre4}\
> > `                 (make-driver "d2" [3 2 3 1] #{2})`{.calibre4}\
> > `                 (make-driver "d3" [4 2 3 4 5] #{3})]]`{.calibre4}\
> > `      (should= 6 (drive-till-all-rumors-spread world))))`{.calibre4}\
> > \
> > `  (it "passes acceptance test 2"`{.calibre4}\
> > `    (let [world [(make-driver "d1" [2 1 2] #{1})`{.calibre4}\
> > `                 (make-driver "d2" [5 2 8] #{2})]]`{.calibre4}\
> > `          (should= :never (drive-till-all-rumors-spread world))))`{.calibre4}\
> > `  )`{.calibre4}]{.calibre_3}]{.calibre_17}
>
> []{#index_split_021.html#filepos250704}

[[[4]{.underline}]{.calibre_10}](#index_split_021.html#filepos250704). [` #{. . .} `{.calibre4}]{.calibre_17} represents a set in Clojure. A [set]{.italic} is a list of items that has no duplicates.

There are some interesting similarities between the Java tests and the Clojure tests. They are both quite wordy; although the Clojure tests contain half as many lines. The Java version has 12 tests whereas the Clojure version has only 8. This difference has a lot to do with the way the two different solutions were partitioned. The Clojure tests also play pretty fast and loose with the data.

Consider, for example, the [` "merges rumors" `{.calibre4}]{.calibre_17} test. The [` merge-rumors `{.calibre4}]{.calibre_17} function expects a list of drivers; however, the test does not create completely formed drivers. Rather, it creates abbreviated structures that look like drivers as far as the [` merge-rumors `{.calibre4}]{.calibre_17} function is concerned.

The solution is all contained in a single, very short file:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_132.html#filepos970338)

> > [[`(ns gossiping-bus-drivers-clojure.core`{.calibre4}\
> > `  (:require [clojure.set :as set]))`{.calibre4}\
> > \
> > `(defn make-driver [name route rumors]`{.calibre4}\
> > `  (assoc`{.calibre4}]{.calibre_3}]{.calibre_17}[[[[5]{.underline}]{.calibre_10}]{.calibre3}](#index_split_021.html#filepos254933)[[` {} :name name :route (cycle`{.calibre4}]{.calibre_3}]{.calibre_17}[[[[6]{.underline}]{.calibre_10}]{.calibre3}](#index_split_021.html#filepos255236)[[` route) :rumors rumors))`{.calibre4}\
> > \
> > `(defn move-driver [driver]`{.calibre4}\
> > `  (update`{.calibre4}]{.calibre_3}]{.calibre_17}[[[[7]{.underline}]{.calibre_10}]{.calibre3}](#index_split_021.html#filepos255625)[[` driver :route rest))`{.calibre4}\
> > \
> > `(defn move-drivers [world]`{.calibre4}\
> > `  (map move-driver world))`{.calibre4}\
> > \
> > `(defn get-stops [world]`{.calibre4}\
> > `  (loop [world world`{.calibre4}\
> > `         stops {}]`{.calibre4}\
> > `    (if (empty? world)`{.calibre4}\
> > `      stops`{.calibre4}\
> > `      (let [driver (first world)`{.calibre4}\
> > `            stop (first (:route driver))`{.calibre4}\
> > `            stops (update stops stop conj driver)]`{.calibre4}\
> > `        (recur (rest world) stops)))))`{.calibre4}\
> > \
> > `(defn merge-rumors [drivers]`{.calibre4}\
> > `  (let [rumors (map :rumors drivers)`{.calibre4}\
> > `        all-rumors (apply set/union`{.calibre4}]{.calibre_3}]{.calibre_17}[[[[8]{.underline}]{.calibre_10}]{.calibre3}](#index_split_021.html#filepos256356)[[` rumors)]`{.calibre4}\
> > `      (map #(assoc % :rumors all-rumors) drivers)))`{.calibre4}\
> > \
> > `(defn spread-rumors [world]`{.calibre4}\
> > `  (let [stops-with-drivers (get-stops world)`{.calibre4}\
> > `        drivers-by-stop (vals`{.calibre4}]{.calibre_3}]{.calibre_17}[[[[9]{.underline}]{.calibre_10}]{.calibre3}](#index_split_021.html#filepos256803)[[` stops-with-drivers)]`{.calibre4}\
> > `    (flatten`{.calibre4}]{.calibre_3}]{.calibre_17}[[[[10]{.underline}]{.calibre_10}]{.calibre3}](#index_split_021.html#filepos257094)[[` (map merge-rumors drivers-by-stop))))`{.calibre4}\
> > \
> > `(defn drive [world]`{.calibre4}\
> > `  (-> world move-drivers spread-rumors))`{.calibre4}\
> > \
> > `(defn drive-till-all-rumors-spread [world]`{.calibre4}\
> > `  (loop [world (drive world)`{.calibre4}\
> > `         time 1]`{.calibre4}\
> > `    (cond`{.calibre4}\
> > `      (> time 480) :never`{.calibre4}\
> > `      (apply = (map :rumors world)) time`{.calibre4}\
> > `      :else (recur (drive world) (inc time)))))`{.calibre4}]{.calibre_3}]{.calibre_17}
>
> []{#index_split_021.html#filepos254913}

[[[5]{.underline}]{.calibre_10}](#index_split_021.html#filepos254913). [` assoc `{.calibre4}]{.calibre_17} adds elements to a map. [` (assoc {} :a 1) `{.calibre4}]{.calibre_17} returns [` {:a 1} `{.calibre4}]{.calibre_17}.

[[[6]{.underline}]{.calibre_10}](#index_split_021.html#filepos254913). [` cycle `{.calibre4}]{.calibre_17} returns a lazy (and "infinite") list that simply repeats the input list endlessly. Thus, [` (cycle [1 2 3]) `{.calibre4}]{.calibre_17} returns [` [1 2 3 1 2 3 1 2 3 …] `{.calibre4}]{.calibre_17}.

[[[7]{.underline}]{.calibre_10}](#index_split_021.html#filepos254913). The [` update `{.calibre4}]{.calibre_17} function returns a new map with one element changed. [` (update m k f a) `{.calibre4}]{.calibre_17} changes the [` k `{.calibre4}]{.calibre_17} element of [` m `{.calibre4}]{.calibre_17} by applying the function [` (f e a) `{.calibre4}]{.calibre_17}, where [` e `{.calibre4}]{.calibre_17} is the old value of element [` k `{.calibre4}]{.calibre_17}. Thus, [` (update {:x 1} :x inc) `{.calibre4}]{.calibre_17} returns [` {:x 2} `{.calibre4}]{.calibre_17}.

[[[8]{.underline}]{.calibre_10}](#index_split_021.html#filepos254913). The [` union `{.calibre4}]{.calibre_17} function is from the [` set `{.calibre4}]{.calibre_17} namespace. Notice the [` ns `{.calibre4}]{.calibre_17} at the top aliases the [` clojure.set `{.calibre4}]{.calibre_17} namespace to just [` set `{.calibre4}]{.calibre_17}.

[[[9]{.underline}]{.calibre_10}](#index_split_021.html#filepos254913). [` vals `{.calibre4}]{.calibre_17} returns a list of all the values in a map. [` keys `{.calibre4}]{.calibre_17} returns a list of all the keys in a map.

[[[10]{.underline}]{.calibre_10}](#index_split_021.html#filepos254913). The [` flatten `{.calibre4}]{.calibre_17} function turns a list of lists into a list of all the elements. So [` (flatten [[1 2][3 4]]) `{.calibre4}]{.calibre_17} returns [` [1 2 3 4] `{.calibre4}]{.calibre_17}.

This solution is 42 lines, whereas the Java solution is 145 lines spread among five files.

Both solutions have the concept of a Driver, but I made no attempt to encapsulate the concepts of Route, Stop, and Rumor into independent objects. They all just happily live within the Driver.

Worse, the Driver "object" is not an object in the traditional OO sense. It has no methods. There is one method in the system, [` move-driver `{.calibre4}]{.calibre_17}, that operates on a single Driver, but it's just a little helper function for the more interesting [` move-drivers `{.calibre4}]{.calibre_17} function.

Six out of the eight functions take only the [` world `{.calibre4}]{.calibre_17} as an argument. Thus, we might say that the only true object in this system is the [` world `{.calibre4}]{.calibre_17}, and it has five methods. But even that is a stretch.

Even if we decide that the Driver is a kind of object, it is not mutable. The simulated [` world `{.calibre4}]{.calibre_17} is nothing more than a list of immutable Drivers. The [` drive `{.calibre4}]{.calibre_17} function accepts the [` world `{.calibre4}]{.calibre_17} and produces a new [` world `{.calibre4}]{.calibre_17} in which all the Drivers have been moved one step, and Rumors have been spread at any stop where more than one Driver has arrived.

That [` drive `{.calibre4}]{.calibre_17} function is an example of an important concept. Notice how the [` world `{.calibre4}]{.calibre_17} passes through a pipeline of functions. In this case there are only two, [` move-drivers `{.calibre4}]{.calibre_17} and [` spread-rumors `{.calibre4}]{.calibre_17}, but in larger systems the pipeline can be quite long. At each stage along that pipeline the [` world `{.calibre4}]{.calibre_17} is modified into a slightly new form.

This tells us that the partitioning of this system is not about objects, but about functions. The relatively unpartitioned data passes from one independent function to the next.

You might argue that the Java code is relatively straightforward, whereas the Clojure code is too dense and obscure. Believe me when I say that it does not take very long to get comfortable with that density and that the perceived obscuration is an illusion based on unfamiliarity.

Is the lack of partitioning in the Clojure version a problem? Not at its current size; but if this program were to grow the way most systems grow, that problem would assert itself with a vengeance. Partitioning OO programs is a bit more natural than partitioning functional programs because the dividing lines are much more obvious and pronounced.

On the other hand, the dividing lines we chose for the Java version are not guaranteed to lead to an [effective]{.italic} partitioning. The warning is in the [` drive `{.calibre4}]{.calibre_17} function of the Clojure program. It seems likely that a better partitioning of this system might lie along the different operations that manipulate the world, rather than things like Routes, Stops, and Rumors.

[[[Conclusion]{.calibre_3}]{.bold}]{.calibre1}

We saw some differences in the Prime Factors and Bowling Game katas; but the differences were relatively minor. The differences in the Gossiping Bus Drivers kata were much more pronounced. This is likely because that last kata was a bit larger than the first two (I'd say twice the size), and also because it was a true finite state machine.

A [finite state machine]{.italic} moves from state to state, taking actions that depend upon the incoming events and the current state. When such systems are written in an OO style, the state tends to be stored in mutable objects that have dedicated methods. But in a functional style, the state remains []{#index_split_021.html#filepos261948}externalized in immutable data structures that are passed through pipelines of functions.

We can perhaps conclude from this that programs that do simple calculations, like Prime Factors, are little affected by the OO or functional style. They are, after all, simple functions without any change of state. Programs in which state change is restricted to minor issues, such as array indexing, are only slightly affected by the difference in style. But those programs that are driven by changes of state from one moment to the next, like the Gossiping Bus Drivers program, will see profound differences between the two styles.

The OO style leads to a partitioning that is strongly related to data cohesion, whereas the functional style leads to a partitioning that is strongly related to behavioral cohesion. Which of these two is better is a question that I will leave for subsequent chapters.

::: {#index_split_021.html#calibre_pb_21 .mbp_pagebreak}
:::

[]{#index_split_022.html}

[[[9]{.calibre_3}]{.bold}]{.calibre1}

[[[Object-Oriented Programming]{.calibre_3}]{.bold}]{.calibre1}

![](images/00228.jpg){.calibre_36}

In the preceding chapter, we saw that the OO style of programming is strongly related to data types and the cohesion of data. But that's not all there is to object orientation. Indeed, data cohesion may be secondary to another attribute of object orientation: polymorphism.

In [Clean Architecture]{.italic},[]{#index_split_022.html#filepos263698}[[[[1]{.underline}]{.calibre_10}]{.calibre3}](#index_split_022.html#filepos264030) I made the point that the OO style has three attributes: encapsulation, inheritance, and polymorphism. I then led you through the reasoning that, of the three, polymorphism is the most beneficial. The other two are, at best, ancillary.

[[[1]{.underline}]{.calibre_10}](#index_split_022.html#filepos263698). Robert C. Martin, [Clean Architecture]{.italic} (Pearson, 2017).

The examples in the previous chapters did not lend themselves to any polymorphism. Let's correct that by examining how we might solve the Payroll problem from Section 3 of [Agile Software Development: Principles, Patterns, and Practices]{.italic}.[]{#index_split_022.html#filepos264486}[[[[2]{.underline}]{.calibre_10}]{.calibre3}](#index_split_022.html#filepos264582)

[[[2]{.underline}]{.calibre_10}](#index_split_022.html#filepos264486). Robert C Martin, [Agile Software Development: Principles, Patterns, and Practices]{.italic} (Pearson, 2002).

The requirements are as follows.

::: calibre_11
 
:::

-   There is a database of employee records.

-   The payroll program runs daily, generating payments for those employees who should be paid on that day.

-   Salaried employees are paid on the last business day of the month. Their monthly salary is a field in their employee record.

-   Commissioned employees are paid every other Friday. They are paid a base salary plus commission. The base salary and the commission rate are fields in their employee record. Commission is calculated by multiplying the commission rate by the total of the sales receipts for that employee.

-   Hourly employees are paid every Friday. Their hourly rate is a field in their employee record. Their pay is calculated by multiplying their hourly rate by the sum of the hours on their timecards for the week. If that sum is greater than 40, the remaining hours are paid at 1.5 times their hourly rate.

-   Employees are given the option to have their paychecks mailed to their home address, held at their paymaster's office, or directly deposited into their bank account. The address, paymaster, and bank information are fields in their employee record.

The typical OO solution to this problem is shown in the unified modeling language (UML) diagram in [[[Figure 9.1]{.underline}]{.calibre_10}](#index_split_022.html#filepos267011).

![](images/00144.jpg){#filepos267011 .calibre_37}

[[Figure 9.1.]{.bold}]{.calibre3}[ Object model for the Payroll problem]{.calibre3}

Perhaps the best place to begin is with the [` Payroll `{.calibre4}]{.calibre_17} class. In Java, it has a [` run `{.calibre4}]{.calibre_17} method that looks like this:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_133.html#filepos970469)

> > [[`void run() {`{.calibre4}\
> > `  for (Employee e : db.getEmployees()) {`{.calibre4}\
> > `    if (e.isPayDay()) {`{.calibre4}\
> > `      Pay pay = e.calcPay();`{.calibre4}\
> > `      e.sendPay(pay);`{.calibre4}\
> > `    }`{.calibre4}\
> > `  }`{.calibre4}\
> > `}`{.calibre4}]{.calibre_3}]{.calibre_17}
>
> []{#index_split_022.html#filepos267992}

I have made the point many times, and in many places, including the aforementioned books, that this little snippet of code is the [pure truth]{.italic}. For each employee, if today is the day they should be paid, then calculate their pay and send it to them.

From that little snippet of code, the rest of the implementation ought to be pretty clear. There are three uses of the [Strategy]{.italic}[]{#index_split_022.html#filepos268487}[[[[3]{.underline}]{.calibre_10}]{.calibre3}](#index_split_022.html#filepos268816) pattern: one to implement [` calcPay `{.calibre4}]{.calibre_17}, another to implement [` isPayDay `{.calibre4}]{.calibre_17}, and the last to implement [` sendPay `{.calibre4}]{.calibre_17}.

[[[3]{.underline}]{.calibre_10}](#index_split_022.html#filepos268487). Erich Gamma, Richard Helm, Ralph Johnson, and John Vlissides, [Design Patterns: Elements of Reusable Object-Oriented Software]{.italic} (Addison-Wesley, 1995), 315.

It should also be clear that this structure of objects must be built up by the [` getEmployees `{.calibre4}]{.calibre_17} function, which reads the employees from the database and arranges them properly. It is unlikely that the data in the database looks like the object structure seen here.

There is also a very clear architectural boundary (dashed line) that cuts across all those inheritance relationships, dividing the high-level abstractions from the low-level details.

[[[Functional Payroll]{.calibre_3}]{.bold}]{.calibre1}

[[[Figure 9.2]{.underline}]{.calibre_10}](#index_split_022.html#filepos270004) shows what this might look like as a functional program.

![](images/00103.jpg){#filepos270004 .calibre_38}

[[Figure 9.2.]{.bold}]{.calibre3}[ Data flow diagram of the Payroll problem]{.calibre3}

Isn't it interesting that I chose a data flow diagram (DFD) to represent the functional solution? DFDs are very helpful in depicting the relationships between processes and data elements, but they are not nearly as helpful as UML class diagrams when it comes to depicting architectural decisions.

Still, the DFD helps us propose the functional version of the [pure truth]{.italic}:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_134.html#filepos970615)

> > [[`(defn payroll [today db]`{.calibre4}\
> > `  (let [employees (get-employees db)`{.calibre4}\
> > `        employees-to-pay (get-employees-to-be-paid-today`{.calibre4}\
> > `                            today employees)`{.calibre4}\
> > `        amounts (get-paycheck-amounts employees-to-pay)`{.calibre4}\
> > `        ids (get-ids employees-to-pay)`{.calibre4}\
> > `        dispositions (get-dispositions employees-to-pay)]`{.calibre4}\
> > `    (send-paychecks ids amounts dispositions)))`{.calibre4}]{.calibre_3}]{.calibre_17}

Notice that this differs from the Java version in that it is not an iterative approach. Rather, the list of employees flows through the program, getting modified at each stage according to the data flow diagram. This is typical of the way functional programs are conceived and written. Functional programs tend to be more like [plumbing]{.italic} than step-by-step procedures. They regulate and modify the flow of data, rather than iterating step by step through the data.

So, what about the architecture? There was that nice architectural boundary in the UML diagram of the OO version. Where is the architectural boundary in the functional version?

Let's look a bit deeper. The tests may give us some hints:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_135.html#filepos970761)

> > [[`(it "pays one salaried employee at end of month by mail"`{.calibre4}\
> > `  (let [employees [{:id "emp1"`{.calibre4}\
> > `                    :schedule :monthly`{.calibre4}\
> > `                    :pay-class [:salaried 5000]`{.calibre4}\
> > `                    :disposition [:mail "name" "home"]}]`{.calibre4}\
> > `        db {:employees employees}`{.calibre4}\
> > `        today (parse-date "Nov 30 2021")]`{.calibre4}\
> > `    (should= [{:type :mail`{.calibre4}\
> > `               :id "emp1"`{.calibre4}\
> > `               :name "name"`{.calibre4}\
> > `               :address "home"`{.calibre4}\
> > `               :amount 5000}]`{.calibre4}\
> > `             (payroll today db))))`{.calibre4}]{.calibre_3}]{.calibre_17}

In this test, the database contains a list of [` employee `{.calibre4}]{.calibre_17}s, and each [` employee `{.calibre4}]{.calibre_17} is a hash map with specific fields. That's not so different from an object, is it? The [` payroll `{.calibre4}]{.calibre_17} function returns a list of paycheck directives, each of which is also a hash map---another object. Interesting.

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_136.html#filepos970907)

> > [[`(it "pays one hourly employee on Friday by Direct Deposit"`{.calibre4}\
> > `  (let [employees [{:id "empid"`{.calibre4}\
> > `                    :schedule :weekly`{.calibre4}\
> > `                    :pay-class [:hourly 15]`{.calibre4}\
> > `                    :disposition [:deposit "routing" "account"]}]`{.calibre4}\
> > `        time-cards {"empid" [["Nov 12 2022" 80/10`{.calibre4}]{.calibre_3}]{.calibre_17}[[[[4]{.underline}]{.calibre_10}]{.calibre3}](#index_split_022.html#filepos275223)[[`]]}`{.calibre4}\
> > `        db {:employees employees :time-cards time-cards}`{.calibre4}\
> > `        friday (parse-date "Nov 18 2022")]`{.calibre4}\
> > `    (should= [{:type :deposit`{.calibre4}\
> > `               :id "empid"`{.calibre4}\
> > `               :routing "routing"`{.calibre4}\
> > `               :account "account"`{.calibre4}\
> > `               :amount 120}]`{.calibre4}\
> > `             (payroll friday db))))`{.calibre4}]{.calibre_3}]{.calibre_17}
>
> []{#index_split_022.html#filepos275203}

[[[4]{.underline}]{.calibre_10}](#index_split_022.html#filepos275203). This is not 80 divided by 10. Rather, it is the rational number 80/10. This ensures that subsequent mathematics will not treat the value as an integer.

This test shows how the [` employee `{.calibre4}]{.calibre_17} and [` paycheck-directive `{.calibre4}]{.calibre_17} objects vary based upon the [` :schedule `{.calibre4}]{.calibre_17}, [` :pay-class `{.calibre4}]{.calibre_17}, and [` :disposition `{.calibre4}]{.calibre_17}. It also shows that the database contains [` time-card `{.calibre4}]{.calibre_17}s associated with employee [` id `{.calibre4}]{.calibre_17}s. From this, the third test ought to be predictable:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_137.html#filepos971053)

> > [[`(it "pays one commissioned employee on an even Friday by Paymaster"`{.calibre4}\
> > `  (let [employees [{:id "empid"`{.calibre4}\
> > `                    :schedule :biweekly`{.calibre4}\
> > `                    :pay-class [:commissioned 100 5/100]`{.calibre4}\
> > `                    :disposition [:paymaster "paymaster"]}]`{.calibre4}\
> > `        sales-receipts {"empid" [["Nov 12 2022" 15000]]}`{.calibre4}\
> > `        db {:employees employees :sales-receipts sales-receipts}`{.calibre4}\
> > `        friday (parse-date "Nov 18 2022")]`{.calibre4}\
> > `    (should= [{:type :paymaster`{.calibre4}\
> > `               :id "empid"`{.calibre4}\
> > `               :paymaster "paymaster"`{.calibre4}\
> > `               :amount 850}]`{.calibre4}\
> > `             (payroll friday db))))`{.calibre4}]{.calibre_3}]{.calibre_17}

Notice that the payments are being properly calculated, the dispositions are being correctly interpreted, and---as far as we can tell---the schedules are being followed. So how is this all being accomplished?

Here's the key to it all:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_138.html#filepos971199)

> > [[`(defn get-pay-class [employee]`{.calibre4}\
> > `  (first (:pay-class employee)))`{.calibre4}\
> > \
> > `(defn get-disposition [paycheck-directive]`{.calibre4}\
> > `  (first (:disposition paycheck-directive)))`{.calibre4}\
> > \
> > ]{.calibre_3}]{.calibre_17}[[`(defmulti is-today-payday :schedule)`{.calibre4}]{.calibre_3}]{.bold}[[\
> > ]{.calibre_3}]{.calibre_17}[[`(defmulti calc-pay get-pay-class)`{.calibre4}]{.calibre_3}]{.bold}[[\
> > ]{.calibre_3}]{.calibre_17}[[`(defmulti dispose get-disposition)`{.calibre4}]{.calibre_3}]{.bold}[[\
> > \
> > `(defn get-employees-to-be-paid-today [today employees]`{.calibre4}\
> > `  (filter`{.calibre4}]{.calibre_3}]{.calibre_17}[[[[5]{.underline}]{.calibre_10}]{.calibre3}](#index_split_022.html#filepos280110)[[` #(is-today-payday % today) employees))`{.calibre4}\
> > \
> > `(defn- build-employee [db employee]`{.calibre4}\
> > `  (assoc employee :db db))`{.calibre4}\
> > \
> > `(defn get-employees [db]`{.calibre4}\
> > `  (map (partial`{.calibre4}]{.calibre_3}]{.calibre_17}[[[[6]{.underline}]{.calibre_10}]{.calibre3}](#index_split_022.html#filepos280545)[[` build-employee db) (:employees db)))`{.calibre4}\
> > \
> > `(defn create-paycheck-directives [ids payments dispositions]`{.calibre4}\
> > `  (map #(assoc {} :id %1 :amount %2 :disposition %3)`{.calibre4}\
> > `       ids payments dispositions))`{.calibre4}\
> > \
> > `(defn send-paychecks [ids payments dispositions]`{.calibre4}\
> > `  (for`{.calibre4}]{.calibre_3}]{.calibre_17}[[[[7]{.underline}]{.calibre_10}]{.calibre3}](#index_split_022.html#filepos280981)[[` [paycheck-directive`{.calibre4}\
> > `        (create-paycheck-directives ids payments dispositions)]`{.calibre4}\
> > `    (dispose paycheck-directive)))`{.calibre4}\
> > \
> > `(defn get-paycheck-amounts [employees]`{.calibre4}\
> > `  (map calc-pay employees))`{.calibre4}\
> > \
> > `(defn get-dispositions [employees]`{.calibre4}\
> > `  (map :disposition employees))`{.calibre4}\
> > \
> > `(defn get-ids [employees]`{.calibre4}\
> > `  (map :id employees))`{.calibre4}]{.calibre_3}]{.calibre_17}
>
> []{#index_split_022.html#filepos280090}

[[[5]{.underline}]{.calibre_10}](#index_split_022.html#filepos280090). [` (filter predicate list) `{.calibre4}]{.calibre_17} calls [` predicate `{.calibre4}]{.calibre_17} for every member of [` list `{.calibre4}]{.calibre_17} and returns a sequence of all the members for which [` predicate `{.calibre4}]{.calibre_17} was not [falsey]{.italic}.

[[[6]{.underline}]{.calibre_10}](#index_split_022.html#filepos280090). The [` partial `{.calibre4}]{.calibre_17} function takes a function and some arguments, and returns a new function in which all those arguments have already been initialized. Thus, [` ((partial f 1) 2) `{.calibre4}]{.calibre_17} is equivalent to [` (f 1 2) `{.calibre4}]{.calibre_17}.

[[[7]{.underline}]{.calibre_10}](#index_split_022.html#filepos280090). In this case, the [` for `{.calibre4}]{.calibre_17} function calls [` dispose `{.calibre4}]{.calibre_17} for each [` paycheck-directive `{.calibre4}]{.calibre_17} in the list returned by [` create-paycheck-directives `{.calibre4}]{.calibre_17}.

Do you see those [` defmulti `{.calibre4}]{.calibre_17} statements (in bold)? They are analogous, though not identical, to a Java interface. Each [` defmulti `{.calibre4}]{.calibre_17} defines a polymorphic function. However, that function does not dispatch based upon an intrinsic type, the way Java or C# or even Ruby and Python do. Rather, they dispatch upon the result of the function specified right after the name.

So, the [` get-pay-class `{.calibre4}]{.calibre_17} function returns the value that the [` calc-pay `{.calibre4}]{.calibre_17} function will polymorphically dispatch on. What does [` get-pay-class `{.calibre4}]{.calibre_17} return? It returns the first element of the [` pay-class `{.calibre4}]{.calibre_17} field of the [` employee `{.calibre4}]{.calibre_17}. According to our tests, those values are [` :salaried `{.calibre4}]{.calibre_17}, [` :hourly `{.calibre4}]{.calibre_17}, and [` :commissioned `{.calibre4}]{.calibre_17}.

So where are the implementations of the [` calc-pay `{.calibre4}]{.calibre_17} functions? They are [further down]{.italic} in the program:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_139.html#filepos971345)

> > [[`(defn-`{.calibre4}]{.calibre_3}]{.calibre_17}[[[[8]{.underline}]{.calibre_10}]{.calibre3}](#index_split_022.html#filepos284683)[[` get-salary [employee]`{.calibre4}\
> > `  (second (:pay-class employee)))`{.calibre4}\
> > \
> > `(defmethod calc-pay :salaried [employee]`{.calibre4}\
> > `  (get-salary employee))`{.calibre4}\
> > \
> > `(defmethod calc-pay :hourly [employee]`{.calibre4}\
> > `  (let [db (:db employee)`{.calibre4}\
> > `        time-cards (:time-cards db)`{.calibre4}\
> > `        my-time-cards (get`{.calibre4}]{.calibre_3}]{.calibre_17}[[[[9]{.underline}]{.calibre_10}]{.calibre3}](#index_split_022.html#filepos284928)[[` time-cards (:id employee))`{.calibre4}\
> > `        [_ hourly-rate]`{.calibre4}]{.calibre_3}]{.calibre_17}[[[[10]{.underline}]{.calibre_10}]{.calibre3}](#index_split_022.html#filepos285216)[[` (:pay-class employee)`{.calibre4}\
> > `        hours (map second my-time-cards)`{.calibre4}\
> > `        total-hours (reduce + hours)]`{.calibre4}\
> > `    (* total-hours hourly-rate)))`{.calibre4}\
> > \
> > `(defmethod calc-pay :commissioned [employee]`{.calibre4}\
> > `  (let [db (:db employee)`{.calibre4}\
> > `        sales-receipts (:sales-receipts db)`{.calibre4}\
> > `        my-sales-receipts (get sales-receipts (:id employee))`{.calibre4}\
> > `        [_ base-pay commission-rate] (:pay-class employee)`{.calibre4}\
> > `        sales (map second my-sales-receipts)`{.calibre4}\
> > `        total-sales (reduce + sales)]`{.calibre4}\
> > `    (+ (* total-sales commission-rate) base-pay)))`{.calibre4}]{.calibre_3}]{.calibre_17}
>
> []{#index_split_022.html#filepos284663}

[[[8]{.underline}]{.calibre_10}](#index_split_022.html#filepos284663). The trailing [` - `{.calibre4}]{.calibre_17} makes this a private function, so only functions in this file can access it.

[[[9]{.underline}]{.calibre_10}](#index_split_022.html#filepos284663). [` (get m k) `{.calibre4}]{.calibre_17} returns the value of [` k `{.calibre4}]{.calibre_17} in the map [` m `{.calibre4}]{.calibre_17}.

[[[10]{.underline}]{.calibre_10}](#index_split_022.html#filepos284663). [Destructures]{.italic} the [` pay-class `{.calibre4}]{.calibre_17} of the [` employee `{.calibre4}]{.calibre_17} and ignores the first element.

I italicized the words [further down]{.italic} because that is significant in a Clojure program. Clojure programs cannot call functions that are declared below the point of call. But these functions [are]{.italic} declared below the point of call. That means there is a source code dependency inversion. The [` calc-pay `{.calibre4}]{.calibre_17} implementations are called by the [` payroll `{.calibre4}]{.calibre_17} function; but the [` payroll `{.calibre4}]{.calibre_17} function is above the [` calc-pay `{.calibre4}]{.calibre_17} implementations.

Indeed, I could move all the implementations of the [` defmulti `{.calibre4}]{.calibre_17} function to a different source file that the [` payroll `{.calibre4}]{.calibre_17} source file does not [` require `{.calibre4}]{.calibre_17}.

If we draw the relationships between those source files, we get the diagram in [[[Figure 9.3]{.underline}]{.calibre_10}](#index_split_022.html#filepos286703).

![](images/00162.jpg){#filepos286703 .calibre_39}

[[Figure 9.3.]{.bold}]{.calibre3}[ Dependency inversion]{.calibre3}

The arrows depict the [` requires `{.calibre4}]{.calibre_17} relationships between the source files. The source code of those [` requires `{.calibre4}]{.calibre_17} in the [` payroll-implementation.clj `{.calibre4}]{.calibre_17} file looks like this:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_140.html#filepos971491)

> > [[`(ns payroll-implementation`{.calibre4}\
> > `  (:require [payroll :refer [is-today-payday calc-pay dispose]]))`{.calibre4}]{.calibre_3}]{.calibre_17}

The source code dependency inversion should be obvious. The [` payroll `{.calibre4}]{.calibre_17} function in [` payroll.clj `{.calibre4}]{.calibre_17} calls the [` is-today-payday `{.calibre4}]{.calibre_17}, [` calc-pay `{.calibre4}]{.calibre_17}, and [` dispose `{.calibre4}]{.calibre_17} implementations in the [` payroll-implementation.clj `{.calibre4}]{.calibre_17} file, but the [` payroll.clj `{.calibre4}]{.calibre_17} file does not depend upon the [` payroll-implementation.clj `{.calibre4}]{.calibre_17} file. The dependency points the other way around.

What does all this inversion mean? It means that the low-level details in [` payroll-implementation.clj `{.calibre4}]{.calibre_17} depend upon the high-level policy in [` payroll.clj `{.calibre4}]{.calibre_17}. And whenever low-level details depend upon high-level policy, we have the potential for an architectural boundary. We could even draw it as shown in [[[Figure 9.4]{.underline}]{.calibre_10}](#index_split_022.html#filepos288922).

![](images/00251.jpg){#filepos288922 .calibre_40}

[[Figure 9.4.]{.bold}]{.calibre3}[ Architectural boundary]{.calibre3}

Notice that I used a UML implements arrow. It's almost as if [` Payroll `{.calibre4}]{.calibre_17} and [` PayrollImplementation `{.calibre4}]{.calibre_17} were classes in a Java program.

But we can do even better than this. We can move all the [` defmulti `{.calibre4}]{.calibre_17} statements, along with their supporting functions, into their own [` payroll-interface `{.calibre4}]{.calibre_17} namespace and source file, like this:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_141.html#filepos971636)

> > [[`(ns payroll-interface)`{.calibre4}\
> > \
> > `(defn- get-pay-class [employee]`{.calibre4}\
> > `  (first (:pay-class employee)))`{.calibre4}\
> > \
> > `(defn- get-disposition [paycheck-directive]`{.calibre4}\
> > `  (first (:disposition paycheck-directive)))`{.calibre4}\
> > \
> > `(defmulti is-today-payday :schedule)`{.calibre4}\
> > `(defmulti calc-pay get-pay-class)`{.calibre4}\
> > `(defmulti dispose get-disposition)`{.calibre4}]{.calibre_3}]{.calibre_17}

And now we can draw the architecture diagram as shown in [[[Figure 9.5]{.underline}]{.calibre_10}](#index_split_022.html#filepos290612).

![](images/00184.jpg){#filepos290612 .calibre_41}

[[Figure 9.5.]{.bold}]{.calibre3}[ Architecture with interface]{.calibre3}

This is starting to look more and more like the UML diagram of a Java or C# program. It looks like we got a [` Payroll `{.calibre4}]{.calibre_17} class, a [` PayrollInterface `{.calibre4}]{.calibre_17} class, and a [` PayrollImplementation `{.calibre4}]{.calibre_17} class. And indeed, from an architectural point of view, that's a pretty accurate statement.

But there are some interesting differences. Where, for example, are the [` PaySchedule `{.calibre4}]{.calibre_17}, [` PayClassification `{.calibre4}]{.calibre_17}, and [` PayDisposition `{.calibre4}]{.calibre_17} classes that we saw in the UML of the OO Java program?

We could easily pull them out of the Clojure program by splitting the [` PayrollImplementation.clj `{.calibre4}]{.calibre_17} file into three namespaces and files, as shown in [[[Figure 9.6]{.underline}]{.calibre_10}](#index_split_022.html#filepos291974).

![](images/00169.jpg){#filepos291974 .calibre_42}

[[Figure 9.6.]{.bold}]{.calibre3}[ Split architecture]{.calibre3}

This is not the kind of thing you can do in Java or C# since there is no way, in those languages, to implement each function of an interface in a different module. However, it's perfectly possible in Clojure. The important thing to remember is that this is an [architectural]{.italic} diagram, not a class diagram. [` PaySchedule `{.calibre4}]{.calibre_17}, [` PayClassification `{.calibre4}]{.calibre_17}, and [` PayDisposition `{.calibre4}]{.calibre_17} are namespaces and source files, not classes. We do not make instances of them. They don't represent objects in an OO sense.

Not that there aren't objects in our Clojure solution. There certainly are. The [` employee `{.calibre4}]{.calibre_17}, the [` paycheck-directive `{.calibre4}]{.calibre_17}, and even the [` pay-class `{.calibre4}]{.calibre_17} and [` disposition `{.calibre4}]{.calibre_17} are objects. They do not have methods as strongly associated with them as they would if they were written in an OO language; but there are functions through which those objects flow.

[[[Namespaces and Source Files]{.calibre_3}]{.bold}]{.calibre1}

In Clojure especially, namespaces and source files are deeply connected. Each namespace must be contained in its own source file, and the name of that file must correspond[]{#index_split_022.html#filepos293742}[[[[11]{.underline}]{.calibre_10}]{.calibre3}](#index_split_022.html#filepos294148) to the name of the namespace. This is very similar to the way Java forces public classes into their own source file named for the class. It is also very similar to the file/class convention used by C++ and C# programmers. This could lead you to consider that each Clojure namespace is something like a class.

[[[11]{.underline}]{.calibre_10}](#index_split_022.html#filepos293742). Through a simple translation algorithm.

The correspondence is not perfect, of course. The contents of a Clojure namespace need not be class-like at all. But, in general, the concept is not a bad one.

One of the great temptations in functional languages like Clojure is to group functions into namespaces in a kind of ad hoc, by-feel way. Without the OO structure to force us to divide functions into classes that exist in their own source files, we often wind up with source file structures that are ricketier and more fragile than they ought to be.

So, when writing functional programs, it is not a bad idea to consider the partitioning disciplines of OO and continue to apply them. We'll see more of this later as we investigate principles, patterns, and architecture.

[[[Conclusion]{.calibre_3}]{.bold}]{.calibre1}

First of all, functional programs and OO programs are different. Functional programs tend to be constructions of plumbing that regulate data flow transformations, while mutable OO programs tend to iterate step by step over objects. However, from an architectural point of view, the two styles are quite compatible. It turns out that we can partition the functions of a functional program into the same kinds of architecturally significant elements as an OO program. From an architectural point of view, there's very little difference.

Functional programs may not be composed of syntactically enforced classes that enclose methods and define objects. Yet, objects still exist in functional programs. Those objects are less tightly bound to the functions that operate upon them than they would be in an OO language. Whether that is an advantage or a disadvantage is something we will continue to probe in the chapters that follow.

We shall see as these pages turn more and more toward design and architecture, the differences between functional programs and the object orientation of immutable objects start to become less and less relevant.

::: {#index_split_022.html#calibre_pb_22 .mbp_pagebreak}
:::

[]{#index_split_023.html}

[[[10]{.calibre_3}]{.bold}]{.calibre1}

[[[Types]{.calibre_3}]{.bold}]{.calibre1}

![](images/00276.jpg){.calibre_43}

The preceding chapter may have left you somewhat distressed. Those things that I called objects were just hash maps and were completely untyped. Anybody could stick anything into them without any constraint. The salary in the [` :pay-class `{.calibre4}]{.calibre_17} could hold a string instead of a number. The [` :schedule `{.calibre4}]{.calibre_17} field could hold an integer instead of the appropriate keyword.

In short, these objects are not statically typed. The compiler does not check them. And therefore, [all hell could break loose]{.italic}!

Many functional languages, as well as many OO languages, are statically typed in order to prevent that hell. Other languages, like Clojure, Python, and Ruby, depend upon other mechanisms to prevent that hell.

Those of us who practice TDD are not usually very concerned about that hell. Our tests generally ensure that the objects that we pass around are properly constructed. Still, in complex systems, where the totality of all the objects can end up being quite complex, there is a need for a more formal and complete way to ensure the integrity of our types than a dynamically typed language (and even most statically typed languages) can give us.

In Clojure, I use the [` clojure.spec `{.calibre4}]{.calibre_17} library to achieve the goal of type integrity. The type specification for our payroll example looks like this:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_142.html#filepos971767)

> > [[`(s/def ::id string?)`{.calibre4}\
> > `(s/def ::schedule #{:monthly :weekly :biweekly})`{.calibre4}\
> > `(s/def ::salaried-pay-class (s/tuple #(= % :salaried) pos`{.calibre4}]{.calibre_3}]{.calibre_17}[[[[1]{.underline}]{.calibre_10}]{.calibre3}](#index_split_023.html#filepos303239)[[`?))`{.calibre4}\
> > `(s/def ::hourly-pay-class (s/tuple #(= % :hourly) pos?))`{.calibre4}\
> > `(s/def ::commissioned-pay-class (s/tuple #(= % :commissioned)`{.calibre4}\
> > `                                         pos? pos?))`{.calibre4}\
> > `(s/def ::pay-class (s/or :salaried ::salaried-pay-class`{.calibre4}\
> > `                         :Hourly ::hourly-pay-class`{.calibre4}\
> > `                         :Commissioned ::commissioned-pay-class))`{.calibre4}\
> > `(s/def ::mail-disposition (s/tuple #(= % :mail) string? string?))`{.calibre4}\
> > `(s/def ::deposit-disposition (s/tuple #(= % :deposit)`{.calibre4}\
> > `                                      string? string?))`{.calibre4}\
> > `(s/def ::paymaster-disposition (s/tuple #(= % :paymaster)`{.calibre4}\
> > `                                        string?))`{.calibre4}\
> > `(s/def ::disposition (s/or :mail ::mail-disposition`{.calibre4}\
> > `                           :deposit ::deposit-disposition`{.calibre4}\
> > `                           :paymaster ::paymaster-disposition))`{.calibre4}\
> > `(s/def ::employee (s/keys :req-un [::id ::schedule`{.calibre4}\
> > `                                   ::pay-class ::disposition]))`{.calibre4}\
> > `(s/def ::employees (s/coll-of ::employee))`{.calibre4}\
> > \
> > `(s/def ::date string?)`{.calibre4}\
> > `(s/def ::time-card (s/tuple ::date pos?))`{.calibre4}\
> > `(s/def ::time-cards (s/map-of ::id (s/coll-of ::time-card)))`{.calibre4}\
> > \
> > `(s/def ::sales-receipt (s/tuple ::date pos?))`{.calibre4}\
> > `(s/def ::sales-receipts (s/map-of`{.calibre4}\
> > `                           ::id (s/coll-of ::sales-receipt)))`{.calibre4}\
> > \
> > `(s/def ::db (s/keys :req-un [::employees]`{.calibre4}\
> > `                    :opt-un [::time-cards ::sales-receipts]))`{.calibre4}\
> > \
> > `(s/def ::amount pos?)`{.calibre4}\
> > `(s/def ::name string?)`{.calibre4}\
> > `(s/def ::address string?)`{.calibre4}\
> > `(s/def ::mail-directive (s/and #(= (:type %) :mail)`{.calibre4}\
> > `                               (s/keys :req-un [::id`{.calibre4}\
> > `                                                ::name`{.calibre4}\
> > `                                                ::address`{.calibre4}\
> > `                                                ::amount])))`{.calibre4}\
> > \
> > `(s/def ::routing string?)`{.calibre4}\
> > `(s/def ::account string?)`{.calibre4}\
> > `(s/def ::deposit-directive (s/and #(= (:type %) :deposit)`{.calibre4}\
> > `                                  (s/keys :req-un [::id`{.calibre4}\
> > `                                                   ::routing`{.calibre4}\
> > `                                                   ::account`{.calibre4}\
> > `                                                   ::amount])))`{.calibre4}\
> > `(s/def ::paymaster string?)`{.calibre4}\
> > `(s/def ::paymaster-directive (s/and #(= (:type %) :paymaster)`{.calibre4}\
> > `                                    (s/keys :req-un [::id`{.calibre4}\
> > `                                                     ::paymaster`{.calibre4}\
> > `                                                     ::amount])))`{.calibre4}\
> > \
> > `(s/def ::paycheck-directive (s/or`{.calibre4}\
> > `                              :mail ::mail-directive`{.calibre4}\
> > `                              :deposit ::deposit-directive`{.calibre4}\
> > `                              :paymaster ::paymaster-directive))`{.calibre4}\
> > \
> > `(s/def ::paycheck-directives (s/coll-of ::paycheck-directive))`{.calibre4}]{.calibre_3}]{.calibre_17}
>
> []{#index_split_023.html#filepos303219}

[[[1]{.underline}]{.calibre_10}](#index_split_023.html#filepos303219). [` (pos? x) `{.calibre4}]{.calibre_17} returns true if [` x `{.calibre4}]{.calibre_17} is a number greater than zero.

If this looks scary, it should. There's a lot of detail in there. Keep in mind, however, that this is the level of detail that you would have to specify within the modules of a statically typed language in order to capture all the type constraints.

Understanding this type specification is not actually difficult. Look down toward the middle and find the definition of [` ::db `{.calibre4}]{.calibre_17}. This just says that the database is a hash map with a required [` :employees `{.calibre4}]{.calibre_17} field and two optional fields for [` :time-cards `{.calibre4}]{.calibre_17} and [` :sales-receipts `{.calibre4}]{.calibre_17}.

If you look a bit higher in the specification, you'll see that [` ::employees `{.calibre4}]{.calibre_17} is just a collection of [` ::employee `{.calibre4}]{.calibre_17}, [` ::sales-receipts `{.calibre4}]{.calibre_17} is a collection of [` ::sales-receipt `{.calibre4}]{.calibre_17}, and [` ::time-cards `{.calibre4}]{.calibre_17} is a collection of [` ::time-card `{.calibre4}]{.calibre_17}. Don't let the double colons bother you; they are a namespace convention. You can read the Clojure docs later if you want to understand them. For now, just look at the keywords and ignore how many colons there are.

As we continue to work our way up, we see that an [` ::employee `{.calibre4}]{.calibre_17} is a hash map that is required to have the keys [` :id `{.calibre4}]{.calibre_17}, [` :schedule `{.calibre4}]{.calibre_17}, [` :pay-class `{.calibre4}]{.calibre_17}, and [` :disposition `{.calibre4}]{.calibre_17}. Keep exploring and you'll find that the [` :id `{.calibre4}]{.calibre_17} must be a string; the [` :schedule `{.calibre4}]{.calibre_17} must be one of [` :monthly `{.calibre4}]{.calibre_17}, [` :weekly `{.calibre4}]{.calibre_17}, or [` :biweekly `{.calibre4}]{.calibre_17}; and a [` :salaried-pay-class `{.calibre4}]{.calibre_17} is a tuple containing [` :salaried `{.calibre4}]{.calibre_17}, followed by a positive number.

The [` s/or `{.calibre4}]{.calibre_17} statements might bother you a bit. The arguments come in pairs, and the first in each pair is just the name of that alternative. So, in the [` ::disposition `{.calibre4}]{.calibre_17} definition, [` :mail `{.calibre4}]{.calibre_17} is just the name of the [` ::mail-disposition `{.calibre4}]{.calibre_17} alternative. Don't worry anymore about this. It will become clear if you decide one day to read the [` clojure.spec `{.calibre4}]{.calibre_17} docs.

So, given this elaborate type specification, how do we use it? I sometimes use it in my tests as follows:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_144.html#filepos972059)

> > [[`(it "pays one salaried employee at end of month by mail"`{.calibre4}\
> > `  (let [employees [{:id "emp1"`{.calibre4}\
> > `                    :schedule :monthly`{.calibre4}\
> > `                    :pay-class [:salaried 5000]`{.calibre4}\
> > `                    :disposition [:mail "name" "home"]}]`{.calibre4}\
> > `        db {:employees employees}`{.calibre4}\
> > `        today (parse-date "Nov 30 2021")]`{.calibre4}\
> > `    `{.calibre4}]{.calibre_3}]{.calibre_17}[[`(should (s/valid? ::db db))`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `    (let [paycheck-directives (payroll today db)]`{.calibre4}\
> > `      `{.calibre4}]{.calibre_3}]{.calibre_17}[[`(should (s/valid? ::paycheck-directives`{.calibre4}]{.calibre_3}]{.bold}[[` `{.calibre4}\
> > `                     `{.calibre4}]{.calibre_3}]{.calibre_17}[[`paycheck-directives))`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `      (should= [{:type :mail`{.calibre4}\
> > `                 :id "emp1"`{.calibre4}\
> > `                 :name "name"`{.calibre4}\
> > `                 :address "home"`{.calibre4}\
> > `                 :amount 5000}]`{.calibre4}\
> > `               paycheck-directives))))`{.calibre4}]{.calibre_3}]{.calibre_17}

Look for the calls to [` s/valid? `{.calibre4}]{.calibre_17}, which is a function that returns true if the data matches the spec. Look carefully and you'll see that I'm checking the [` ::db `{.calibre4}]{.calibre_17} spec on the way in and the [` ::paycheck-directives `{.calibre4}]{.calibre_17} spec on the way out. This is pretty secure. If my tests have high coverage, and they all check the specs for the inputs and outputs of the functions they call, then violations of type ought to be extremely rare.

I have, upon occasion, also used Clojure's [` :pre `{.calibre4}]{.calibre_17} and [` :post `{.calibre4}]{.calibre_17} features to run the specs on critical data before and after the main processing functions of my applications.

Here, for example, is the main processing step of the [` spacewar `{.calibre4}]{.calibre_17}[]{#index_split_023.html#filepos309457}[[[[2]{.underline}]{.calibre_10}]{.calibre3}](#index_split_023.html#filepos309582) game I wrote some years ago:

[[[2]{.underline}]{.calibre_10}](#index_split_023.html#filepos309457). [[[https://github.com/unclebob/spacewar]{.underline}]{.calibre_10}](https://github.com/unclebob/spacewar)

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_145.html#filepos972205)

> > [[`(defn update-world [ms world]`{.calibre4}\
> > `  ;{:pre [(valid-world? world)]`{.calibre4}\
> > `  ; :post [(valid-world? %)]}`{.calibre4}\
> > `  (->> world`{.calibre4}\
> > `       (game-won ms)`{.calibre4}\
> > `       (game-over ms)`{.calibre4}\
> > `       (ship/update-ship ms)`{.calibre4}\
> > `       (shots/update-shots ms)`{.calibre4}\
> > `       (explosions/update-explosions ms)`{.calibre4}\
> > `       (clouds/update-clouds ms)`{.calibre4}\
> > `       (klingons/update-klingons ms)`{.calibre4}\
> > `       (bases/update-bases ms)`{.calibre4}\
> > `       (romulans/update-romulans ms)`{.calibre4}\
> > `       (view-frame/update-messages ms)`{.calibre4}\
> > `       (add-messages)))`{.calibre4}]{.calibre_3}]{.calibre_17}

The [` :pre `{.calibre4}]{.calibre_17} and [` :post `{.calibre4}]{.calibre_17} statements are commented out,[]{#index_split_023.html#filepos310963}[[[[3]{.underline}]{.calibre_10}]{.calibre3}](#index_split_023.html#filepos311151) but they are ready to be reasserted should I suspect some kind of terrible type corruption.

[[[3]{.underline}]{.calibre_10}](#index_split_023.html#filepos310963). I don't much care for commented-out code. I'd remove these lines as the project matured.

[[[Conclusion]{.calibre_3}]{.bold}]{.calibre1}

There is a lot of wailing and gnashing of teeth over the static versus dynamic typing issue. Each side yells at the other without listening to what either side has to say. I think both sides have valid points. Dynamic typing makes code easier to write. Static typing makes code a lot safer, easier to understand, and much more internally consistent. It seems to me that a library like [` clojure.spec `{.calibre4}]{.calibre_17} strikes a great balance. It gives you the ability to have as much or as little type checking as you need. It allows you to specify when types [are]{.italic} checked and when they are [not]{.italic}. What's more, it allows you to specify dynamic constraints that no static type system [can]{.italic} check. So, for my money, libraries like this give you better than the best of both worlds.

::: {#index_split_023.html#calibre_pb_23 .mbp_pagebreak}
:::

[]{#index_split_024.html}

[[III]{.calibre_3}]{.calibre2}

[[Functional Design]{.calibre_3}]{.calibre2}

::: {#index_split_024.html#calibre_pb_24 .mbp_pagebreak}
:::

[]{#index_split_025.html}

[[[11]{.calibre_3}]{.bold}]{.calibre1}

[[[Data Flow]{.calibre_3}]{.bold}]{.calibre1}

![](images/00333.jpg){.calibre_44}

In [[[Chapter 9]{.underline}]{.calibre_10}](#index_split_022.html#filepos262956), Object-Oriented Programming, I suggested that the design of a functional program is more like plumbing than procedure. There is a definite data flow bias to it. This is because we tend to use [` map `{.calibre4}]{.calibre_17}, [` filter `{.calibre4}]{.calibre_17}, and [` reduce `{.calibre4}]{.calibre_17} to transform the contents of lists into other lists, rather than iterating through the problem one element at a time to produce results.

We can see this bias in many of our previous examples, including the Bowling Game, Gossiping Bus Drivers, and Payroll applications in [[[Part II]{.underline}]{.calibre_10}](#index_split_018.html#filepos165870), Comparative Analysis.

As another example, consider this interesting problem from day ten of Advent of Code 2022.[]{#index_split_025.html#filepos313927}[[[[1]{.underline}]{.calibre_10}]{.calibre3}](#index_split_025.html#filepos314393) The goal was to render pixels on a 6-by-40 screen. The pixels were drawn from left to right, one at a time, based on a clock circuit. Clock cycles were counted starting at 0. If a certain register [` x `{.calibre4}]{.calibre_17} matched the clock cycle number, then the pixel at the appropriate screen position was turned on; otherwise, it was turned off.

[[[1]{.underline}]{.calibre_10}](#index_split_025.html#filepos313927). [[[https://adventofcode.com/2022/day/10]{.underline}]{.calibre_10}](https://adventofcode.com/2022/day/10)

This is actually quite typical of the way old CRT[]{#index_split_025.html#filepos314716}[[[[2]{.underline}]{.calibre_10}]{.calibre3}](#index_split_025.html#filepos315171) displays used to work. You had to energize the electron beam at just the right moment as it rastered over the screen. So you matched the bits in the bitmap to the clock that drove that beam. If, according to the clock, the beam was at position 934, and if the 934th bit in the bitmap was set, then you energized the beam for an instant to display that pixel.

[[[2]{.underline}]{.calibre_10}](#index_split_025.html#filepos314716). Cathode ray tube. A [cathode ray]{.italic} is an electron. CRTs have electron guns that create narrow beams of electrons that are rastered across the screen using regularly changing magnetic fields. The beam strikes phosphors on the screen and makes them glow, thus creating a raster image.

The Advent of Code problem was a bit more interesting. It asked us to simulate a simple processor that had two instructions. The first instruction was [` noop `{.calibre4}]{.calibre_17}, which took one clock cycle but had no other effect. The other instruction was [` addx `{.calibre4}]{.calibre_17}, which took an integer argument [` n `{.calibre4}]{.calibre_17} that it added to the [` x `{.calibre4}]{.calibre_17} register of the processor. This instruction consumed two clock cycles and only changed the [` x `{.calibre4}]{.calibre_17} register after both cycles had completed. Pixels on []{#index_split_025.html#filepos316270}the screen would be visible for a clock cycle if, and only if, at the beginning of that cycle the [` x `{.calibre4}]{.calibre_17} register matched the clock cycle number.

So if according to the clock, the beam was over screen position 23, and if the [` x `{.calibre4}]{.calibre_17} register was 23 at the start of cycle 23, then the beam would be energized for that clock cycle.

To complicate matters just a little more, the matching of the [` x `{.calibre4}]{.calibre_17} register to the clock cycle was widened so that 22, 23, and 24 would match clock cycle 23. In other words, the [` x `{.calibre4}]{.calibre_17} register specified a window that was three pixels wide. So long as the clock cycle fell within that window, the beam would be energized.

Since the screen is 40 pixels wide and 6 pixels tall, the matching of the clock cycle to [` x `{.calibre4}]{.calibre_17} is modulus 40.

The task was to execute a set of instructions and produce a list of six strings that were 40 characters each, with [` "#" `{.calibre4}]{.calibre_17} indicating a pixel that was visible and [` "." `{.calibre4}]{.calibre_17} indicating one that was not visible.

If you were to write this program in Java, C, Go, C++, C#, or any other procedural/OO language, you might create a loop that iterated one cycle at a time while accumulating the appropriate pixels for each cycle. The loop would consume instructions and modify the [` x `{.calibre4}]{.calibre_17} register as directed.

Here's a typical example in Java:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_146.html#filepos972336)

> > [[`package crt;`{.calibre4}\
> > \
> > `public class Crt {`{.calibre4}\
> > `  private int x;`{.calibre4}\
> > `  private String pixels = "";`{.calibre4}\
> > `  private int extraCycles = 0;`{.calibre4}\
> > `  private int cycle = 0;`{.calibre4}\
> > `  private int ic;`{.calibre4}\
> > `  private String[] instructions;`{.calibre4}\
> > `  public Crt(int x) {`{.calibre4}\
> > `    this.x = x;`{.calibre4}\
> > `  }`{.calibre4}\
> > \
> > `  public void doCycles(int n, String instructionsLines) {`{.calibre4}\
> > `    instructions = instructionsLines.split("\n");`{.calibre4}\
> > `    ic = 0;`{.calibre4}\
> > `    for (cycle = 0; cycle < n; cycle++) {`{.calibre4}\
> > `      setPixel();`{.calibre4}\
> > `      execute();`{.calibre4}\
> > `    }`{.calibre4}\
> > `  }`{.calibre4}\
> > \
> > `  private void execute() {`{.calibre4}\
> > `    if (instructions[ic].equals("noop"))`{.calibre4}\
> > `      ic++;`{.calibre4}\
> > `    else if (instructions[ic].startsWith("addx ")`{.calibre4}\
> > `             && extraCycles == 0) {`{.calibre4}\
> > `      extraCycles = 1;`{.calibre4}\
> > `    }`{.calibre4}\
> > `    else if (instructions[ic].startsWith("addx ")`{.calibre4}\
> > `             && extraCycles == 1) {`{.calibre4}\
> > `      extraCycles = 0;`{.calibre4}\
> > `      x += Integer.parseInt(instructions[ic].substring(5));`{.calibre4}\
> > `      ic++;`{.calibre4}\
> > `    } else`{.calibre4}\
> > `      System.out.println("TILT");`{.calibre4}\
> > `  }`{.calibre4}\
> > \
> > `  private void setPixel() {`{.calibre4}\
> > `    int pos = cycle % 40;`{.calibre4}\
> > `    int offset = pos - x;`{.calibre4}\
> > `    if (offset >= -1 && 1 >= offset)`{.calibre4}\
> > `      pixels += "#";`{.calibre4}\
> > `    else`{.calibre4}\
> > `      pixels += ".";`{.calibre4}\
> > `  }`{.calibre4}\
> > \
> > `  public String getPixels() {`{.calibre4}\
> > `    return pixels;`{.calibre4}\
> > `  }`{.calibre4}\
> > \
> > `  public int getX() {`{.calibre4}\
> > `    return x;`{.calibre4}\
> > `  }`{.calibre4}\
> > `}`{.calibre4}]{.calibre_3}]{.calibre_17}
>
> []{#index_split_025.html#filepos320339}

Notice all the mutated state. Notice how it iterates, cycle by cycle, to populate the pixels. Notice also the funny business of [` extraCycles `{.calibre4}]{.calibre_17} to account for the fact that [` addx `{.calibre4}]{.calibre_17} takes two cycles to execute.

Finally, notice that although the program is nicely partitioned into a few smallish functions, those functions are all coupled together by the mutable state variables. That is, of course, the usual situation for methods of a mutable class.

I solved this problem in Clojure today. And the solution I came up with was very different from the Java code above. Remember as you read this to start at the bottom. Clojure programs are always written from the bottom up.

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_148.html#filepos972628)

> > [[`(ns day10-cathode-ray-tube.core`{.calibre4}\
> > `  (:require [clojure.string :as string]))`{.calibre4}\
> > \
> > `(defn noop [state]`{.calibre4}\
> > `  (update state :cycles conj (:x state)))`{.calibre4}\
> > \
> > `(defn addx [n state]`{.calibre4}\
> > `  (let [{:keys [x cycles]} state]`{.calibre4}\
> > `    (assoc state :x (+ x n)`{.calibre4}\
> > `                 :cycles (vec (concat cycles [x x])))))`{.calibre4}\
> > \
> > `(defn execute [state lines]`{.calibre4}\
> > `  (if (empty? lines)`{.calibre4}\
> > `    state`{.calibre4}\
> > `    (let [line (first lines)`{.calibre4}\
> > `          state (if (re-matches #"noop" line)`{.calibre4}\
> > `                  (noop state)`{.calibre4}\
> > `                  (if-let [[_ n] (re-matches`{.calibre4}\
> > `                                   #"addx (-?\d+)" line)]`{.calibre4}\
> > `                    (addx (Integer/parseInt n) state)`{.calibre4}\
> > `                    "TILT"))]`{.calibre4}]{.calibre_3}]{.calibre_17}[[[[3]{.underline}]{.calibre_10}]{.calibre3}](#index_split_025.html#filepos323969)[[\
> > `      (recur state (rest lines)))))`{.calibre4}\
> > \
> > `(defn execute-file [file-name]`{.calibre4}\
> > `  (let [lines (string/split-lines (slurp file-name))`{.calibre4}\
> > `        starting-state {:x 1 :cycles []}`{.calibre4}\
> > `        ending-state (execute starting-state lines)]`{.calibre4}\
> > `    (:cycles ending-state)))`{.calibre4}\
> > \
> > `(defn render-cycles [cycles]`{.calibre4}\
> > `  (loop [cycles cycles`{.calibre4}\
> > `         screen ""`{.calibre4}\
> > `         t 0]`{.calibre4}\
> > `    (if (empty? cycles)`{.calibre4}\
> > `      (map #(apply str %) (partition 40 40 "" screen))`{.calibre4}\
> > `      (let [x (first cycles)`{.calibre4}\
> > `            offset (- t x)`{.calibre4}\
> > `            pixel? (<= -1 offset 1)`{.calibre4}\
> > `            screen (str screen (if pixel? "#" "."))`{.calibre4}\
> > `            t (mod (inc t) 40)]`{.calibre4}\
> > `        (recur (rest cycles) screen t)))))`{.calibre4}\
> > \
> > `(defn print-screen [lines]`{.calibre4}\
> > `  (doseq [line lines]`{.calibre4}\
> > `    (println line))`{.calibre4}\
> > `  true)`{.calibre4}\
> > \
> > `(defn -main []`{.calibre4}\
> > `  (-> "input"`{.calibre4}\
> > `      execute-file`{.calibre4}\
> > `      render-cycles`{.calibre4}\
> > `      print-screen))`{.calibre4}]{.calibre_3}]{.calibre_17}
>
> []{#index_split_025.html#filepos323949}

[[[3]{.underline}]{.calibre_10}](#index_split_025.html#filepos323949). TILT is my favorite error message. Long ago, pinball machines would put up this message and cancel your game if you physically tilted the machine in order to manipulate the ball.

The [` execute-file `{.calibre4}]{.calibre_17} function transforms the list of instructions in the named file into a list of resulting [` x `{.calibre4}]{.calibre_17} values. The [` render-cycles `{.calibre4}]{.calibre_17} function then transforms the list of [` x `{.calibre4}]{.calibre_17} values into a list of pixels, which it finally [` partition `{.calibre4}]{.calibre_17}s into strings of 40 characters.

Notice that there are, of course, no mutable variables. Instead, the [` state `{.calibre4}]{.calibre_17} value flows through each of the functions as though through a pipeline.

The [` state `{.calibre4}]{.calibre_17} value begins in [` execute-file `{.calibre4}]{.calibre_17} and then flows to [` execute `{.calibre4}]{.calibre_17}, then repeatedly to [` noop `{.calibre4}]{.calibre_17} or [` addx `{.calibre4}]{.calibre_17}, and then back to [` execute `{.calibre4}]{.calibre_17}, and finally back to [` execute-file `{.calibre4}]{.calibre_17}. At each stage in that flow, a new value of [` state `{.calibre4}]{.calibre_17} is created from the old without changing the old.

If this seems eerily familiar to you, it should. This is very much like the pipes and filters we have gotten used to in our command-line shells. Data flows into a command from a pipe, is transformed by that command, and then flows out to the next command through a pipe.

Here's a recent command I've been using at the shell:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_150.html#filepos972920)

> > [[`ls -lh private/messages | cut -c 32-37,57-64`{.calibre4}]{.calibre_3}]{.calibre_17}

It lists the [` private/messages `{.calibre4}]{.calibre_17} directory and then [` cut `{.calibre4}]{.calibre_17}s out certain fields. The data flows out of the [` ls `{.calibre4}]{.calibre_17} command, through the pipe, and then into the [` cut `{.calibre4}]{.calibre_17} command. This has the same kind of feel as the [` state `{.calibre4}]{.calibre_17} value flowing through the [` execute `{.calibre4}]{.calibre_17}, [` addx `{.calibre4}]{.calibre_17}, and [` noop `{.calibre4}]{.calibre_17} functions.

As a result of this pipelining, you should notice that my [` cathode-ray-tube `{.calibre4}]{.calibre_17} program is partitioned into a set of smallish functions that are not coupled to one another by mutable state. Whatever coupling exists is merely the coupling of the data formats that flow from function to function through the pipes.

Finally, notice that there is none of the funny business we saw in the Java program surrounding the two cycles of the [` addx `{.calibre4}]{.calibre_17} instruction. Instead, the []{#index_split_025.html#filepos327739}two cycles are neatly accounted for by simply adding two [` x `{.calibre4}]{.calibre_17} values to the [` :cycles `{.calibre4}]{.calibre_17} element of the [` state `{.calibre4}]{.calibre_17}.

Of course, I didn't have to use the data flow style. I could have created a Clojure algorithm that was much closer to the Java algorithm. But that's not the way I think about things when I'm writing in a functional language. Instead, I am biased toward data flow solutions.

Some of the newer features in Java and C# lend themselves to the data flow style. But they are wordy and appear to me to be bolted onto the languages in awkward ways. Your mileage may vary; but I find that when I use procedural/OO languages I tend to iterate much more than I tend to plumb.

Or, to say this differently:

[In mutable languages, behaviors flow through objects. In functional languages, objects flow through behaviors.]{.italic}

::: {#index_split_025.html#calibre_pb_25 .mbp_pagebreak}
:::

[]{#index_split_026.html}

[[[12]{.calibre_3}]{.bold}]{.calibre1}

[[[Solid]{.calibre_3}]{.bold}]{.calibre1}

![](images/00348.jpg){.calibre_45}

I wrote about the SOLID principles over two decades ago in the context of OO design. Because of that context, many have come to associate those principles with OO and regard them as anathema to functional programming. This is unfortunate because the SOLID principles are general principles of software design that are not specific to any particular programming style. In this chapter, I will endeavor to explain how the SOLID principles apply to functional programming.

The following chapters are summaries, not complete descriptions, of the principles. For those of you who are interested in more detail, I recommend the following sources.

::: calibre_11
 
:::

-   [Agile Software Development: Principles, Patterns, and Practices]{.italic}.[[[[1]{.underline}]{.calibre_10}]{.calibre3}](#index_split_026.html#filepos330436)

    > [[[1]{.underline}]{.calibre_10}](#index_split_026.html#filepos330436). Robert C. Martin (Pearson, 2002).

-   [Clean Architecture]{.italic}.[[[[2]{.underline}]{.calibre_10}]{.calibre3}](#index_split_026.html#filepos330835)

    > [[[2]{.underline}]{.calibre_10}](#index_split_026.html#filepos330835). Robert C. Martin (Pearson, 2017).

-   [[[Cleancoder.com]{.underline}]{.calibre_10}](http://Cleancoder.com). Check out the blog posts and articles. There are lots and lots of things to learn on this Web site about principles and more.

-   [[[Cleancoders.com]{.underline}]{.calibre_10}](http://Cleancoders.com). This Web site has videos that explain each principle in great detail and with compelling examples.

[[[The Single Responsibility Principle (SRP)]{.calibre_3}]{.bold}]{.calibre1}

![](images/00346.jpg){.calibre_48}

The [SRP]{.italic} is a simple statement about focusing our modules on the sources that cause them to change. Those sources are, of course, [people]{.italic}. It is []{#index_split_026.html#filepos331947}people who request changes to software, and therefore it is people to whom our modules are responsible.

These people can be separated into groups called [roles]{.italic} or [actors]{.italic}. An actor is a person, or a group of people, who require the same things from the system. The kinds of changes they request will be consistent with each other. On the other hand, different actors have different needs. The changes one actor requests will affect the system in very different ways from the changes requested by other actors. Those disparate changes may even be at cross purposes to each other.

When a module is responsible to more than one actor, the changes requested by those competing actors can interfere with each other. This interference often leads to the design smell of [fragility]{.italic}; causing the system to break in unexpected ways when simple changes are made.

Nothing can be quite so terrifying to managers and customers than systems that suddenly misbehave in startling ways after simple feature changes are made. If this repeats too often, the only conclusion they can come to is that the developers have lost control of the system and don't know what they are doing.

A violation of the SRP can be as simple as mixing GUI formatting and business rule code together in the same module. Or it can be as complex as using stored procedures in the database to implement business rules.

Here's a simple example of a nasty SRP violation written in Clojure. First, let's look at the tests because they tell the story:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_151.html#filepos973050)

> > [[`(describe "Order Entry System"`{.calibre4}\
> > `  (context "Parsing Customers"`{.calibre4}\
> > `    (it "parses a valid customer"`{.calibre4}\
> > `      (should=`{.calibre4}\
> > `        {:id "1234567"`{.calibre4}\
> > `         :name "customer name"`{.calibre4}\
> > `         :address "customer address"`{.calibre4}\
> > `         :credit-limit 50000}`{.calibre4}\
> > `        (parse-customer`{.calibre4}\
> > `          ["Customer-id: 1234567"`{.calibre4}\
> > `           "Name: customer name"`{.calibre4}\
> > `           "Address: customer address"`{.calibre4}\
> > `           "Credit Limit: 50000"])))`{.calibre4}\
> > \
> > `    (it "parses invalid customer"`{.calibre4}\
> > `      (should= :invalid`{.calibre4}\
> > `               (parse-customer`{.calibre4}\
> > `                 ["Customer-id: X"`{.calibre4}\
> > `                  "Name: customer name"`{.calibre4}\
> > `                  "Address: customer address"`{.calibre4}\
> > `                  "Credit Limit: 50000"]))`{.calibre4}\
> > `      (should= :invalid`{.calibre4}\
> > `               (parse-customer`{.calibre4}\
> > `                 ["Customer-id: 1234567"`{.calibre4}\
> > `                  "Name: "`{.calibre4}\
> > `                  "Address: customer address"`{.calibre4}\
> > `                  "Credit Limit: 50000"]))`{.calibre4}\
> > `      (should= :invalid`{.calibre4}\
> > `               (parse-customer`{.calibre4}\
> > `                 ["Customer-id: 1234567"`{.calibre4}\
> > `                  "Name: customer name"`{.calibre4}\
> > `                  "Address: "`{.calibre4}\
> > `                  "Credit Limit: 50000"]))`{.calibre4}\
> > `      (should= :invalid`{.calibre4}\
> > `               (parse-customer`{.calibre4}\
> > `                 ["Customer-id: 1234567"`{.calibre4}\
> > `                  "Name: customer name"`{.calibre4}\
> > `                  "Address: customer address"`{.calibre4}\
> > `                  "Credit Limit: invalid"])))`{.calibre4}\
> > `    (it "makes sure credit limit is <= 50000"`{.calibre4}\
> > `      (should= :invalid`{.calibre4}\
> > `               (parse-customer`{.calibre4}\
> > `                 ["Customer-id: 1234567"`{.calibre4}\
> > `                  "Name: customer name"`{.calibre4}\
> > `                  "Address: customer address"`{.calibre4}\
> > `                  "Credit Limit: 50001"])))))`{.calibre4}]{.calibre_3}]{.calibre_17}

The first test tells us that we are parsing some text input into a customer record. That record has four fields: [` id `{.calibre4}]{.calibre_17}, [` name `{.calibre4}]{.calibre_17}, [` address `{.calibre4}]{.calibre_17}, and [` credit-limit `{.calibre4}]{.calibre_17}. The next four tests tell us about syntax errors such as missing or malformed input.

The last test is the interesting one. It tests a business rule. Testing a business rule as part of parsing the input is a clear SRP violation. The parsing code can safely validate syntax errors, but it should avoid all [semantic]{.italic} checks because those checks are in the domain of a different actor. The actor who specifies the input format is not the same as the actor who specifies the largest allowable credit limit.[]{#index_split_026.html#filepos337513}[[[[3]{.underline}]{.calibre_10}]{.calibre3}](#index_split_026.html#filepos337609)

[[[3]{.underline}]{.calibre_10}](#index_split_026.html#filepos337513). This is true even when the two actors are the same person. In that case, that person is playing two different roles.

The code that passes these tests exacerbates the problem:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_153.html#filepos973343)

> > [[`(defn validate-customer`{.calibre4}\
> > `  [{:keys [id name address credit-limit] :as customer}]`{.calibre4}\
> > `  (if (or (nil? id)`{.calibre4}\
> > `          (nil? name)`{.calibre4}\
> > `          (nil? address)`{.calibre4}\
> > `          (nil? credit-limit))`{.calibre4}\
> > `    :invalid`{.calibre4}\
> > `    (let [credit-limit (Integer/parseInt credit-limit)]`{.calibre4}\
> > `      (if `{.calibre4}]{.calibre_3}]{.calibre_17}[[`(> credit-limit 50000)`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `        :invalid`{.calibre4}\
> > `        (assoc customer :credit-limit credit-limit)))))`{.calibre4}\
> > \
> > `(defn parse-customer [lines]`{.calibre4}\
> > \
> > `  (let [[_ id] (re-matches #"^Customer-id: (\d{7})$"`{.calibre4}\
> > `                           (nth lines 0))`{.calibre4}\
> > `        [_ name] (re-matches #"^Name: (.+)$" (nth lines 1))`{.calibre4}\
> > `        [_ address] (re-matches #"^Address: (.+)$" (nth lines 2))`{.calibre4}\
> > `        [_ credit-limit] (re-matches #"^Credit Limit: (\d+)$"`{.calibre4}\
> > `                                     (nth lines 3))]`{.calibre4}\
> > `    (validate-customer`{.calibre4}\
> > `      {:id id`{.calibre4}\
> > `       :name name`{.calibre4}\
> > `       :address address`{.calibre4}\
> > `       :credit-limit credit-limit})))`{.calibre4}]{.calibre_3}]{.calibre_17}
>
> []{#index_split_026.html#filepos339613}

Look at how the [` validate-customer `{.calibre4}]{.calibre_17} function mixes the syntax checks with the semantic business rule that limits the credit limit to 50,000. That semantic check belongs in an entirely different module, not tangled in with all those syntax checks.

Worse, consider a programmer who conscientiously uses [` clojure/spec `{.calibre4}]{.calibre_17} to dynamically define the type of [` customer `{.calibre4}]{.calibre_17}:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_154.html#filepos973489)

> > [[`(s/def ::id (s/and`{.calibre4}\
> > `              string?`{.calibre4}\
> > `              #(re-matches #"\d+" %)))`{.calibre4}\
> > `(s/def ::name string?)`{.calibre4}\
> > `(s/def ::address string?)`{.calibre4}\
> > `(s/def ::credit-limit `{.calibre4}]{.calibre_3}]{.calibre_17}[[`(s/and int? #(<= % 50000))`{.calibre4}]{.calibre_3}]{.bold}[[`)`{.calibre4}\
> > `(s/def ::customer (s/keys :req-un [::id ::name`{.calibre4}\
> > `                                   ::address ::credit-limit]))`{.calibre4}]{.calibre_3}]{.calibre_17}

This specification properly constrains the customer data structure to be syntactically correct; but it also imposes the semantic business rule constraint that the credit limit must not be greater than 50,000.

Why am I concerned about mixing the credit limit constraint with the syntax of the data structure? It is because I expect the syntax of the data structure and the credit limit constraint to be specified by different actors. And I expect those different actors will request changes at different times and for different reasons. I don't want a change to the syntax to inadvertently break a business rule.

Of course, this begs the question: Where do semantic validations belong? The answer to that is semantic validations belong in the modules responsible to the actors who are likely to change them. If, for example, []{#index_split_026.html#filepos342014}there is a business rule that says that credit limits must not exceed 50,000, then the enforcement code should go in the module that handles all the other credit limit processing.

[Gather together the things that change for the]{.italic}

[same reasons, and at the same times.]{.italic}

[Separate those things that change for different]{.italic}

[reasons or at different times.]{.italic}

[[[The Open-Closed Principle (OCP)]{.calibre_3}]{.bold}]{.calibre1}

![](images/00024.jpg){.calibre_50}

The [OCP]{.italic} was first stated by Bertrand Meyer in his classic 1988 book, [Object-Oriented Software Construction]{.italic}.[]{#index_split_026.html#filepos342989}[[[[4]{.underline}]{.calibre_10}]{.calibre3}](#index_split_026.html#filepos343326) To paraphrase, it says that software modules should be open for extension but closed for modification. This means that you want to design your modules such that extending or changing their behavior does not require you to modify their code.

[[[4.]{.underline}]{.calibre_10}](#index_split_026.html#filepos342989) Pearson, 1988.

This may sound oxymoronic, but it's actually something that we do all the time. Consider, for example, the [` copy `{.calibre4}]{.calibre_17} program in C:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_155.html#filepos973635)

> > [[`void copy() {`{.calibre4}\
> > `  int c;`{.calibre4}\
> > `  while ((c = getchar()) != EOF)`{.calibre4}\
> > `    putchar(c);`{.calibre4}\
> > `}`{.calibre4}]{.calibre_3}]{.calibre_17}

This program copies characters from [` stdin `{.calibre4}]{.calibre_17} to [` stdout `{.calibre4}]{.calibre_17}. I can add new devices to the operating system anytime I like. For example, I could add an optical character recognition (OCR) and a text-to-speech synthesizer to the system. This program would still operate without complaint and would happily copy characters from the OCR to the voice synthesizer without needing to be modified or even recompiled.

This is a very powerful idea that allows us to separate high-level policy from low-level detail and keep the high-level policy immune from changes to the low-level detail. However, it requires that the high-level policy access the low-level detail through an abstraction layer.

In OO programs, we typically create that abstraction layer through polymorphic interfaces. In statically typed languages like Java, C#, and C++, those interfaces are classes[]{#index_split_026.html#filepos345161}[[[[5]{.underline}]{.calibre_10}]{.calibre3}](#index_split_026.html#filepos345418) with abstract methods. High-level policies are given access through those interfaces to the low-level details that implement, or inherit from, those interfaces.

[[[5]{.underline}]{.calibre_10}](#index_split_026.html#filepos345161). The keyword [` interface `{.calibre4}]{.calibre_17} in Java and C# defines classes where every method is abstract.

In dynamically typed OO languages like Python and Ruby, these interfaces are duck types. [Duck types]{.italic} have no particular syntax within the language. They are simply sets of function signatures called by the high-level policies and implemented by the low-level details. The dynamic type system determines the polymorphic dispatch at runtime by matching those signatures.

Some functional languages, like F# and Scala, sit on top of an OO foundation and thus can take advantage of the polymorphic interfaces of that foundation. But functional languages have long had another mechanism by which the abstraction layer for the OCP can be created: functions.

[[Functions]{.calibre_3}]{.bold}

Consider this simple Clojure program:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_026.html#filepos347814)

> > [[`(defn copy [read write]`{.calibre4}\
> > `  (let [c (read)]`{.calibre4}\
> > `    (if (= c :eof)`{.calibre4}\
> > `      nil`{.calibre4}\
> > `      (recur read (write c)))))`{.calibre4}]{.calibre_3}]{.calibre_17}

This is essentially the same program as the [` copy `{.calibre4}]{.calibre_17} program written in C, except that the functions to read and write have been passed in as arguments.[]{#index_split_026.html#filepos347275}[[[[6]{.underline}]{.calibre_10}]{.calibre3}](#index_split_026.html#filepos347430) Nevertheless, the abstraction layer for the OCP is intact.

[[[6.]{.underline}]{.calibre_10}](#index_split_026.html#filepos347275) Functions that are passed as arguments, or returned as values from functions, are sometimes called [higher-order functions]{.italic}.

By the way, I tested this program using the following tests. I think you'll find this interesting.

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_157.html#filepos973927)

> > [[`(def str-in (atom nil))`{.calibre4}\
> > `(def str-out (atom nil))`{.calibre4}\
> > \
> > `(defn str-read []`{.calibre4}\
> > `  (let [c (first @str-in)]`{.calibre4}\
> > `    (if (nil? c)`{.calibre4}\
> > `      :eof`{.calibre4}\
> > `      (do`{.calibre4}\
> > `        (swap! str-in rest)`{.calibre4}\
> > `        c))))`{.calibre4}\
> > \
> > `(defn str-write [c]`{.calibre4}\
> > `  (swap! str-out str c)`{.calibre4}\
> > `  str-write)`{.calibre4}\
> > \
> > `(describe "copy"`{.calibre4}\
> > `  (it "can read and write using str-read and str-write"`{.calibre4}\
> > `    (reset! str-in "abcedf")`{.calibre4}\
> > `    (reset! str-out "")`{.calibre4}\
> > `    (copy str-read str-write)`{.calibre4}\
> > `    (should= "abcdef" @str-out)))`{.calibre4}]{.calibre_3}]{.calibre_17}
>
> []{#index_split_026.html#filepos348780}

I used the [` atom `{.calibre4}]{.calibre_17}s because I/O is a side effect and is therefore not purely functional. After all, when you read from an input or write to an output, you are mutating their states. Thus, the low-level I/O functions are not purely functional and use Software Transactional Memory to manage the mutation of state.

[[Objects with Vtables]{.calibre_3}]{.bold}

For those of you who are pining for OO, you can pass an "object" into [` copy `{.calibre4}]{.calibre_17} using the following technique:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_026.html#filepos350604)

> > [[`(defn copy [`{.calibre4}]{.calibre_3}]{.calibre_17}[[`device`{.calibre4}]{.calibre_3}]{.bold}[[`]`{.calibre4}\
> > `  (let [c ((`{.calibre4}]{.calibre_3}]{.calibre_17}[[`:getchar device)`{.calibre4}]{.calibre_3}]{.bold}[[`)]`{.calibre4}\
> > `    (if (= c :eof)`{.calibre4}\
> > `      nil`{.calibre4}\
> > `      (do`{.calibre4}\
> > `        `{.calibre4}]{.calibre_3}]{.calibre_17}[[`((:putchar device)`{.calibre4}]{.calibre_3}]{.bold}[[` c)`{.calibre4}\
> > `        (recur `{.calibre4}]{.calibre_3}]{.calibre_17}[[[`device`{.calibre4}]{.calibre_3}]{.bold}]{.italic}[[`)))))`{.calibre4}]{.calibre_3}]{.calibre_17}

The test simply loads the device map with the functions:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_159.html#filepos974219)

> > [[`(it "can read and write using str-read and str-write"`{.calibre4}\
> > `    (reset! str-in "abcedf")`{.calibre4}\
> > `    (reset! str-out "")`{.calibre4}\
> > `    (copy `{.calibre4}]{.calibre_3}]{.calibre_17}[[`{:getchar str-read :putchar str-write}`{.calibre4}]{.calibre_3}]{.bold}[[`)`{.calibre4}\
> > `    (should= "abcdef" @str-out))`{.calibre4}]{.calibre_3}]{.calibre_17}

C++ programmers will recognize that the [` device `{.calibre4}]{.calibre_17} argument is just a vtable---which is the polymorphism mechanism in C++. In any case, it should be obvious that you can define many different devices for the [` copy `{.calibre4}]{.calibre_17} program to use. You can extend the behavior of [` copy `{.calibre4}]{.calibre_17} without having to modify it.

[[Multi-methods]{.calibre_3}]{.bold}

Still another variation on this theme is the use of multi-methods. Many languages, functional or otherwise, support multi-methods in one way or another. [Multi-methods]{.italic} are another form of duck typing, because they create a loose grouping of methods that are dynamically dispatched based on their function signature and the "type"[]{#index_split_026.html#filepos352217}[[[[7]{.underline}]{.calibre_10}]{.calibre3}](#index_split_026.html#filepos352331) of the arguments.

[[[7.]{.underline}]{.calibre_10}](#index_split_026.html#filepos352217) I used quotes here because the "type" of the arguments is not necessarily associated with their specific data types. Indeed, that "type" can be a completely different concept.

In Clojure, we use the time-honored approach of a [dispatching function]{.italic} to specify that "type":

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_160.html#filepos974365)

> > [[`(defmulti getchar (fn [device] (:device-type device)))`{.calibre4}\
> > `(defmulti putchar (fn [device c] (:device-type device)))`{.calibre4}]{.calibre_3}]{.calibre_17}

Here we see [` getchar `{.calibre4}]{.calibre_17} and [` putchar `{.calibre4}]{.calibre_17} declared as multi-methods. Each has a dispatching function that takes the same arguments that [` getchar `{.calibre4}]{.calibre_17} and [` putchar `{.calibre4}]{.calibre_17} will be called with. We can change the [` copy `{.calibre4}]{.calibre_17} program to call those multi-methods:

> > [[`(defn copy [device]`{.calibre4}\
> > `  (let [c `{.calibre4}]{.calibre_3}]{.calibre_17}[[`(getchar device)`{.calibre4}]{.calibre_3}]{.bold}[[`]`{.calibre4}\
> > `    (if (= c :eof)`{.calibre4}\
> > `      nil`{.calibre4}\
> > `      (do`{.calibre4}\
> > `        `{.calibre4}]{.calibre_3}]{.calibre_17}[[`(putchar device c)`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `        (recur device)))))`{.calibre4}]{.calibre_3}]{.calibre_17}

The test for this new copy function is below. Notice that the test [` device `{.calibre4}]{.calibre_17} is no longer a vtable containing pointers to functions. Instead, it now contains the input and output [` atom `{.calibre4}]{.calibre_17}s, and also a [` :device-type `{.calibre4}]{.calibre_17}. It is that [` :device-type `{.calibre4}]{.calibre_17} that the multi-methods will be dispatching on.

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_161.html#filepos974510)

> > [[`(it "can read and write using multi-method"`{.calibre4}\
> > `  (let [device {:device-type :test-device`{.calibre4}\
> > `                :input (atom "abcdef")`{.calibre4}\
> > `                :output (atom nil)}]`{.calibre4}\
> > `    (copy device)`{.calibre4}\
> > `    (should= "abcdef" @(:output device))))`{.calibre4}]{.calibre_3}]{.calibre_17}
>
> []{#index_split_026.html#filepos355413}

All that remains are the implementations of the multi-methods. They should not be too surprising.

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_162.html#filepos974656)

> > [[`(defmethod getchar :test-device [device]`{.calibre4}\
> > `  (let [input (:input device)`{.calibre4}\
> > `        c (first @input)]`{.calibre4}\
> > `    (if (nil? c)`{.calibre4}\
> > `      :eof`{.calibre4}\
> > `      (do`{.calibre4}\
> > `        (swap! input rest)`{.calibre4}\
> > `        c))))`{.calibre4}\
> > \
> > `(defmethod putchar :test-device [device c]`{.calibre4}\
> > `  (let [output (:output device)]`{.calibre4}\
> > `    (swap! output str c)))`{.calibre4}]{.calibre_3}]{.calibre_17}

These are the implementations that will be dispatched when the [` :device-type `{.calibre4}]{.calibre_17} is [` :test-device `{.calibre4}]{.calibre_17}. It should be clear that many other such implementation methods could be created for various different devices. Those new devices will extend the [` copy `{.calibre4}]{.calibre_17} program without forcing any modification.

[[Independent Deployability]{.calibre_3}]{.bold}

One of the benefits we expect to get from the OCP is the ability to compile high-level policies and low-level details in separate modules and to deploy them independently. In Java and C#, this would mean compiling them down into separate [` jar `{.calibre4}]{.calibre_17} or [` dll `{.calibre4}]{.calibre_17} files that can be dynamically loaded. In C++, we would compile the modules and place the binaries into dynamically loadable shared libraries.

The Clojure solutions shown above do not achieve that goal. The high-level policy and the low-level detail cannot be dynamically loaded from two separate [` jar `{.calibre4}]{.calibre_17} files.

This is much less of an issue than it would be in Java or C# because "loading" a Clojure program almost always[]{#index_split_026.html#filepos357817}[[[[8]{.underline}]{.calibre_10}]{.calibre3}](#index_split_026.html#filepos358280) involves compiling it. Thus, while the high-level policies and low-level details may not be dynamically loaded from [` jar `{.calibre4}]{.calibre_17} files, they are dynamically compiled and loaded from [source]{.italic} files. Therefore, most of the benefits of independently deployable [` jar `{.calibre4}]{.calibre_17} files are preserved.

[[[8]{.underline}]{.calibre_10}](#index_split_026.html#filepos357817). Clojure allows for precompilation in some cases.

However, if you absolutely must have total and complete independent deployability, there is another option. You can use Clojure's protocols and records:

> > [[`(defprotocol device`{.calibre4}\
> > `  (getchar [_])`{.calibre4}\
> > `  (putchar [_ c]))`{.calibre4}]{.calibre_3}]{.calibre_17}

The protocol will become a Java [` interface `{.calibre4}]{.calibre_17} that can be independently compiled into a [` jar `{.calibre4}]{.calibre_17} file for dynamic loading. The implementation of the protocol (shown below) can likewise be independently compiled and loaded:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_163.html#filepos974802)

> > [[`(defrecord str-device [in-atom out-atom]`{.calibre4}\
> > `  device`{.calibre4}\
> > `  (getchar [_]`{.calibre4}\
> > `    (let [c (first @in-atom)]`{.calibre4}\
> > `      (if (nil? c)`{.calibre4}\
> > `        :eof`{.calibre4}\
> > `        (do`{.calibre4}\
> > `          (swap! in-atom rest)`{.calibre4}\
> > `          c))))`{.calibre4}\
> > \
> > `  (putchar [_ c]`{.calibre4}\
> > `    (swap! out-atom str c)))`{.calibre4}\
> > \
> > `(describe "copy"`{.calibre4}\
> > `  (it "can read and write using str-read and str-write"`{.calibre4}\
> > `    (let [device (->str-device (atom "abcdef") (atom nil))]`{.calibre4}\
> > `      (copy device)`{.calibre4}\
> > `      (should= "abcdef" @(:out-atom device)))))`{.calibre4}]{.calibre_3}]{.calibre_17}
>
> []{#index_split_026.html#filepos360177}

Notice the [` ->str-device `{.calibre4}]{.calibre_17} function in the test. That's essentially the Java constructor of the [` str-device `{.calibre4}]{.calibre_17} class that implements the [` device `{.calibre4}]{.calibre_17} protocol. Notice also that I loaded the [` atom `{.calibre4}]{.calibre_17}s into the device as in the previous example.

Indeed, I did not change the [` copy `{.calibre4}]{.calibre_17} program to get this example to work. The [` copy `{.calibre4}]{.calibre_17} program is exactly as it was in the multi-method example. Now that's the OCP at work!

If the protocol/record mechanism of Clojure feels like OO, that's because it is OO. The JVM is an OO foundation, and Clojure fits very nicely upon that foundation.

[[[The Liskov Substitution Principle (LSP)]{.calibre_3}]{.bold}]{.calibre1}

![](images/00312.jpg){.calibre_51}

Any language that supports the OCP must also support the LSP. The two principles are linked because every violation of the LSP is a latent violation of the OCP.

The [LSP]{.italic} was first described by Barbara Liskov in 1988,[]{#index_split_026.html#filepos361727}[[[[9]{.underline}]{.calibre_10}]{.calibre3}](#index_split_026.html#filepos361996) providing a more or less formal definition of a subtype. In essence, she said that a subtype must be substitutable for its base type in any program that uses the base type.

[[[9]{.underline}]{.calibre_10}](#index_split_026.html#filepos361727). Coincidentally, that's the same year that Bertrand Meyer published the OCP.

To clarify that, let us say that we have some program [` pay `{.calibre4}]{.calibre_17} that uses a type [` employee `{.calibre4}]{.calibre_17}:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_164.html#filepos974948)

> > [[`(defn pay [employee pay-date]`{.calibre4}\
> > `  (let [is-payday? (:is-payday employee)`{.calibre4}\
> > `        calc-pay (:calc-pay employee)`{.calibre4}\
> > `        send-paycheck (:send-paycheck employee)]`{.calibre4}\
> > `    (when (is-payday? pay-date)`{.calibre4}\
> > `      (let [paycheck (calc-pay)]`{.calibre4}\
> > `        (send-paycheck paycheck)))))`{.calibre4}]{.calibre_3}]{.calibre_17}

Notice that I'm using the vtable approach to create the type. Notice also that the data within the type is completely hidden from the [` pay `{.calibre4}]{.calibre_17} function. All the [` pay `{.calibre4}]{.calibre_17} function can see is the methods within the [` employee `{.calibre4}]{.calibre_17} type. How much more OO can you get?

Here's the test code that uses this type. Notice that the [` make-test-employee `{.calibre4}]{.calibre_17} function makes an object that uses [duck typing]{.italic} to conform to the [` employee `{.calibre4}]{.calibre_17} type:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_165.html#filepos975094)

> > [[`(defn test-is-payday [employee-data pay-date]`{.calibre4}\
> > `  true)`{.calibre4}\
> > \
> > `(defn test-calc-pay [employee-data]`{.calibre4}\
> > `  (:pay employee-data))`{.calibre4}\
> > \
> > `(defn test-send-paycheck [employee-data paycheck]`{.calibre4}\
> > `  (format "Send %d to: %s at: %s"`{.calibre4}\
> > `          paycheck`{.calibre4}\
> > `          (:name employee-data)`{.calibre4}\
> > `          (:address employee-data)))`{.calibre4}\
> > `(defn make-test-employee [name address pay]`{.calibre4}\
> > `  (let [employee-data {:name name`{.calibre4}\
> > `                       :address address`{.calibre4}\
> > `                       :pay pay}`{.calibre4}\
> > \
> > `        employee {:employee-data employee-data`{.calibre4}\
> > `                  :is-payday (partial test-is-payday`{.calibre4}\
> > `                                      employee-data)`{.calibre4}\
> > `                  :calc-pay (partial test-calc-pay employee-data)`{.calibre4}\
> > `                  :send-paycheck (partial test-send-paycheck`{.calibre4}\
> > `                                          employee-data)}]`{.calibre4}\
> > \
> > `    employee))`{.calibre4}\
> > \
> > `(describe "Payroll"`{.calibre4}\
> > `  (it "pays a salaried employee"`{.calibre4}\
> > `    (should= "Send 100 to: name at: address"`{.calibre4}\
> > `             (pay (make-test-employee "name" "address" 100)`{.calibre4}\
> > `                  :now))))`{.calibre4}]{.calibre_3}]{.calibre_17}
>
> []{#index_split_026.html#filepos365605}

Notice the [` make-test-employee `{.calibre4}]{.calibre_17} function uses the pointer to implementation (PIMPL)[]{#index_split_026.html#filepos365791}[[[[10]{.underline}]{.calibre_10}]{.calibre3}](#index_split_026.html#filepos366206) pattern to hide the data in the [` :employee-data `{.calibre4}]{.calibre_17} field and expose only the methods. Finally, notice that all the polymorphic methods are given the [` employee-data `{.calibre4}]{.calibre_17} as their first arguments. Oh, just so OO! And yet entirely functional.

[[[10]{.underline}]{.calibre_10}](#index_split_026.html#filepos365791). Holding all the data behind a single field to help keep it private. See [[[https://cpppatterns.com/patterns/pimpl.html]{.underline}]{.calibre_10}](https://cpppatterns.com/patterns/pimpl.html).

It should be clear that I could create many different kinds of employee objects and pass them to the [` pay `{.calibre4}]{.calibre_17} function without modifying the [` pay `{.calibre4}]{.calibre_17} function at all. This is the OCP.

However, to achieve that I must be very careful to make sure that every employee object I create conforms to the expectations of the [` pay `{.calibre4}]{.calibre_17} function. If one of those methods does something that [` pay `{.calibre4}]{.calibre_17} doesn't expect, then [` pay `{.calibre4}]{.calibre_17} will malfunction.

For example, this test fails:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_166.html#filepos975240)

> > [[`      (it "does not pay an employee whose payday is not today"`{.calibre4}\
> > `        (should-be-nil`{.calibre4}\
> > `          (pay (make-later-employee "name" "address" 100)`{.calibre4}\
> > `               :now)))`{.calibre4}]{.calibre_3}]{.calibre_17}

It fails because [` make-later-employee `{.calibre4}]{.calibre_17} does not conform to the [` pay `{.calibre4}]{.calibre_17} function's expectations for the :[` is-payday `{.calibre4}]{.calibre_17} method. As you can see below, it returns [` :tomorrow `{.calibre4}]{.calibre_17} instead of [` false `{.calibre4}]{.calibre_17}:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_167.html#filepos975385)

> > [[`(defn make-later-employee [name address pay]`{.calibre4}\
> > `  (let [employee (make-test-employee name address pay)`{.calibre4}\
> > `        is-payday? (partial (fn [_ _] :tomorrow)`{.calibre4}\
> > `                            (:employee-data employee))]`{.calibre4}\
> > `    (assoc employee :is-payday is-payday?)))`{.calibre4}]{.calibre_3}]{.calibre_17}

This is an LSP violation.

Now imagine you were the author of the [` pay `{.calibre4}]{.calibre_17} function, and you were tasked with debugging why certain employees were getting paychecks at the wrong times. You find that many employee objects are using the [` :tomorrow `{.calibre4}]{.calibre_17} convention instead of returning a boolean as they should. What do you do?[]{#index_split_026.html#filepos369446}[[[[11]{.underline}]{.calibre_10}]{.calibre3}](#index_split_026.html#filepos369543)

[[[11]{.underline}]{.calibre_10}](#index_split_026.html#filepos369446). Of course, a statically typed language would solve that particular issue. So would a well-timed call to [` s/valid? `{.calibre4}]{.calibre_17}, given appropriate specs. But that's not the case we are investigating at the moment.

You [could]{.italic} fix all those employees. Or you could add an extra condition to the [` pay `{.calibre4}]{.calibre_17} function:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_168.html#filepos975531)

> > [[`(defn pay [employee pay-date]`{.calibre4}\
> > `  (let [is-payday? (:is-payday employee)`{.calibre4}\
> > `        calc-pay (:calc-pay employee)`{.calibre4}\
> > `        send-paycheck (:send-paycheck employee)]`{.calibre4}\
> > `    (when `{.calibre4}]{.calibre_3}]{.calibre_17}[[`(= true`{.calibre4}]{.calibre_3}]{.bold}[[` (is-payday? pay-date)`{.calibre4}]{.calibre_3}]{.calibre_17}[[`)`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `      (let [paycheck (calc-pay)]`{.calibre4}\
> > `        (send-paycheck paycheck)))))`{.calibre4}]{.calibre_3}]{.calibre_17}
>
> []{#index_split_026.html#filepos370974}

Yeah, that's pretty ugly.[]{#index_split_026.html#filepos371062}[[[[12]{.underline}]{.calibre_10}]{.calibre3}](#index_split_026.html#filepos371277) It's also an OCP violation because we've modified high-level policy due to the misbehavior of a low-level detail.

[[[12]{.underline}]{.calibre_10}](#index_split_026.html#filepos371062). Think long and hard about why that is ugly and why many programmers would be tempted to delete the = true, thus re-exposing the bug.

[[The ISA Rule]{.calibre_3}]{.bold}

The OO literature often uses the term [ISA]{.italic} (pronounced, and meaning, "is a") to describe subtypes. To describe the above situation in those terms we would say that the [` test-employee `{.calibre4}]{.calibre_17} ISA [` employee `{.calibre4}]{.calibre_17}, and the [` later-employee `{.calibre4}]{.calibre_17} ISA [` employee `{.calibre4}]{.calibre_17}. This usage can be confusing.

First, the [` later-employee `{.calibre4}]{.calibre_17} is not an [` employee `{.calibre4}]{.calibre_17} because it does not conform to the expectations of the [` pay `{.calibre4}]{.calibre_17} function; and it is the [` pay `{.calibre4}]{.calibre_17} function, and all the other functions that operate on [` employee `{.calibre4}]{.calibre_17}s, that define what the [` employee `{.calibre4}]{.calibre_17} type is.

But second, and perhaps more important, the term [ISA]{.italic} can be deeply misleading. The ancient and venerable square/rectangle conundrum is often used to make this point.

Let us say that we have an object that describes a rectangle. In Clojure, it might look like this:

> > [[`(defn make-rect [h w]`{.calibre4}\
> > `  {:h h :w w})`{.calibre4}]{.calibre_3}]{.calibre_17}

A simple test of this rectangle object might look like this:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_169.html#filepos975677)

> > [[`(it "calculates proper area after change in size"`{.calibre4}\
> > `  (should= 12 (-> (make-rect 1 1) (set-h 3) (set-w 4) area)))`{.calibre4}]{.calibre_3}]{.calibre_17}

To make this work we'll need the [` set-h `{.calibre4}]{.calibre_17}, [` set-w `{.calibre4}]{.calibre_17}, and [` area `{.calibre4}]{.calibre_17} functions as follows:

> > [[`(defn set-h [rect h]`{.calibre4}\
> > `  (assoc rect :h h))`{.calibre4}\
> > \
> > `(defn set-w [rect w]`{.calibre4}\
> > `  (assoc rect :w w))`{.calibre4}\
> > \
> > `(defn area [rect]`{.calibre4}\
> > `  (* (:h rect) (:w rect)))`{.calibre4}]{.calibre_3}]{.calibre_17}

Nothing here should be surprising. The rectangle object is not mutable. The [` set-h `{.calibre4}]{.calibre_17} and [` set-w `{.calibre4}]{.calibre_17} functions simply create new rectangles with the changed parameters.

So let's flesh this out a bit and create a small system that uses our rectangle. Here are the tests:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_170.html#filepos975822)

> > [[`(describe "Rectangle"`{.calibre4}\
> > `  (it "calculates proper area and perimeter"`{.calibre4}\
> > `    (should= 25 (area (make-rect 5 5)))`{.calibre4}\
> > `    (should= 18 (perimeter (make-rect 4 5)))`{.calibre4}\
> > `    (should= 12 (-> (make-rect 1 1) (set-h 3) (set-w 4) area)))`{.calibre4}\
> > \
> > `  (it "minimally increases area"`{.calibre4}\
> > `    (should= 15 (-> (make-rect 3 4) minimally-increase-area area))`{.calibre4}\
> > `    (should= 24 (-> (make-rect 5 4) minimally-increase-area area))`{.calibre4}\
> > `    `{.calibre4}]{.calibre_3}]{.calibre_17}[[`(should= 20 (-> (make-rect 4 4) minimally-increase-area area))))`{.calibre4}]{.calibre_3}]{.bold}

And here are the functions that pass those tests:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_171.html#filepos975968)

> > [[`(defn perimeter [rect]`{.calibre4}\
> > `  (let [{:keys [h w]}`{.calibre4}]{.calibre_3}]{.calibre_17}[[[[13]{.underline}]{.calibre_10}]{.calibre3}](#index_split_026.html#filepos376708)[[` rect]`{.calibre4}\
> > `    (* 2 (+ h w))))`{.calibre4}\
> > \
> > `(defn minimally-increase-area [rect]`{.calibre4}\
> > `  (let [{:keys [h w]} rect]`{.calibre4}\
> > `    (cond`{.calibre4}\
> > `      (>= h w) (make-rect (inc h) w)`{.calibre4}\
> > `      (> w h) (make-rect h (inc w))`{.calibre4}\
> > `      :else :tilt)))`{.calibre4}]{.calibre_3}]{.calibre_17}
>
> []{#index_split_026.html#filepos376688}

[[[13]{.underline}]{.calibre_10}](#index_split_026.html#filepos376688). This [destructures]{.italic} the map into the named components. In this case, it is equivalent to [` (let [h (:h rect) w (:w rect)] `{.calibre4}]{.calibre_17}...

Again, there's nothing very surprising about this. Perhaps you are confused by the [` minimally-increase-area `{.calibre4}]{.calibre_17} function. This function simply increases the area of the rectangle by the smallest integral amount possible.[]{#index_split_026.html#filepos377293}[[[[14]{.underline}]{.calibre_10}]{.calibre3}](#index_split_026.html#filepos377390)

[[[14]{.underline}]{.calibre_10}](#index_split_026.html#filepos377293). Presuming all the lengths and widths are integers.

So now let's imagine that this system has been in operation for years and has been very successful. But lately the customers of this system have been asking for squares. How do we add squares to our system?

If we apply the ISA rule, we might decide that a square is a rectangle, and therefore, we should make the functions that accept rectangles also accept squares. In Java, we might accomplish this by deriving the class [` Square `{.calibre4}]{.calibre_17} from the class [` Rectangle `{.calibre4}]{.calibre_17}. In Clojure, we can do this by simply creating rectangles with equal sides:

> > [[`(defn make-square [side]`{.calibre4}\
> > `  (make-rect side side))`{.calibre4}]{.calibre_3}]{.calibre_17}

This should bother us slightly because the size of the [` square `{.calibre4}]{.calibre_17} object is the same as the size of the [` rectangle `{.calibre4}]{.calibre_17} object. Objects of type [` square `{.calibre4}]{.calibre_17} ought to be smaller since they don't need both the height and the width. But memory is cheap, and we want to keep things simple, right?

The question is, will all our tests still pass? They should, of course, because our squares are really just rectangles (ah, that's just the ISA rule!).

These tests pass just fine:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_172.html#filepos976114)

> > [[`(should= 36 (area (make-square 6)))`{.calibre4}\
> > `(should= 20 (perimeter (make-square 5)))`{.calibre4}]{.calibre_3}]{.calibre_17}

So does this one, but it's bothersome because somewhere in there, "squareness" got lost:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_173.html#filepos976259)

> > [[`(should= 12 (-> (make-square 1) (set-h 3) (set-w 4) area))`{.calibre4}]{.calibre_3}]{.calibre_17}

The functions [` set-h `{.calibre4}]{.calibre_17} and [` set-w `{.calibre4}]{.calibre_17} do not return a [` square `{.calibre4}]{.calibre_17} when passed a [` square `{.calibre4}]{.calibre_17}. That's a bit strange; but in some bizarre way it actually makes sense. I mean, if you set the height of a [` square `{.calibre4}]{.calibre_17} without changing the width, it's not going to be a [` square `{.calibre4}]{.calibre_17} anymore, right?

If you feel a little itching at the back of your brain right now, you should probably pay attention to it.

Anyway, what about our [` minimally-increase-area `{.calibre4}]{.calibre_17} test? Does it pass?

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_174.html#filepos976404)

> > [[`(should= 30 (-> (make-square 5) minimally-increase-area area))`{.calibre4}]{.calibre_3}]{.calibre_17}

Yes, that passes too. And of course, it should since the function simply increases the height or width as necessary.

So it looks like we're done, and this worked just great!

[[Nope!]{.calibre_3}]{.bold}

Our customer calls us up a few days later, and he's not very happy. He's been trying to minimally increase the area of his squares, and it's just not working.

"When I increase the area of a 5-by-5 square," he bleats, "I get a rectangle back with an area of 30. I need to get a [square]{.italic} back with an area of 36!"

Uh-oh. Looks like we guessed wrong. This is an LSP violation. We created a subtype that does not conform to the expectations of the functions that use the base type. The expectation of [` minimally-increase-area `{.calibre4}]{.calibre_17} is that height and width can be modified independently. According to our customer, that's not true for a [` square `{.calibre4}]{.calibre_17}.

So, what should we do?

We could add a [` :type `{.calibre4}]{.calibre_17} field to the objects and have the constructors put either [` :square `{.calibre4}]{.calibre_17} or [` :rectangle `{.calibre4}]{.calibre_17} into the field, respectively. And of course, then we'd have to put an [` if `{.calibre4}]{.calibre_17} statement into the [` minimally-increase-area `{.calibre4}]{.calibre_17} function. We'd also have to change [` set-h `{.calibre4}]{.calibre_17} and [` set-w `{.calibre4}]{.calibre_17} to change the type to [` :rectangle `{.calibre4}]{.calibre_17}. And those changes violate the OCP, because every violation of the LSP is a latent violation of the OCP.

I'll leave other solutions as an exercise. You might try using multi-methods. You might try using protocols and records. You might try using vtables. Or you might just keep the two types absolutely separate and never pass a [` square `{.calibre4}]{.calibre_17} into a function that takes a [` rectangle `{.calibre4}]{.calibre_17}.

[[The Representative Rule]{.calibre_3}]{.bold}

I prefer this last option. That's because I don't much care for the ISA rule. You see, while it is [geometrically]{.italic} true that a square is a rectangle, none of the objects in my code were actual rectangles or squares. My code had objects that [represented]{.italic} squares and rectangles, but they were [neither]{.italic} squares [nor]{.italic} rectangles. And here's the thing about representatives:

[The representatives of things do not share the]{.italic}

[relationships of the things they represent.]{.italic}

Just because a square is a rectangle in geometry, it does not mean that a [` square `{.calibre4}]{.calibre_17} object in code is a [` rectangle `{.calibre4}]{.calibre_17} object in code. That relationship is not shared because objects of type [` square `{.calibre4}]{.calibre_17} do not behave the way objects of type [` rectangle `{.calibre4}]{.calibre_17} behave.

When you see two objects in the real world that are obviously connected by the phrase "is a," you may be tempted to create a subtype relationship in your code. Be careful with that. You may just run afoul of the representative rule and violate the LSP.

[[[The Interface Segregation Principle (ISP)]{.calibre_3}]{.bold}]{.calibre1}

![](images/00363.jpg){.calibre_52}

The name of this principle derives from its origins in statically typed OO languages. The example I usually use to describe the ISP works quite well for such languages as Java, C#, and C++, because those languages depend upon declared interfaces. In dynamically typed languages like Ruby, Python, JavaScript, and Clojure, those examples don't work particularly well, because in those languages, interfaces are undeclared and are already segregated by duck typing.

For example, consider the following Java interface:

> > [[`interface AtmInteractor {`{.calibre4}\
> > `  void requestAccount();`{.calibre4}\
> > `  void requestAmount();`{.calibre4}\
> > `  void requestPin();`{.calibre4}\
> > `}`{.calibre4}]{.calibre_3}]{.calibre_17}

Here we see three methods bound together in the [` AtmInteractor `{.calibre4}]{.calibre_17} interface. Any user of this interface therefore depends upon all three methods, even if that user only calls one of those methods. Thus, that user depends upon more than it needs. If the signature of one of those methods changes, or if another method is added to that interface, then that user will have to be recompiled and redeployed, making the design unnecessarily fragile.

We solve this weakness in statically typed OO languages by segregating the interfaces as follows:

> > [[`interface AccountInteractor {`{.calibre4}\
> > `  void requestAccount();`{.calibre4}\
> > `}`{.calibre4}\
> > \
> > `interface AmountInteractor {`{.calibre4}\
> > `  void requestAmount();`{.calibre4}\
> > `}`{.calibre4}\
> > \
> > `interface PinInteractor {`{.calibre4}\
> > `  void requestPin();`{.calibre4}\
> > `}`{.calibre4}]{.calibre_3}]{.calibre_17}

Then each user can depend only upon the methods that it needs to call while the implementation can multiply implement those interfaces:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_175.html#filepos976549)

> > [[`public class AtmInteractor implements AccountInteractor,`{.calibre4}\
> > `                                      AmountInteractor,`{.calibre4}\
> > `                                      PinInteractor {`{.calibre4}\
> > `  void requestAccount() {…};`{.calibre4}\
> > `  void requestAmount() {…};`{.calibre4}\
> > `  void requestPin() {…};`{.calibre4}\
> > `}`{.calibre4}]{.calibre_3}]{.calibre_17}
>
> []{#index_split_026.html#filepos388474}

Perhaps the UML diagram in [[[Figure 12.1]{.underline}]{.calibre_10}](#index_split_026.html#filepos388856) will make this clearer. By segregating the interfaces, the three users depend only on the methods that they need; and yet those methods can be implemented by a single class.

![](images/00048.jpg){#filepos388856 .calibre_53}

[[Figure 12.1.]{.bold}]{.calibre3}[ Segregated interfaces]{.calibre3}

In Clojure, we could use one of our duck typing techniques to address this problem:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_176.html#filepos976695)

> > [[`(defmulti request-account :interactor)`{.calibre4}\
> > `(defmulti request-amount :interactor)`{.calibre4}\
> > `(defmulti request-pin :interactor)`{.calibre4}]{.calibre_3}]{.calibre_17}

Those three multi-methods are not bound together under a single declaration. Indeed, they do not even need to be kept together in the same source file. They could instead be declared in modules that are specific to their function. Thus, if the signature of one changed, or if a new multi-method were added, there would be no impact upon the users of []{#index_split_026.html#filepos390014}the multi-methods that were not changed. If they were precompiled,[]{#index_split_026.html#filepos390087}[[[[15]{.underline}]{.calibre_10}]{.calibre3}](#index_split_026.html#filepos390222) they would not require recompilation.

[[[15]{.underline}]{.calibre_10}](#index_split_026.html#filepos390087). Clojure allows modules to be precompiled for faster loading.

This means that in dynamically typed languages, like Clojure, it is easier to avoid depending on things you don't need. But that doesn't mean that the principle doesn't apply.

[[Don't Depend on Things You Don't Need]{.calibre_3}]{.bold}

Back to the name. The word [Interface]{.italic} in [Interface Segregation Principle]{.italic} is not tied solely to the interface classes in Java, C#, and C++. Rather, it applies to the generic meaning of the word. The "interface" of a module is simply the list of all the access points within that module.

Java and C# (and, by strong convention, C++) are class-based languages in which there is a strong coupling between classes and source files. Java in particular demands that each source file be named after the sole public class declared within that source file. This automatically sets up the conditions that the ISP is trying to avoid. Groups of methods are coupled together into a single module that users will depend upon, even if they don't depend upon every one of those methods. Thus, unless the designer is careful, those users will depend upon things they don't need.

Dynamically typed languages like Ruby, Python, and Clojure do not have this class-to-module constraint. You can declare anything you like within any source file you like. You can write the entire application in a single source file if you like\![]{#index_split_026.html#filepos392002}[[[[16]{.underline}]{.calibre_10}]{.calibre3}](#index_split_026.html#filepos392247) Therefore, it is even easier in those languages to set up the conditions that will cause users of a module to depend upon things they don't need.

[[[16]{.underline}]{.calibre_10}](#index_split_026.html#filepos392002). Not recommended. ;-)

This is not a situation that is specific to functional languages. It is also not a situation from which functional languages are immune. Designers can easily pollute the interfaces of their modules with all kinds of access points that the majority of their users don't need.

[[Why?]{.calibre_3}]{.bold}

Why do we care about depending on modules that have more than we need? Why should it bother us if our module only uses one of the ten functions in another module?

In statically typed languages the cost can be severe because a change to one of the functions we don't use can force our module to be recompiled and redeployed. If our module is just one of many modules in a binary component (like a [` jar `{.calibre4}]{.calibre_17} file), then that entire component will need to be redeployed. Those are couplings that every serious designer should be careful about.

In dynamically typed languages, the cost is reduced but is not zero. In Clojure, for example, there is a strict requirement[]{#index_split_026.html#filepos393622}[[[[17]{.underline}]{.calibre_10}]{.calibre3}](#index_split_026.html#filepos393984) that the source code dependencies between modules must be acyclic. The more functions that a module contains, the more outgoing and incoming source code dependencies impinge upon that module and thus the greater the probability that it will participate in a cycle.

[[[17]{.underline}]{.calibre_10}](#index_split_026.html#filepos393622). We'll encounter this in [[[Chapter 17]{.underline}]{.calibre_10}](#index_split_034.html#filepos691643), [[[Wa-Tor]{.underline}]{.calibre_10}](#index_split_034.html#filepos691643).

But possibly the best reason for caring about these dependencies is that a module structure that limits extraneous dependencies is [cogent]{.italic}. It is an indication that intelligent human beings have cared enough to separate the concerns and lower the coupling. The readers of your code will thank you for that care.

[[Conclusion]{.calibre_3}]{.bold}

The real meaning of the ISP is:

[Gather together the things that are used together.]{.italic}

[Separate those things that are used separately.]{.italic}

[Don't depend on things you don't need.]{.italic}

[[[The Dependency Inversion Principle (DIP)]{.calibre_3}]{.bold}]{.calibre1}

![](images/00050.jpg){.calibre_54}

Of the SOLID principles, one could say that the OCP is the moral heart, the SRP is the organizing force, while the LSP and the ISP are caution signs surrounding the potholes created by carelessness. That leaves the DIP, which is the underlying mechanism behind all the others. In almost every case when we find a principle violation, the solution involves the inversion of one or more critical dependencies.

In decades long past, software was constructed with a completely constrained and parallel dependency structure. Source code dependencies paralleled runtime dependencies. The structure looked like [[[Figure 12.2]{.underline}]{.calibre_10}](#index_split_026.html#filepos396164).

![](images/00133.jpg){#filepos396164 .calibre_55}

[[Figure 12.2.]{.bold}]{.calibre3}[ The ancient parallel dependency structure]{.calibre3}

The dashed arrows are runtime dependencies. They show that high-level modules call mid-level modules, which call low-level modules. The solid arrows are source code dependencies. They show that each source code module depends upon the modules it calls. Those source code dependencies were statements like [` #include `{.calibre4}]{.calibre_17}, [` import `{.calibre4}]{.calibre_17}, [` require `{.calibre4}]{.calibre_17}, and [` using `{.calibre4}]{.calibre_17} that mentioned the name of the downstream source file.

In those ancient days of yore, those two kinds of dependencies were always[]{#index_split_026.html#filepos397120}[[[[18]{.underline}]{.calibre_10}]{.calibre3}](#index_split_026.html#filepos397473) parallel to each other. If module [` X `{.calibre4}]{.calibre_17} had a runtime dependency on module [` Y `{.calibre4}]{.calibre_17}, it also had a source code dependency on module [` Y `{.calibre4}]{.calibre_17}.

[[[18]{.underline}]{.calibre_10}](#index_split_026.html#filepos397120). Well, not quite always. In the late '50s and early '60s, Herculean efforts were expended by operating system engineers to invert a few, very strategic dependencies in order to create the abstraction of device independence. They had no tool other than explicit pointers to functions, so they were very, very careful.

This meant that high-level policy was inextricably dependent upon low-level detail. Think hard about the implications of that statement.

But in the late '60s, Ole-Johan Dahl and Kristen Nygaard moved a data structure[]{#index_split_026.html#filepos398209}[[[[19]{.underline}]{.calibre_10}]{.calibre3}](#index_split_026.html#filepos398566) in the ALGOL compiler from the stack to the heap and discovered OO.[]{#index_split_026.html#filepos398370}[[[[20]{.underline}]{.calibre_10}]{.calibre3}](#index_split_026.html#filepos398776) And with that discovery came the ability for programmers to invert dependencies easily and safely.

[[[19]{.underline}]{.calibre_10}](#index_split_026.html#filepos398209). The data structure was the stack frame of function calls. The language they created was Simula 67.

[[[20]{.underline}]{.calibre_10}](#index_split_026.html#filepos398370). The history of the invention of Simula is fascinating. It is briefly described in the 1972 book [Structured Programming]{.italic} by Edsger W. Dijkstra, Ole-Johan Dahl, and C. A. R. Hoare (Academic Press), and in much more detail in the paper "The Development of the Simula Languages" by Dahl and Nygaard ([[[https://hannemyr.com/cache/knojd_acm78.pdf]{.underline}]{.calibre_10}](https://hannemyr.com/cache/knojd_acm78.pdf)).

It took another 25 years before OO languages started to move into the mainstream. But since then, virtually all programmers have been able to effortlessly break that parallel dependence. They do it as shown in [[[Figure 12.3]{.underline}]{.calibre_10}](#index_split_026.html#filepos399704).

![](images/00331.jpg){#filepos399704 .calibre_56}

[[Figure 12.3.]{.bold}]{.calibre3}[ Inverting the dependency by inserting an interface]{.calibre3}

[` HL1 `{.calibre4}]{.calibre_17} has a runtime dependency on [` F() `{.calibre4}]{.calibre_17} within [` ML1 `{.calibre4}]{.calibre_17}; but [` HL1 `{.calibre4}]{.calibre_17} has no source code dependency, either direct or transitive, upon [` ML1 `{.calibre4}]{.calibre_17}. Instead, they both depend upon the interface [` I `{.calibre4}]{.calibre_17}.[]{#index_split_026.html#filepos400414}[[[[21]{.underline}]{.calibre_10}]{.calibre3}](#index_split_026.html#filepos400511)

[[[21]{.underline}]{.calibre_10}](#index_split_026.html#filepos400414). In dynamically typed languages, the interface [` I `{.calibre4}]{.calibre_17} would not exist as a source code module. Rather, it would be a duck type that [` HL1 `{.calibre4}]{.calibre_17} and [` ML1 `{.calibre4}]{.calibre_17} would conform to.

This ability to take any source code dependency and invert it provides us with an immense amount of power. We can easily and safely arrange the source code dependencies of our software to ensure that high-level modules [do not]{.italic} depend upon low-level modules.

This allows us to create structures like that shown in [[[Figure 12.4]{.underline}]{.calibre_10}](#index_split_026.html#filepos401437).

![](images/00285.jpg){#filepos401437 .calibre_57}

[[Figure 12.4.]{.bold}]{.calibre3}[ Plug-in structure]{.calibre3}

Here we see the high-level business rules have runtime dependencies upon the user interface (UI) and the database but have no source code dependencies on those modules. This application of the DIP means that the UI and database are [plug-ins]{.italic} to the business rules and could easily be replaced with different implementations without affecting the business rules, thereby conforming to the OCP.

Of course, what's really going on is that the UI and the database are implementing interfaces contained within the business rules. The business rules operate upon those interfaces, allowing the flow of control to go outward toward the UI and database while keeping the source code dependencies inverted inward toward the business rules (see [[[Figure 12.5]{.underline}]{.calibre_10}](#index_split_026.html#filepos402586)).

![](images/00247.jpg){#filepos402586 .calibre_58}

[[Figure 12.5.]{.bold}]{.calibre3}[ The interfaces within the business rules allow plug-ins.]{.calibre3}

Notice that all the dependencies point toward abstractions. This leads us to one way to describe the DIP:

[Where possible, point all source code dependencies at abstractions.]{.italic}

[[A Blast from the Past]{.calibre_3}]{.bold}

But enough theory. Let's see this at work. I'm going to borrow a nostalgic example from my friend and mentor, Martin Fowler. He presented this [Video Store]{.italic}[]{#index_split_026.html#filepos403404}[[[[22]{.underline}]{.calibre_10}]{.calibre3}](#index_split_026.html#filepos403721) example in the first edition of his wonderful book, [Refactoring]{.italic}.[]{#index_split_026.html#filepos403569}[[[[23]{.underline}]{.calibre_10}]{.calibre3}](#index_split_026.html#filepos404005) Of course, I'm going to use Clojure instead of Java.

[[[22]{.underline}]{.calibre_10}](#index_split_026.html#filepos403404). Video killed the radio store and the Internet killed the video store. Yes, boys and girls, there was a time when we would go to the video store to rent videotapes and DVDs.

[[[23]{.underline}]{.calibre_10}](#index_split_026.html#filepos403569). Addison-Wesley, 1999.

Here are the tests:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_177.html#filepos976840)

> > [[`(describe "Video Store"`{.calibre4}\
> > `  (with customer (make-customer "Fred"))`{.calibre4}\
> > \
> > `  (it "makes statement for a single new release"`{.calibre4}\
> > `    (should= (str "Rental Record for Fred\n"`{.calibre4}\
> > `                  "\tThe Cell\t9.0\n"`{.calibre4}\
> > `                  "You owed 9.0\n"`{.calibre4}\
> > `                  "You earned 2 frequent renter points\n")`{.calibre4}\
> > `             (make-statement`{.calibre4}\
> > `               (make-rental-order`{.calibre4}\
> > `                 @customer`{.calibre4}\
> > `                 [(make-rental`{.calibre4}\
> > `                    (make-movie "The Cell" :new-release)`{.calibre4}\
> > `                    3)]))))`{.calibre4}\
> > \
> > `  (it "makes statement for two new releases"`{.calibre4}\
> > `    (should= (str "Rental Record for Fred\n"`{.calibre4}\
> > `                  "\tThe Cell\t9.0\n"`{.calibre4}\
> > `                  "\tThe Tigger Movie\t9.0\n"`{.calibre4}\
> > `                  "You owed 18.0\n"`{.calibre4}\
> > `                  "You earned 4 frequent renter points\n")`{.calibre4}\
> > `             (make-statement`{.calibre4}\
> > `               (make-rental-order`{.calibre4}\
> > `                 @customer`{.calibre4}\
> > `                 [(make-rental`{.calibre4}\
> > `                    (make-movie "The Cell" :new-release)`{.calibre4}\
> > `                    3)`{.calibre4}\
> > `                  (make-rental`{.calibre4}\
> > `                    (make-movie "The Tigger Movie" :new-release)`{.calibre4}\
> > `                    3)]))))`{.calibre4}\
> > \
> > `  (it "makes statement for one childrens movie"`{.calibre4}\
> > `    (should= (str "Rental Record for Fred\n"`{.calibre4}\
> > `                  "\tThe Tigger Movie\t1.5\n"`{.calibre4}\
> > `                  "You owed 1.5\n"`{.calibre4}\
> > `                  "You earned 1 frequent renter points\n")`{.calibre4}\
> > `             (make-statement`{.calibre4}\
> > `               (make-rental-order`{.calibre4}\
> > `                 @customer`{.calibre4}\
> > `                 [(make-rental`{.calibre4}\
> > `                    (make-movie "The Tigger Movie" :childrens)`{.calibre4}\
> > `                    3)]))))`{.calibre4}\
> > \
> > `  (it "makes statement for several regular movies"`{.calibre4}\
> > `    (should= (str "Rental Record for Fred\n"`{.calibre4}\
> > `                  "\tPlan 9 from Outer Space\t2.0\n"`{.calibre4}\
> > `                  "\t8 1/2\t2.0\n"`{.calibre4}\
> > `                  "\tEraserhead\t3.5\n"`{.calibre4}\
> > `                  "You owed 7.5\n"`{.calibre4}\
> > `                  "You earned 3 frequent renter points\n")`{.calibre4}\
> > `             (make-statement`{.calibre4}\
> > `               (make-rental-order`{.calibre4}\
> > `                 @customer`{.calibre4}\
> > `                 [(make-rental`{.calibre4}\
> > `                    (make-movie "Plan 9 from Outer Space" :regular)`{.calibre4}\
> > `                    1)`{.calibre4}\
> > `                  (make-rental`{.calibre4}\
> > `                    (make-movie "8 1/2", :regular)`{.calibre4}\
> > `                    2)`{.calibre4}\
> > `                  (make-rental`{.calibre4}\
> > `                    (make-movie "Eraserhead" :regular)`{.calibre4}\
> > `                    3)])))))`{.calibre4}]{.calibre_3}]{.calibre_17}

From these tests, you should be able to determine what this application does. Customers rent videos for a certain number of days. The price and the reward points are apparently calculated based upon the type of the video and the number of days they are rented. There seem to be three types of videos: [` :regular `{.calibre4}]{.calibre_17}, [` :new-release `{.calibre4}]{.calibre_17}, and [` :childrens `{.calibre4}]{.calibre_17}.

Here is the code that passes these tests:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_179.html#filepos977132)

> > [[`(defn make-customer [name]`{.calibre4}\
> > `  {:name name})`{.calibre4}\
> > \
> > `(defn make-movie [title type]`{.calibre4}\
> > `  {:title title`{.calibre4}\
> > `   :type type})`{.calibre4}\
> > \
> > `(defn make-rental [movie days]`{.calibre4}\
> > `  {:movie movie`{.calibre4}\
> > `   :days days})`{.calibre4}\
> > \
> > `(defn make-rental-order [customer rentals]`{.calibre4}\
> > `  {:customer customer`{.calibre4}\
> > `   :rentals rentals})`{.calibre4}\
> > \
> > `(defn determine-amount [rental]`{.calibre4}\
> > `  (let [{:keys [movie days]} rental`{.calibre4}\
> > `        type (:type movie)]`{.calibre4}\
> > `    (condp = type`{.calibre4}\
> > `      :regular`{.calibre4}\
> > `      (if (> days 2)`{.calibre4}\
> > `        (+ 2.0 (* (- days 2) 1.5))`{.calibre4}\
> > `        2.0)`{.calibre4}\
> > \
> > `      :new-release`{.calibre4}\
> > `      (* 3.0 days)`{.calibre4}\
> > \
> > `      :childrens`{.calibre4}\
> > `      (if (> days 3)`{.calibre4}\
> > `        (+ 1.5 (* (- days 3) 1.5))`{.calibre4}\
> > `        1.5))))`{.calibre4}\
> > \
> > `(defn determine-points [rental]`{.calibre4}\
> > `  (let [{:keys [movie days]} rental`{.calibre4}\
> > `          type (:type movie)]`{.calibre4}\
> > `    (if (and (= type :new-release)`{.calibre4}\
> > `             (> days 1))`{.calibre4}\
> > `      2`{.calibre4}\
> > `      1)))`{.calibre4}\
> > \
> > `(defn make-detail [rental]`{.calibre4}\
> > `  (let [title (:title (:movie rental))`{.calibre4}\
> > `        price (determine-amount rental)]`{.calibre4}\
> > `    (format "\t%s\t%.1f" title price)))`{.calibre4}\
> > \
> > `(defn make-details [rentals]`{.calibre4}\
> > `  (map make-detail rentals))`{.calibre4}\
> > \
> > `(defn make-footer [rentals]`{.calibre4}\
> > `  (let [owed (reduce + (map determine-amount rentals))`{.calibre4}\
> > `        points (reduce + (map determine-points rentals))]`{.calibre4}\
> > `    (format`{.calibre4}\
> > `      "\nYou owed %.1f\nYou earned %d frequent renter points\n"`{.calibre4}\
> > `      owed points)))`{.calibre4}\
> > \
> > `(defn make-statement [rental-order]`{.calibre4}\
> > `  (let [{:keys [name]} (:customer rental-order)`{.calibre4}\
> > `        {:keys [rentals]} rental-order`{.calibre4}\
> > `        header (format "Rental Record for %s\n" name)`{.calibre4}\
> > `        details (string/join "\n" (make-details rentals))`{.calibre4}\
> > `        footer (make-footer rentals)]`{.calibre4}\
> > `    (str header details footer)))`{.calibre4}]{.calibre_3}]{.calibre_17}
>
> []{#index_split_026.html#filepos411531}

If you read the first edition of [Refactoring]{.italic}, this should look pretty familiar. In essence, we have a simple report generator that calculates and formats a statement for a rental order.

The very first thing you should have noticed is the horrific SRP violation in the tests. Those tests couple the business rules with the construction and formatting of the statement. If someone from marketing decides to make even a trivial change to the statement format, all the tests will fail.

Consider, for example, the effects of changing the statement to begin with the words "Rental Statement for" instead of "Rental Record for."

This SRP violation makes the tests very fragile. To fix this we need to separate the tests that specify the format of the report from the tests that specify the business rules.

To do this I'm going to split the tests into three different modules: one for testing the calculations, another for the formatting, and the last for integration.

Here is the [` statement-calculator `{.calibre4}]{.calibre_17} test. From now on, I'll include all the [` ns `{.calibre4}]{.calibre_17}[]{#index_split_026.html#filepos412960}[[[[24]{.underline}]{.calibre_10}]{.calibre3}](#index_split_026.html#filepos413149) statements so that you can see the names of the modules and their source code dependencies.

[[[24]{.underline}]{.calibre_10}](#index_split_026.html#filepos412960). [` ns `{.calibre4}]{.calibre_17} stands for namespace. These statements generally appear at the start of every Clojure module and define the module's name and its dependencies.

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_181.html#filepos977424)

> > [[`(ns video-store.statement-calculator-spec`{.calibre4}\
> > `  (:require [speclj.core :refer :all]`{.calibre4}\
> > `            [video-store.statement-calculator :refer :all]))`{.calibre4}\
> > `(declare customer)`{.calibre4}\
> > \
> > `(describe "Rental Statement Calculation"`{.calibre4}\
> > `  (with customer (make-customer "Fred"))`{.calibre4}\
> > \
> > `  (it "makes statement for a single new release"`{.calibre4}\
> > `    (should= {:customer-name "Fred"`{.calibre4}\
> > `              :movies [{:title "The Cell"`{.calibre4}\
> > `                        :price 9.0}]`{.calibre4}\
> > `              :owed 9.0`{.calibre4}\
> > `              :points 2}`{.calibre4}\
> > `             (make-statement-data`{.calibre4}\
> > `               (make-rental-order`{.calibre4}\
> > `                 @customer`{.calibre4}\
> > `                 [(make-rental`{.calibre4}\
> > `                    (make-movie "The Cell" :new-release)`{.calibre4}\
> > `                    3)]))))`{.calibre4}\
> > \
> > `  (it "makes statement for two new releases"`{.calibre4}\
> > `    (should= {:customer-name "Fred",`{.calibre4}\
> > `              :movies [{:title "The Cell", :price 9.0}`{.calibre4}\
> > `                       {:title "The Tigger Movie", :price 9.0}],`{.calibre4}\
> > `              :owed 18.0,`{.calibre4}\
> > `              :points 4}`{.calibre4}\
> > `             (make-statement-data`{.calibre4}\
> > `               (make-rental-order`{.calibre4}\
> > `                 @customer`{.calibre4}\
> > `                 [(make-rental`{.calibre4}\
> > `                    (make-movie "The Cell" :new-release)`{.calibre4}\
> > `                    3)`{.calibre4}\
> > `                  (make-rental`{.calibre4}\
> > `                    (make-movie "The Tigger Movie" :new-release)`{.calibre4}\
> > `                    3)]))))`{.calibre4}\
> > \
> > `  (it "makes statement for one childrens movie"`{.calibre4}\
> > `    (should= {:customer-name "Fred",`{.calibre4}\
> > `              :movies [{:title "The Tigger Movie", :price 1.5}],`{.calibre4}\
> > `              :owed 1.5,`{.calibre4}\
> > `              :points 1}`{.calibre4}\
> > `             (make-statement-data`{.calibre4}\
> > `               (make-rental-order`{.calibre4}\
> > `                 @customer`{.calibre4}\
> > `                 [(make-rental`{.calibre4}\
> > `                    (make-movie "The Tigger Movie" :childrens)`{.calibre4}\
> > `                    3)]))))`{.calibre4}\
> > \
> > `  (it "makes statement for several regular movies"`{.calibre4}\
> > `    (should= {:customer-name "Fred",`{.calibre4}\
> > `              :movies [{:title "Plan 9 from Outer Space",`{.calibre4}\
> > `                        :price 2.0}`{.calibre4}\
> > `                       {:title "8 1/2", :price 2.0}`{.calibre4}\
> > `                       {:title "Eraserhead", :price 3.5}],`{.calibre4}\
> > `              :owed 7.5,`{.calibre4}\
> > `              :points 3}`{.calibre4}\
> > `             (make-statement-data`{.calibre4}\
> > `               (make-rental-order`{.calibre4}\
> > `                 @customer`{.calibre4}\
> > `                 [(make-rental`{.calibre4}\
> > `                    (make-movie "Plan 9 from Outer Space"`{.calibre4}\
> > `                                :regular)`{.calibre4}\
> > `                    1)`{.calibre4}\
> > `                  (make-rental`{.calibre4}\
> > `                    (make-movie "8 1/2", :regular)`{.calibre4}\
> > `                    2)`{.calibre4}\
> > `                  (make-rental`{.calibre4}\
> > `                    (make-movie "Eraserhead" :regular)`{.calibre4}\
> > `                    3)])))))`{.calibre4}]{.calibre_3}]{.calibre_17}

What we've done here is replace the formatted rental statement with a data structure that contains all the data that goes into the statement. This allows us to separate the formatting from the calculation, as shown in the [` statement-calculator `{.calibre4}]{.calibre_17} implementation:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_183.html#filepos977716)

> > [[`(ns video-store.statement-calculator)`{.calibre4}\
> > \
> > `(defn make-customer [name]`{.calibre4}\
> > `  {:name name})`{.calibre4}\
> > \
> > `(defn make-movie [title type]`{.calibre4}\
> > `  {:title title`{.calibre4}\
> > `   :type type})`{.calibre4}\
> > \
> > `(defn make-rental [movie days]`{.calibre4}\
> > `  {:movie movie`{.calibre4}\
> > `   :days days})`{.calibre4}\
> > \
> > `(defn make-rental-order [customer rentals]`{.calibre4}\
> > `  {:customer customer`{.calibre4}\
> > `   :rentals rentals})`{.calibre4}\
> > \
> > `(defn determine-amount [rental]`{.calibre4}\
> > `  (let [{:keys [movie days]} rental`{.calibre4}\
> > `        type (:type movie)]`{.calibre4}\
> > `    (condp = type`{.calibre4}\
> > `      :regular`{.calibre4}\
> > `      (if (> days 2)`{.calibre4}\
> > `        (+ 2.0 (* (- days 2) 1.5))`{.calibre4}\
> > `        2.0)`{.calibre4}\
> > \
> > `      :new-release`{.calibre4}\
> > `      (* 3.0 days)`{.calibre4}\
> > \
> > `      :childrens`{.calibre4}\
> > `      (if (> days 3)`{.calibre4}\
> > `        (+ 1.5 (* (- days 3) 1.5))`{.calibre4}\
> > `        1.5))))`{.calibre4}\
> > \
> > `(defn determine-points [rental]`{.calibre4}\
> > `  (let [{:keys [movie days]} rental`{.calibre4}\
> > `        type (:type movie)]`{.calibre4}\
> > `    (if (and (= type :new-release)`{.calibre4}\
> > `             (> days 1))`{.calibre4}\
> > `      2`{.calibre4}\
> > `      1)))`{.calibre4}\
> > \
> > `(defn make-statement-data [rental-order]`{.calibre4}\
> > `  (let [{:keys [name]} (:customer rental-order)`{.calibre4}\
> > `        {:keys [rentals]} rental-order]`{.calibre4}\
> > `    {:customer-name name`{.calibre4}\
> > `     :movies (for [rental rentals]`{.calibre4}\
> > `               {:title (:title (:movie rental))`{.calibre4}\
> > `                :price (determine-amount rental)})`{.calibre4}\
> > `     :owed (reduce + (map determine-amount rentals))`{.calibre4}\
> > `     :points (reduce + (map determine-points rentals))}))`{.calibre4}]{.calibre_3}]{.calibre_17}

This is a bit simpler than before and is nicely encapsulated. Notice the [` ns `{.calibre4}]{.calibre_17} statement shows that this module has no source code dependencies. Everything in the module is about the calculation of the data that goes into the statement. However, there is nothing here that hints at the formatting of the statement.

The formatting test is quite simple:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_184.html#filepos977863)

> > [[`(ns video-store.statement-formatter-spec`{.calibre4}\
> > `  (:require [speclj.core :refer :all]`{.calibre4}\
> > `            [video-store.statement-formatter :refer :all]))`{.calibre4}\
> > \
> > `(describe "Rental Statement Format"`{.calibre4}\
> > `  (it "Formats a rental statement"`{.calibre4}\
> > `    (should= (str "Rental Record for CUSTOMER\n"`{.calibre4}\
> > `                  "\tMOVIE\t9.9\n"`{.calibre4}\
> > `                  "You owed 100.0\n"`{.calibre4}\
> > `                  "You earned 99 frequent renter points\n")`{.calibre4}\
> > `             (format-rental-statement`{.calibre4}\
> > `               {:customer-name "CUSTOMER"`{.calibre4}\
> > `                :movies [{:title "MOVIE"`{.calibre4}\
> > `                          :price 9.9}]`{.calibre4}\
> > `                :owed 100.0`{.calibre4}\
> > `                :points 99}))))`{.calibre4}]{.calibre_3}]{.calibre_17}

This should be self-explanatory. We're just making sure that we can format the data produced by the [` statement-calculator `{.calibre4}]{.calibre_17} module. The implementation is also very simple:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_185.html#filepos978009)

> > [[`(ns video-store.statement-formatter)`{.calibre4}\
> > \
> > `(defn format-rental-statement [statement-data]`{.calibre4}\
> > `  (let [customer-name (:customer-name statement-data)`{.calibre4}\
> > `        movies (:movies statement-data)`{.calibre4}\
> > `        owed (:owed statement-data)`{.calibre4}\
> > `        points (:points statement-data)]`{.calibre4}\
> > `    (str`{.calibre4}\
> > `      (format "Rental Record for %s\n" customer-name)`{.calibre4}\
> > `      (apply str`{.calibre4}\
> > `             (for [movie movies]`{.calibre4}\
> > `               (format "\t%s\t%.1f\n"`{.calibre4}\
> > `                       (:title movie)`{.calibre4}\
> > `                       (:price movie))))`{.calibre4}\
> > `      (format "You owed %.1f\n" owed)`{.calibre4}\
> > `      (format "You earned %d frequent renter points\n" points))))`{.calibre4}]{.calibre_3}]{.calibre_17}

Again, we have a nicely encapsulated module with no source code dependencies.

To make sure that both of these modules work together as they should, I added a simple integration test:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_186.html#filepos978155)

> > [[`(ns video-store.integration-specs`{.calibre4}\
> > `  (:require [speclj.core :refer :all]`{.calibre4}\
> > `            [video-store.statement-formatter :refer :all]`{.calibre4}\
> > `            [video-store.statement-calculator :refer :all]))`{.calibre4}\
> > \
> > `(describe "Integration Tests"`{.calibre4}\
> > `  (it "formats a statement for several regular movies"`{.calibre4}\
> > `    (should= (str "Rental Record for Fred\n"`{.calibre4}\
> > `                  "\tPlan 9 from Outer Space\t2.0\n"`{.calibre4}\
> > `                  "\t8 1/2\t2.0\n"`{.calibre4}\
> > `                  "\tEraserhead\t3.5\n"`{.calibre4}\
> > `                  "You owed 7.5\n"`{.calibre4}\
> > `                  "You earned 3 frequent renter points\n")`{.calibre4}\
> > `             (format-rental-statement`{.calibre4}\
> > `               (make-statement-data`{.calibre4}\
> > `                 (make-rental-order`{.calibre4}\
> > `                   (make-customer "Fred")`{.calibre4}\
> > `                   [(make-rental`{.calibre4}\
> > `                      (make-movie`{.calibre4}\
> > `                        "Plan 9 from Outer Space" :regular)`{.calibre4}\
> > `                      1)`{.calibre4}\
> > `                    (make-rental`{.calibre4}\
> > `                      (make-movie "8 1/2", :regular)`{.calibre4}\
> > `                      2)`{.calibre4}\
> > `                    (make-rental`{.calibre4}\
> > `                      (make-movie "Eraserhead" :regular)`{.calibre4}\
> > `                      3)]))))))`{.calibre4}]{.calibre_3}]{.calibre_17}
>
> []{#index_split_026.html#filepos425856}

This is much better from an SRP point of view. If the marketing folks make trivial changes to the format of the report, only the formatting and integration tests will break. None of the calculation tests will break. That might not seem like a big win in a toy example like this. But in a real-world application where the tests would number in the thousands, this is a very big win indeed.

We are also protected from business rule changes. If the finance people decide they need to change the way prices are calculated, the formatting test will be immune, and only the calculation and integration tests will be affected.

[[A DIP Violation]{.calibre_3}]{.bold}

While all this winning was going on, did you happen to notice the DIP violation? You might have missed it because it's not in the production code. It's in the integration test.

Look at the [` ns `{.calibre4}]{.calibre_17} statement. Do you see those two lines that mention the [` statement-formatter `{.calibre4}]{.calibre_17} and the [` statement-calculator `{.calibre4}]{.calibre_17}? Those lines create source code dependencies on the concrete implementations of those modules. That's a high-level policy depending on a concrete low-level detail. That's a definitional DIP violation.

Perhaps this puzzles you. How can a test be a high-level policy? Aren't tests as low level as you can get? Aren't they the ultimate details?

Yes, that's true. But integration tests in particular are stand-ins for high-level policy. Look at that integration test again. It does precisely what the high-level policy of the application would have to do. It calls [` make-statement-data `{.calibre4}]{.calibre_17} and passes the result to [` format-rental-statement `{.calibre4}]{.calibre_17}. And since both of those functions are concrete implementations, our high-level production code will have the same DIP violation as our integration test.

Do we always pay attention to the DIP in our tests? It is always wise to be aware. It may not always be wise to force compliance. Some tests are best left coupled to low-level implementations. However, if you want your test suites to be robust and flexible and if you don't want a hundred tests to break when you change one small thing in the production code, then keeping an eye on the coupling between your tests and the production code is a good idea.[]{#index_split_026.html#filepos428673}[[[[25]{.underline}]{.calibre_10}]{.calibre3}](#index_split_026.html#filepos428770)

[[[25]{.underline}]{.calibre_10}](#index_split_026.html#filepos428673). I spend a lot of time on this topic in my book [Clean Craftsmanship]{.italic} (Addison-Wesley, 2021).

But perhaps you are still not convinced. So let's add a new feature. Sometimes we want the statement to be displayed on a text terminal, and sometimes we want it on a browser. So we need text and HTML versions of [` format-rental-statement `{.calibre4}]{.calibre_17}.

Let's also add one more new feature. Some of our stores are offering a "buy two, get one free" policy. So, if you rent three videos, you will only be charged for the two most expensive ones.

If we were implementing this in an OO language, we would likely be tempted to create two new abstract classes or interfaces. The [` StatementFormatter `{.calibre4}]{.calibre_17} abstraction would have a [` format-rental-statement `{.calibre4}]{.calibre_17} method that would be implemented in both the [` TextFormatter `{.calibre4}]{.calibre_17} and [` HTMLFormatter `{.calibre4}]{.calibre_17} implementations. Likewise, the [` StatementPolicy `{.calibre4}]{.calibre_17} abstraction would implement the [` make-statement-data `{.calibre4}]{.calibre_17} function in both [` NormalPolicy `{.calibre4}]{.calibre_17} and [` BuyTwoGetOneFreePolicy `{.calibre4}]{.calibre_17}.

We can easily mimic this design by using any one of the three approaches that we discussed in the section on the OCP. We could build vtables for the two abstractions. Or we could use [` defprotocol `{.calibre4}]{.calibre_17} and [` defrecord `{.calibre4}]{.calibre_17} to build actual Java interfaces and implementations. Or, finally, we could use multi-methods.

Let's see what the multi-method approach looks like. Keep in mind that this is a child-sized problem posing as an adult situation. What you'll see me do here is meant to show how much larger problems can be designed and partitioned.

In the end, as shown in [[[Figure 12.6]{.underline}]{.calibre_10}](#index_split_026.html#filepos431358), I split the whole system up into eleven modules, three of which are tests.

![](images/00198.jpg){#filepos431358 .calibre_59}

[[Figure 12.6.]{.bold}]{.calibre3}[ Splitting the Video Store application into modules]{.calibre3}

[[[Figure 12.6]{.underline}]{.calibre_10}](#index_split_026.html#filepos431358) looks like a UML diagram for an OO solution. The dependency inversion should be obvious. The [` order-processing `{.calibre4}]{.calibre_17} module is the highest-level policy. It depends upon two abstractions. The [` statement-formatter `{.calibre4}]{.calibre_17} is an interface, whereas the [` statement-policy `{.calibre4}]{.calibre_17} is an abstract class with one implemented method.

If you are confused at my use of OO vernacular to describe a functional program in Clojure, you shouldn't be. The OO words I'm using have very direct analogies in the functional world.

The [` statement-formatter `{.calibre4}]{.calibre_17} interface is implemented by the [` text-formatter `{.calibre4}]{.calibre_17} and the [` HTML-formatter `{.calibre4}]{.calibre_17}. The [` statement-policy `{.calibre4}]{.calibre_17} abstract class is implemented by the [` normal-statement-policy `{.calibre4}]{.calibre_17}. The [` buy-two-get-one-free-policy `{.calibre4}]{.calibre_17} implementation derives from [` normal-statement-policy `{.calibre4}]{.calibre_17} but overrides one of its methods. The mechanisms behind all this "inheritance" will become clear in a moment.

The tests appear at the bottom. They are marked with [` <T> `{.calibre4}]{.calibre_17}. They use a little utility module named [` constructors `{.calibre4}]{.calibre_17} that knows how to build the basic data structures. Then each uses its particular portion of the production code to test what it needs.

Now let's look at the source code. Pay special attention to the [` ns `{.calibre4}]{.calibre_17} statements and notice that they match the arrows on the UML diagram.

Let's begin with the [` constructors `{.calibre4}]{.calibre_17}. They are pretty self-explanatory:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_187.html#filepos978301)

> > [[`(ns video-store.constructors)`{.calibre4}\
> > \
> > `(defn make-customer [name]`{.calibre4}\
> > `  {:name name})`{.calibre4}\
> > \
> > `(defn make-movie [title type]`{.calibre4}\
> > `  {:title title`{.calibre4}\
> > `   :type type})`{.calibre4}\
> > \
> > `(defn make-rental [movie days]`{.calibre4}\
> > `  {:movie movie`{.calibre4}\
> > `   :days days})`{.calibre4}\
> > \
> > `(defn make-rental-order [customer rentals]`{.calibre4}\
> > `  {:customer customer`{.calibre4}\
> > `   :rentals rentals})`{.calibre4}]{.calibre_3}]{.calibre_17}

The [` constructors `{.calibre4}]{.calibre_17} have no outgoing dependencies in the [` ns `{.calibre4}]{.calibre_17} statement and simply build plain old Clojure data structures.

The integration test is in the [` integration-specs `{.calibre4}]{.calibre_17} module:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_188.html#filepos978447)

> > [[`(ns video-store.integration-specs`{.calibre4}\
> > `  (:require [speclj.core :refer :all]`{.calibre4}\
> > `            [video-store.constructors :refer :all]`{.calibre4}\
> > `            [video-store.text-statement-formatter :refer :all]`{.calibre4}\
> > `            [video-store.normal-statement-policy :refer :all]`{.calibre4}\
> > `            [video-store.order-processing :refer :all]))`{.calibre4}\
> > \
> > `(declare rental-order)`{.calibre4}\
> > \
> > `(describe "Integration Tests"`{.calibre4}\
> > `  (with rental-order (make-rental-order`{.calibre4}\
> > `                       (make-customer "Fred")`{.calibre4}\
> > `                       [(make-rental`{.calibre4}\
> > `                          (make-movie`{.calibre4}\
> > `                            "Plan 9 from Outer Space"`{.calibre4}\
> > `                            :regular)`{.calibre4}\
> > `                          1)`{.calibre4}\
> > `                        (make-rental`{.calibre4}\
> > `                          (make-movie "8 1/2", :regular)`{.calibre4}\
> > `                          2)`{.calibre4}\
> > `                        (make-rental`{.calibre4}\
> > `                          (make-movie "Eraserhead" :regular)`{.calibre4}\
> > `                          3)]))`{.calibre4}\
> > `  (it "formats a text statement"`{.calibre4}\
> > `    (should= (str "Rental Record for Fred\n"`{.calibre4}\
> > `                  "\tPlan 9 from Outer Space\t2.0\n"`{.calibre4}\
> > `                  "\t8 1/2\t2.0\n"`{.calibre4}\
> > `                  "\tEraserhead\t3.5\n"`{.calibre4}\
> > `                  "You owed 7.5\n"`{.calibre4}\
> > `                  "You earned 3 frequent renter points\n")`{.calibre4}\
> > `             (process-order`{.calibre4}\
> > `               (make-normal-policy)`{.calibre4}\
> > `               (make-text-formatter)`{.calibre4}\
> > `               @rental-order))))`{.calibre4}]{.calibre_3}]{.calibre_17}

This is pretty much the same as before, except that the [` ns `{.calibre4}]{.calibre_17} statement has all the explicit source code dependencies. This test still violates the DIP, but only because it must call the [` make-normal-policy `{.calibre4}]{.calibre_17} and [` make-text-formatter `{.calibre4}]{.calibre_17} constructors within the corresponding modules. I suppose I could have used an [Abstract Factory]{.italic}[]{#index_split_026.html#filepos437981}[[[[26]{.underline}]{.calibre_10}]{.calibre3}](#index_split_026.html#filepos438185) to break those last dependencies; but it didn't seem worth the effort for a test that tests integration.

[[[26]{.underline}]{.calibre_10}](#index_split_026.html#filepos437981). See [[[Chapter 16]{.underline}]{.calibre_10}](#index_split_032.html#filepos560846), "[[[Design Patterns Review]{.underline}]{.calibre_10}](#index_split_032.html#filepos560846)."

The other two tests are more specific. Pay special attention to the fact that their source code dependencies only pull in what they need:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_189.html#filepos978593)

> > [[`(ns video-store.statement-formatter-spec`{.calibre4}\
> > `  (:require [speclj.core :refer :all]`{.calibre4}\
> > `            [video-store.statement-formatter :refer :all]`{.calibre4}\
> > `            [video-store.text-statement-formatter :refer :all]`{.calibre4}\
> > `            [video-store.html-statement-formatter :refer :all]))`{.calibre4}\
> > \
> > `(declare statement-data)`{.calibre4}\
> > `(describe "Rental Statement Format"`{.calibre4}\
> > `  (with statement-data {:customer-name "CUSTOMER"`{.calibre4}\
> > `                        :movies [{:title "MOVIE"`{.calibre4}\
> > `                                  :price 9.9}]`{.calibre4}\
> > `                        :owed 100.0`{.calibre4}\
> > `                        :points 99})`{.calibre4}\
> > `  (it "Formats a text rental statement"`{.calibre4}\
> > `    (should= (str "Rental Record for CUSTOMER\n"`{.calibre4}\
> > `                  "\tMOVIE\t9.9\n"`{.calibre4}\
> > `                  "You owed 100.0\n"`{.calibre4}\
> > `                  "You earned 99 frequent renter points\n")`{.calibre4}\
> > `             (format-rental-statement`{.calibre4}\
> > `               (make-text-formatter)`{.calibre4}\
> > `               @statement-data`{.calibre4}\
> > `               )))`{.calibre4}\
> > \
> > `  (it "Formats an html rental statement"`{.calibre4}\
> > `      (should= (str`{.calibre4}\
> > `                 "<h1>Rental Record for CUSTOMER</h1>"`{.calibre4}\
> > `                 "<table>"`{.calibre4}\
> > `                 "<tr><td>MOVIE</td><td>9.9</td></tr>"`{.calibre4}\
> > `                 "</table>"`{.calibre4}\
> > `                 "You owed 100.0<br>"`{.calibre4}\
> > `                 "You earned <b>99</b> frequent renter points")`{.calibre4}\
> > `               (format-rental-statement`{.calibre4}\
> > `                 (make-html-formatter)`{.calibre4}\
> > `                 @statement-data))))`{.calibre4}]{.calibre_3}]{.calibre_17}

The [` statement-formatter-spec `{.calibre4}]{.calibre_17} tests the two different formats. The format is specified by the first argument of the [` format-rental-statement `{.calibre4}]{.calibre_17} function. That argument is created by the [` make-text-formatter `{.calibre4}]{.calibre_17} and [` make-html-formatter `{.calibre4}]{.calibre_17} functions, which are implemented in the appropriate modules, as you'll see.

The last test is the [` statement-policy-spec `{.calibre4}]{.calibre_17}:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_190.html#filepos978739)

> > [[`(ns video-store.statement-policy-spec`{.calibre4}\
> > `  (:require`{.calibre4}\
> > `    [speclj.core :refer :all]`{.calibre4}\
> > `    [video-store.constructors :refer :all]`{.calibre4}\
> > `    [video-store.statement-policy :refer :all]`{.calibre4}\
> > `    [video-store.normal-statement-policy :refer :all]`{.calibre4}\
> > `    [video-store.buy-two-get-one-free-policy :refer :all]))`{.calibre4}\
> > \
> > `(declare customer normal-policy formatter)`{.calibre4}\
> > `(declare new-release-1 new-release-2 childrens)`{.calibre4}\
> > `(declare regular-1 regular-2 regular-3)`{.calibre4}\
> > \
> > `(describe "Rental Statement Calculation"`{.calibre4}\
> > `  (with customer (make-customer "CUSTOMER"))`{.calibre4}\
> > `  (with normal-policy (make-normal-policy))`{.calibre4}\
> > `  (with new-release-1 (make-movie "new release 1" :new-release))`{.calibre4}\
> > `  (with new-release-2 (make-movie "new release 2" :new-release))`{.calibre4}\
> > `  (with childrens (make-movie "childrens" :childrens))`{.calibre4}\
> > `  (with regular-1 (make-movie "regular 1" :regular))`{.calibre4}\
> > `  (with regular-2 (make-movie "regular 2" :regular))`{.calibre4}\
> > `  (with regular-3 (make-movie "regular 3" :regular))`{.calibre4}\
> > `  (context "normal policy"`{.calibre4}\
> > `    (it "makes statement for a single new release"`{.calibre4}\
> > `      (should= {:customer-name "CUSTOMER"`{.calibre4}\
> > `                :movies [{:title "new release 1"`{.calibre4}\
> > `                          :price 9.0}]`{.calibre4}\
> > `                :owed 9.0`{.calibre4}\
> > `                :points 2}`{.calibre4}\
> > `               (make-statement-data`{.calibre4}\
> > `                 @normal-policy`{.calibre4}\
> > `                 (make-rental-order`{.calibre4}\
> > `                   @customer`{.calibre4}\
> > `                   [(make-rental @new-release-1 3)]))))`{.calibre4}\
> > \
> > `    (it "makes statement for two new releases"`{.calibre4}\
> > `      (should= {:customer-name "CUSTOMER",`{.calibre4}\
> > `                :movies [{:title "new release 1", :price 9.0}`{.calibre4}\
> > `                         {:title "new release 2", :price 9.0}],`{.calibre4}\
> > `                :owed 18.0,`{.calibre4}\
> > `                :points 4}`{.calibre4}\
> > `               (make-statement-data`{.calibre4}\
> > `                 @normal-policy`{.calibre4}\
> > `                 (make-rental-order`{.calibre4}\
> > `                   @customer`{.calibre4}\
> > `                   [(make-rental @new-release-1 3)`{.calibre4}\
> > `                    (make-rental @new-release-2 3)]))))`{.calibre4}\
> > \
> > `    (it "makes statement for one childrens movie"`{.calibre4}\
> > `      (should= {:customer-name "CUSTOMER",`{.calibre4}\
> > `                :movies [{:title "childrens", :price 1.5}],`{.calibre4}\
> > `                :owed 1.5,`{.calibre4}\
> > `                :points 1}`{.calibre4}\
> > `               (make-statement-data`{.calibre4}\
> > `                 @normal-policy`{.calibre4}\
> > `                 (make-rental-order`{.calibre4}\
> > `                   @customer`{.calibre4}\
> > `                   [(make-rental @childrens 3)]))))`{.calibre4}\
> > \
> > `    (it "makes statement for several regular movies"`{.calibre4}\
> > `      (should= {:customer-name "CUSTOMER",`{.calibre4}\
> > `                :movies [{:title "regular 1", :price 2.0}`{.calibre4}\
> > `                         {:title "regular 2", :price 2.0}`{.calibre4}\
> > `                         {:title "regular 3", :price 3.5}],`{.calibre4}\
> > `                :owed 7.5,`{.calibre4}\
> > `                :points 3}`{.calibre4}\
> > `               (make-statement-data`{.calibre4}\
> > `                 @normal-policy`{.calibre4}\
> > `                 (make-rental-order`{.calibre4}\
> > `                   @customer`{.calibre4}\
> > `                   [(make-rental @regular-1 1)`{.calibre4}\
> > `                    (make-rental @regular-2 2)`{.calibre4}\
> > `                    (make-rental @regular-3 3)])))))`{.calibre4}\
> > \
> > `  (context "Buy two get one free policy"`{.calibre4}\
> > `    (it "makes statement for several regular movies"`{.calibre4}\
> > `      (should= {:customer-name "CUSTOMER",`{.calibre4}\
> > `                :movies [{:title "regular 1", :price 2.0}`{.calibre4}\
> > `                         {:title "regular 2", :price 2.0}`{.calibre4}\
> > `                         {:title "new release 1", :price 3.0}],`{.calibre4}\
> > `                :owed 5.0,`{.calibre4}\
> > `                :points 3}`{.calibre4}\
> > `               (make-statement-data`{.calibre4}\
> > `                 (make-buy-two-get-one-free-policy)`{.calibre4}\
> > `                 (make-rental-order`{.calibre4}\
> > `                   @customer`{.calibre4}\
> > `                   [(make-rental @regular-1 1)`{.calibre4}\
> > `                    (make-rental @regular-2 1)`{.calibre4}\
> > `                    (make-rental @new-release-1 1)]))))))`{.calibre4}]{.calibre_3}]{.calibre_17}
>
> []{#index_split_026.html#filepos447489}

The [` statement-policy-spec `{.calibre4}]{.calibre_17} tests the various pricing rules. You've seen the first batch already. The last test checks the buy two, get one free policy used by some stores. Notice that the policy is passed into the [` make-statement-data `{.calibre4}]{.calibre_17} function and is created by the [` make-normal-policy `{.calibre4}]{.calibre_17} and [` make-buy-two-get-one-free-policy `{.calibre4}]{.calibre_17} functions.

Now, on to the production code. We begin with the [` order-processing `{.calibre4}]{.calibre_17} module:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_192.html#filepos979032)

> > [[`(ns video-store.order-processing`{.calibre4}\
> > `  (:require [video-store.statement-formatter :refer :all]`{.calibre4}\
> > `            [video-store.statement-policy :refer :all]))`{.calibre4}\
> > \
> > `(defn process-order [policy formatter order]`{.calibre4}\
> > `  (->> order`{.calibre4}\
> > `       (make-statement-data policy)`{.calibre4}\
> > `       (format-rental-statement formatter)))`{.calibre4}]{.calibre_3}]{.calibre_17}

There's not much to it. Notice the source code dependencies only refer to the [` statement-formatter `{.calibre4}]{.calibre_17} interface and the [` statement-policy `{.calibre4}]{.calibre_17} abstraction.

The [` statement-formatter `{.calibre4}]{.calibre_17} interface is very simple:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_193.html#filepos979178)

> > [[`(ns video-store.statement-formatter)`{.calibre4}\
> > \
> > `(defmulti format-rental-statement`{.calibre4}\
> > `            (fn [formatter statement-data]`{.calibre4}\
> > `              (:type formatter)))`{.calibre4}]{.calibre_3}]{.calibre_17}

The [` defmulti `{.calibre4}]{.calibre_17} statement is roughly equivalent to creating an abstract []{#index_split_026.html#filepos450008}method in Java or C#. Since this module has nothing but one abstract method, it is roughly equivalent to an interface. The dispatcher function is trivial; it just returns the [` :type `{.calibre4}]{.calibre_17} of the formatter.

The [` statement-policy `{.calibre4}]{.calibre_17} abstraction is a bit more interesting:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_194.html#filepos979324)

> > [[`(ns video-store.statement-policy)`{.calibre4}\
> > \
> > `(defn- policy-movie-dispatch [policy rental]`{.calibre4}\
> > `  [(:type policy) (-> rental :movie :type)])`{.calibre4}\
> > \
> > `(defmulti determine-amount policy-movie-dispatch)`{.calibre4}\
> > `(defmulti determine-points policy-movie-dispatch)`{.calibre4}\
> > `(defmulti total-amount (fn [policy _rentals] (:type policy)))`{.calibre4}\
> > `(defmulti total-points (fn [policy _rentals] (:type policy)))`{.calibre4}\
> > \
> > `(defn make-statement-data [policy rental-order]`{.calibre4}\
> > `  (let [{:keys [name]} (:customer rental-order)`{.calibre4}\
> > `        {:keys [rentals]} rental-order]`{.calibre4}\
> > `    {:customer-name name`{.calibre4}\
> > `     :movies (for [rental rentals]`{.calibre4}\
> > `               {:title (:title (:movie rental))`{.calibre4}\
> > `                :price (determine-amount policy rental)})`{.calibre4}\
> > `     :owed (total-amount policy rentals)`{.calibre4}\
> > `     :points (total-points policy rentals)}))`{.calibre4}]{.calibre_3}]{.calibre_17}

The [` statement-policy `{.calibre4}]{.calibre_17} module has four abstract methods and one implemented method. Notice how it uses the Template Method[]{#index_split_026.html#filepos451916}[[[[27]{.underline}]{.calibre_10}]{.calibre3}](#index_split_026.html#filepos452431) pattern. Notice also that the [` determine-amount `{.calibre4}]{.calibre_17} and [` determine-points `{.calibre4}]{.calibre_17} functions use a dispatch code that is a tuple. That's pretty interesting. It means that we can dispatch those functions based upon two degrees of freedom instead of one. That's something that's hard to do in most OO languages. We'll see it used shortly.

[[[27]{.underline}]{.calibre_10}](#index_split_026.html#filepos451916). See [[[Chapter 17]{.underline}]{.calibre_10}](#index_split_034.html#filepos691643), "[[[Wa-Tor]{.underline}]{.calibre_10}](#index_split_034.html#filepos691643)."

But first let's look at the [` text-statement-formatter `{.calibre4}]{.calibre_17} implementation:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_195.html#filepos979470)

> > [[`(ns video-store.text-statement-formatter`{.calibre4}\
> > `  (:require [video-store.statement-formatter :refer :all]))`{.calibre4}\
> > `(defn make-text-formatter [] {:type ::text})`{.calibre4}\
> > \
> > `(defmethod format-rental-statement`{.calibre4}\
> > `           ::text`{.calibre4}\
> > `           [_formatter statement-data]`{.calibre4}\
> > `  (let [customer-name (:customer-name statement-data)`{.calibre4}\
> > `        movies (:movies statement-data)`{.calibre4}\
> > `        owed (:owed statement-data)`{.calibre4}\
> > `        points (:points statement-data)]`{.calibre4}\
> > `    (str`{.calibre4}\
> > `      (format "Rental Record for %s\n" customer-name)`{.calibre4}\
> > `      (apply str`{.calibre4}\
> > `             (for [movie movies]`{.calibre4}\
> > `               (format "\t%s\t%.1f\n"`{.calibre4}\
> > `                 (:title movie)`{.calibre4}\
> > `                 (:price movie))))`{.calibre4}\
> > `      (format "You owed %.1f\n" owed)`{.calibre4}\
> > `      (format "You earned %d frequent renter points\n" points))))`{.calibre4}]{.calibre_3}]{.calibre_17}

This shouldn't be much of a surprise. I just moved the code over here without much change. Notice the [` make-text-formatter `{.calibre4}]{.calibre_17} function at the top.

The [` html-statement-formatter `{.calibre4}]{.calibre_17} shouldn't be very surprising either:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_196.html#filepos979616)

> > [[`(ns video-store.html-statement-formatter`{.calibre4}\
> > `  (:require [video-store.statement-formatter :refer :all]))`{.calibre4}\
> > \
> > `(defn make-html-formatter [] {:type ::html})`{.calibre4}\
> > \
> > `(defmethod format-rental-statement ::html`{.calibre4}\
> > `  [formatter statement-data]`{.calibre4}\
> > `  (let [customer-name (:customer-name statement-data)`{.calibre4}\
> > `        movies (:movies statement-data)`{.calibre4}\
> > `        owed (:owed statement-data)`{.calibre4}\
> > `        points (:points statement-data)]`{.calibre4}\
> > `    (str`{.calibre4}\
> > `      (format "<h1>Rental Record for %s</h1>" customer-name)`{.calibre4}\
> > `      "<table>"`{.calibre4}\
> > `      (apply str`{.calibre4}\
> > `             (for [movie movies]`{.calibre4}\
> > `               (format "<tr><td>%s</td><td>%.1f</td></tr>"`{.calibre4}\
> > `                       (:title movie) (:price movie))))`{.calibre4}\
> > `      "</table>"`{.calibre4}\
> > `      (format "You owed %.1f<br>" owed)`{.calibre4}\
> > `      (format "You earned <b>%d</b> frequent renter points"`{.calibre4}\
> > `              points))))`{.calibre4}]{.calibre_3}]{.calibre_17}

The more interesting modules are the two policy modules. Let's begin with [` normal-statement-policy `{.calibre4}]{.calibre_17}:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_197.html#filepos979762)

> > [[`(ns video-store.normal-statement-policy`{.calibre4}\
> > `  (:require [video-store.statement-policy :refer :all]))`{.calibre4}\
> > \
> > `(defn make-normal-policy [] {:type ::normal})`{.calibre4}\
> > \
> > `(defmethod determine-amount [::normal :regular] [_policy rental]`{.calibre4}\
> > `  (let [days (:days rental)]`{.calibre4}\
> > `    (if (> days 2)`{.calibre4}\
> > `      (+ 2.0 (* (- days 2) 1.5))`{.calibre4}\
> > `      2.0)))`{.calibre4}\
> > \
> > `(defmethod determine-amount`{.calibre4}\
> > `           [::normal :childrens]`{.calibre4}\
> > `           [_policy rental]`{.calibre4}\
> > `  (let [days (:days rental)]`{.calibre4}\
> > `    (if (> days 3)`{.calibre4}\
> > `      (+ 1.5 (* (- days 3) 1.5))`{.calibre4}\
> > `      1.5)))`{.calibre4}\
> > \
> > `(defmethod determine-amount`{.calibre4}\
> > `           [::normal :new-release]`{.calibre4}\
> > `           [_policy rental]`{.calibre4}\
> > `  (* 3.0 (:days rental)))`{.calibre4}\
> > \
> > `(defmethod determine-points [::normal :regular] [_policy _rental]`{.calibre4}\
> > `  1)`{.calibre4}\
> > \
> > `(defmethod determine-points`{.calibre4}\
> > `           [::normal :new-release]`{.calibre4}\
> > `           [_policy rental]`{.calibre4}\
> > `  (if (> (:days rental) 1) 2 1))`{.calibre4}\
> > \
> > `(defmethod determine-points`{.calibre4}\
> > `           [::normal :childrens]`{.calibre4}\
> > `           [_policy _rental]`{.calibre4}\
> > `  1)`{.calibre4}\
> > \
> > `(defmethod total-amount ::normal [policy rentals]`{.calibre4}\
> > `  (reduce + (map #(determine-amount policy %) rentals)))`{.calibre4}\
> > \
> > `(defmethod total-points ::normal [policy rentals]`{.calibre4}\
> > `  (reduce + (map #(determine-points policy %) rentals)))`{.calibre4}]{.calibre_3}]{.calibre_17}

That's different, isn't it? Look carefully at those [` defmethod `{.calibre4}]{.calibre_17} statements. We've dispatched on both the policy type and the movie type. This isolates the business rules really well.

You might be worried that the two degrees of freedom will create an N\*M problem, leading to a proliferation of the "determine" functions. You'll see how I handle that in a minute.

Notice the [` make-normal-policy `{.calibre4}]{.calibre_17} constructor at the top that was used by our tests.

Now let's look at the [` buy-two-get-one-free-policy `{.calibre4}]{.calibre_17} module:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_199.html#filepos980054)

> > [[`(ns video-store.buy-two-get-one-free-policy`{.calibre4}\
> > `  (:require [video-store.statement-policy :refer :all]`{.calibre4}\
> > `            [video-store.normal-statement-policy :as normal]))`{.calibre4}\
> > \
> > `(derive ::buy-two-get-one-free ::normal/normal)`{.calibre4}\
> > \
> > `(defn make-buy-two-get-one-free-policy []`{.calibre4}\
> > `  {:type ::buy-two-get-one-free})`{.calibre4}\
> > \
> > `(defmethod total-amount`{.calibre4}\
> > `           ::buy-two-get-one-free`{.calibre4}\
> > `           [policy rentals]`{.calibre4}\
> > `  (let [amounts (map #(determine-amount policy %) rentals)]`{.calibre4}\
> > `    (if (> (count amounts) 2)`{.calibre4}\
> > `      (reduce + (drop 1 (sort amounts)))`{.calibre4}\
> > `      (reduce + amounts))))`{.calibre4}]{.calibre_3}]{.calibre_17}
>
> []{#index_split_026.html#filepos460156}

Surprise, surprise! Look at that [` derive `{.calibre4}]{.calibre_17} statement. This is Clojure's way of allowing you to create ISA[]{#index_split_026.html#filepos460365}[[[[28]{.underline}]{.calibre_10}]{.calibre3}](#index_split_026.html#filepos460887) hierarchies. This statement says that a [` ::buy-two-get-one-free `{.calibre4}]{.calibre_17}[]{#index_split_026.html#filepos460565}[[[[29]{.underline}]{.calibre_10}]{.calibre3}](#index_split_026.html#filepos461033) policy is a [` :normal `{.calibre4}]{.calibre_17} policy. The multi-method dispatching mechanism uses hierarchies like this to resolve which [` defmethod `{.calibre4}]{.calibre_17} to dispatch to.

[[[28]{.underline}]{.calibre_10}](#index_split_026.html#filepos460365). Take care to avoid LSP violations!

[[[29]{.underline}]{.calibre_10}](#index_split_026.html#filepos460565). Once again, don't worry about the double colons. They are just a way to scope keywords into a namespace.

What this says to the compiler is that it should use the [` :normal `{.calibre4}]{.calibre_17} implementations unless overridden by a specific [` ::buy-two-get-one-free `{.calibre4}]{.calibre_17} implementation.

Thus, our module only has to override the [` total-amount `{.calibre4}]{.calibre_17} function in order to subtract the least expensive movie if three or more are rented.

[[Conclusion]{.calibre_3}]{.bold}

OK, that's it. We've chopped this system up into 11 modules. Each module is nicely encapsulated. We have inverted the most important source code dependencies so that high-level policies do not depend upon low-level details.

The overall structure looks a lot like an OO program, and yet it is entirely functional.

Nice.

::: {#index_split_026.html#calibre_pb_26 .mbp_pagebreak}
:::

[]{#index_split_027.html}

[[IV]{.calibre_3}]{.calibre2}

[[Functional Pragmatics]{.calibre_3}]{.calibre2}

::: {#index_split_027.html#calibre_pb_27 .mbp_pagebreak}
:::

[]{#index_split_028.html}

[[[13]{.calibre_3}]{.bold}]{.calibre1}

[[[Tests]{.calibre_3}]{.bold}]{.calibre1}

![](images/00090.jpg){.calibre_60}

Throughout this book, you've seen many of the unit tests I have written. In virtually every case, I used the TDD[]{#index_split_028.html#filepos463060}[[[[1]{.underline}]{.calibre_10}]{.calibre3}](#index_split_028.html#filepos463261) discipline of writing my tests and code in a tight loop, with the tests a few seconds ahead of the code.

[[[1]{.underline}]{.calibre_10}](#index_split_028.html#filepos463060). I have written a great deal about this discipline in [Clean Craftsmanship]{.italic} (Addison-Wesley, 2021), [Clean Code]{.italic} (Pearson, 2008), and [Agile Software Development: Principles, Patterns, and Practices]{.italic} (Pearson, 2002). There is also a vast amount of information available on the Web. One of the best books on the topic is [Growing Object-Oriented Software, Guided by Tests]{.italic} by Steve Freeman and Nat Pryce (Addison-Wesley, 2010).

For the most part, those tests were written using a framework called [` speclj `{.calibre4}]{.calibre_17}[]{#index_split_028.html#filepos463976}[[[[2]{.underline}]{.calibre_10}]{.calibre3}](#index_split_028.html#filepos464203) (pronounced "speckle"), written by Micah Martin and others. It is very similar to the RSpec framework that is popular in Ruby.

[[[2]{.underline}]{.calibre_10}](#index_split_028.html#filepos463976). [[[https://github.com/slagyr/speclj]{.underline}]{.calibre_10}](https://github.com/slagyr/speclj)

I have been practicing TDD for well over 20 years now. I've used it in Java, C#, C, C++, Ruby, Python, Lua, Clojure, and a variety of other languages. What I have learned in those decades is that the language does not matter to the discipline. The discipline is the same regardless of the language.

The fact that Clojure is a functional language does not change my testing strategy, nor affect my use of the TDD discipline. I write my Clojure programs test-first the way I write my Java programs test-first. The paradigm doesn't matter. The discipline is universal.

[[[But What about the REPL?]{.calibre_3}]{.bold}]{.calibre1}

Lots of functional programmers say they don't need TDD because they test everything in the REPL. I do lots of experimenting in the REPL too; but in most cases, I encode what I've learned into a test. Tests, like diamonds, are forever. Experiments in the REPL aren't there the morning after.

[[[What about Mocks?]{.calibre_3}]{.bold}]{.calibre1}

[Mocking]{.italic} is a technique used by TDD practitioners to encapsulate their tests away from large swaths of the system. In effect, they create objects, []{#index_split_028.html#filepos465872}called [mocks]{.italic},[]{#index_split_028.html#filepos465899}[[[[3]{.underline}]{.calibre_10}]{.calibre3}](#index_split_028.html#filepos466076) that represent those swaths and use the LSP to substitute the mocks in for them.

[[[3]{.underline}]{.calibre_10}](#index_split_028.html#filepos465899). They are more formally referred to as [test-doubles]{.italic}, but in this context, I'll continue to use the colloquial vernacular.

Since the LSP is viewed as an OO principle, and since mocks in OO languages are based on polymorphic interfaces, it has become something of an urban myth that functional languages do not support mocks.

But as we have seen, the LSP works just as well in a functional language as it does in an OO language, and polymorphic interfaces are generally very easy to create. Thus, the ability to write mocks, in all their various forms, is not at all impeded in a functional language.

As an example, here is a test from my [` more-speech `{.calibre4}]{.calibre_17}[]{#index_split_028.html#filepos467016}[[[[4]{.underline}]{.calibre_10}]{.calibre3}](#index_split_028.html#filepos467156) application that employs a couple of mocks:

[[[4]{.underline}]{.calibre_10}](#index_split_028.html#filepos467016). [[[https://github.com/unclebob/more-speech]{.underline}]{.calibre_10}](https://github.com/unclebob/more-speech)

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_200.html#filepos980185)

> > [[`(it "adds an unrooted article id to a tab"`{.calibre4}\
> > `  (let [message-id 1`{.calibre4}\
> > `        messages {message-id {:tags []}}`{.calibre4}\
> > `        event-context (atom {:text-event-map messages})]`{.calibre4}\
> > `    (reset! ui-context {:event-context event-context})`{.calibre4}\
> > `    (with-redefs [swing-util/add-id-to-tab (stub :add-id-to-tab)`{.calibre4}\
> > `                  swing-util/relaunch (stub :relaunch)]`{.calibre4}\
> > `      (add-article-to-tab 1 "tab" nil)`{.calibre4}\
> > `      (should-have-invoked :relaunch)`{.calibre4}\
> > `      (should-have-invoked :add-id-to-tab`{.calibre4}\
> > `                           {:with ["tab" :selected 1]}))))`{.calibre4}]{.calibre_3}]{.calibre_17}

Don't worry too much about what this test does. Just look down at the [` with-redefs `{.calibre4}]{.calibre_17} statement. This test mocks the [` swing-util/add-id-to-tab `{.calibre4}]{.calibre_17} and [` swing-util/relaunch `{.calibre4}]{.calibre_17} functions to use named stubs. Those stubs are perfect no-ops. They accept any number of arguments and return nothing []{#index_split_028.html#filepos468867}at all.[]{#index_split_028.html#filepos468881}[[[[5]{.underline}]{.calibre_10}]{.calibre3}](#index_split_028.html#filepos469512) But they do remember what happened to them.[]{#index_split_028.html#filepos469017}[[[[6]{.underline}]{.calibre_10}]{.calibre3}](#index_split_028.html#filepos469909) So, down at the bottom, we see that the [` :relaunch `{.calibre4}]{.calibre_17} stub should have been called, and the [` :add-id-to-tab `{.calibre4}]{.calibre_17} stub should have been called with three arguments: [` "tab" `{.calibre4}]{.calibre_17}, [` :selected `{.calibre4}]{.calibre_17}, and [` 1 `{.calibre4}]{.calibre_17}.

[[[5]{.underline}]{.calibre_10}](#index_split_028.html#filepos468881). There are ways to get them to return values, but that's beyond the scope here. Check the [` speclj `{.calibre4}]{.calibre_17} docs ([[[https://github.com/slagyr/speclj]{.underline}]{.calibre_10}](https://github.com/slagyr/speclj)) if you are interested.

[[[6]{.underline}]{.calibre_10}](#index_split_028.html#filepos469017). Which technically makes them spies.

[[[Property-Based Testing]{.calibre_3}]{.bold}]{.calibre1}

One cannot hang out with functional programmers without eventually hearing about QuickCheck and property-based testing. Unfortunately, the topic often arises as a counterargument to TDD. I'm not going to try to support or refute that argument. Instead, I want to show you how very powerful property-based testing is within the TDD discipline.

First of all, what is property-based testing? [Property-based testing]{.italic} is a verification and diagnostic technique that employs the random generation of inputs and a very powerful strategy of defect isolation.

Let's say that I've just written a function that computes the prime factors of a given integer:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_201.html#filepos980331)

> > [[`(defn factors-of [n]`{.calibre4}\
> > `  (loop [factors [] n n divisor 2]`{.calibre4}\
> > `    (if (> n 1)`{.calibre4}\
> > `      (cond`{.calibre4}\
> > `        (> divisor (Math/sqrt n))`{.calibre4}\
> > `        (conj factors n)`{.calibre4}\
> > `        (= 0 (mod n divisor))`{.calibre4}\
> > `        (recur (conj factors divisor)`{.calibre4}\
> > `               (quot n divisor)`{.calibre4}\
> > `               divisor)`{.calibre4}\
> > `        :else`{.calibre4}\
> > `        (recur factors n (inc divisor)))`{.calibre4}\
> > `      factors)))`{.calibre4}]{.calibre_3}]{.calibre_17}

Let's also say that I wrote this function using TDD. Here are my tests:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_202.html#filepos980477)

> > [[`(defn power2 [n]`{.calibre4}\
> > `  (apply * (repeat n 2N)))`{.calibre4}\
> > \
> > `(describe "factor primes"`{.calibre4}\
> > `  (it "factors 1 -> []"`{.calibre4}\
> > `    (should= [] (factors-of 1)))`{.calibre4}\
> > `  (it "factors 2 -> [2]"`{.calibre4}\
> > `    (should= [2] (factors-of 2)))`{.calibre4}\
> > `  (it "factors 3 -> [3]"`{.calibre4}\
> > `    (should= [3] (factors-of 3)))`{.calibre4}\
> > `  (it "factors 4 -> [2 2]"`{.calibre4}\
> > `    (should= [2 2] (factors-of 4)))`{.calibre4}\
> > `  (it "factors 5 -> [5]"`{.calibre4}\
> > `    (should= [5] (factors-of 5)))`{.calibre4}\
> > `  (it "factors 6 -> [2 3]"`{.calibre4}\
> > `    (should= [2 3] (factors-of 6)))`{.calibre4}\
> > `  (it "factors 7 -> [7]"`{.calibre4}\
> > `    (should= [7] (factors-of 7)))`{.calibre4}\
> > `  (it "factors 8 -> [2 2 2]"`{.calibre4}\
> > `    (should= [2 2 2] (factors-of 8)))`{.calibre4}\
> > `  (it "factors 9 -> [3 3]"`{.calibre4}\
> > `    (should= [3 3] (factors-of 9)))`{.calibre4}\
> > `  (it "factors lots"`{.calibre4}\
> > `    (should= [2 2 3 3 5 7 11 11 13]`{.calibre4}\
> > `             (factors-of (* 2 2 3 3 5 7 11 11 13))))`{.calibre4}\
> > `  (it "factors Euler 3"`{.calibre4}\
> > `    (should= [71 839 1471 6857] (factors-of 600851475143)))`{.calibre4}\
> > \
> > `  (it "factors mersenne 2^31-1"`{.calibre4}\
> > `    (should= [2147483647] (factors-of (dec (power2 31))))))`{.calibre4}]{.calibre_3}]{.calibre_17}

Pretty cool, right? But how certain am I that this function actually works? I mean, how do I know that there isn't some horrible corner case where the function fails unexpectedly?

Of course, I may never be perfectly sure about this; but there are some things I can do to make myself a lot more comfortable. One property of the output is that the product of all the factors will equal the input. So why don't I generate a thousand random integers and make sure that the prime factors of each multiply together to equal them.

I can do that like so:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_203.html#filepos980623)

> > [[`(def gen-inputs (gen/large-integer* {:min 1 :max 1E9}))`{.calibre4}\
> > \
> > `(declare n)`{.calibre4}]{.calibre_3}]{.calibre_17}[[[[7]{.underline}]{.calibre_10}]{.calibre3}](#index_split_028.html#filepos475289)[[\
> > \
> > `(describe "properties"`{.calibre4}\
> > `  (it "multiplies out properly"`{.calibre4}\
> > `    (should-be`{.calibre4}\
> > `      :result`{.calibre4}\
> > `      (tc/quick-check`{.calibre4}\
> > `        1000`{.calibre4}\
> > `        (prop/for-all`{.calibre4}\
> > `          [n gen-inputs]`{.calibre4}\
> > `          (let [factors (factors-of n)]`{.calibre4}\
> > `            (= n (reduce * factors))))))))`{.calibre4}]{.calibre_3}]{.calibre_17}
>
> []{#index_split_028.html#filepos475269}

[[[7]{.underline}]{.calibre_10}](#index_split_028.html#filepos475269). A forward declaration of [` n `{.calibre4}]{.calibre_17}.

Here I'm using [` test.check `{.calibre4}]{.calibre_17},[]{#index_split_028.html#filepos475583}[[[[8]{.underline}]{.calibre_10}]{.calibre3}](#index_split_028.html#filepos475984) the property-based testing framework in Clojure that mimics the behavior of QuickCheck. The idea is pretty simple. I've got a generator up there named [` gen-inputs `{.calibre4}]{.calibre_17}. It will generate random integers between 1 and a billion. That ought to be a good enough range.

[[[8]{.underline}]{.calibre_10}](#index_split_028.html#filepos475583). [[[https://clojure.org/guides/test_check_beginner]{.underline}]{.calibre_10}](https://clojure.org/guides/test_check_beginner)

The test tells QuickCheck to run 1,000 times. For each integer, it calculates the prime factors, multiplies them all together, and makes sure that the product equals the input. Nice.

The [` tc/quick-check `{.calibre4}]{.calibre_17} function returns a map with the results. The [` :result `{.calibre4}]{.calibre_17} element of that map will be [` true `{.calibre4}]{.calibre_17} if all the checks passed; and that's what the [` should-be :result `{.calibre4}]{.calibre_17} asserts.

There is another property of the prime factors: They should all be prime. So let's write a function that tests for primality:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_204.html#filepos980769)

> > [[`(defn is-prime? [n]`{.calibre4}\
> > `  (if (= 2 n)`{.calibre4}\
> > `    true`{.calibre4}\
> > `    (loop [candidates (range 2 (inc (Math/sqrt n)))]`{.calibre4}\
> > `      (if (empty? candidates)`{.calibre4}\
> > `        true`{.calibre4}\
> > `        (if (zero? (rem n (first candidates)))`{.calibre4}\
> > `          false`{.calibre4}\
> > `          (recur (rest candidates)))))))`{.calibre4}]{.calibre_3}]{.calibre_17}

That's a pretty traditional, if horribly inefficient, algorithm. Inefficient or not, we can use it to write the property test for the primality of all the factors:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_205.html#filepos980915)

> > [[`(describe "factors"`{.calibre4}\
> > `  (it "they are all prime"`{.calibre4}\
> > `    (should-be`{.calibre4}\
> > `      :result`{.calibre4}\
> > `      (tc/quick-check`{.calibre4}\
> > `        1000`{.calibre4}\
> > `        (prop/for-all`{.calibre4}\
> > `          [n gen-inputs]`{.calibre4}\
> > `          (let [factors (factors-of n)]`{.calibre4}\
> > `            (every? is-prime? factors)))))))`{.calibre4}]{.calibre_3}]{.calibre_17}

OK. So now we know that this function returns a list of integers, each of which is prime, and that when multiplied together equal the input. That's kind of the definition of prime factors.

So this is nice. I can randomly generate a bunch of inputs and then apply property checks to the outputs.

[[[A Diagnostic Technique]{.calibre_3}]{.bold}]{.calibre1}

But I called property-based testing a diagnostic technique, didn't I? So let's look at a more interesting example and I'll show you want I mean.

Remember our Video Store example from the preceding chapter? Let's do some property-based testing on that.

First of all, remember that we wrote a function called [` make-statement-data `{.calibre4}]{.calibre_17} that took a [` policy `{.calibre4}]{.calibre_17} and a [` rental-order `{.calibre4}]{.calibre_17} and generated the [` statement-data `{.calibre4}]{.calibre_17} that we then fed into one of our formatters? So here's the type specification of the [` rental-order `{.calibre4}]{.calibre_17} using [` clojure.spec `{.calibre4}]{.calibre_17}:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_206.html#filepos981061)

> > [[`(s/def ::name string?)`{.calibre4}\
> > `(s/def ::customer (s/keys :req-un [name]))`{.calibre4}\
> > `(s/def ::title string?)`{.calibre4}\
> > `(s/def ::type #{:regular :childrens :new-release})`{.calibre4}\
> > `(s/def ::movie (s/keys :req-un [::title ::type]))`{.calibre4}\
> > `(s/def ::days pos-int?)`{.calibre4}\
> > `(s/def ::rental (s/keys :req-un [::days ::movie]))`{.calibre4}\
> > `(s/def ::rentals (s/coll-of ::rental))`{.calibre4}\
> > `(s/def ::rental-order (s/keys :req-un [::customer ::rentals]))`{.calibre4}]{.calibre_3}]{.calibre_17}

That's not too hard to read. From the bottom up:

::: calibre_11
 
:::

-   A [` :rental-order `{.calibre4}]{.calibre_17} is a map with two elements: [` :customer `{.calibre4}]{.calibre_17} and [` :rentals `{.calibre4}]{.calibre_17}.

-   The [` :rentals `{.calibre4}]{.calibre_17} element is a collection of [` :rental `{.calibre4}]{.calibre_17} items.

-   A [` :rental `{.calibre4}]{.calibre_17} is a map with [` :days `{.calibre4}]{.calibre_17} and [` :movie `{.calibre4}]{.calibre_17} elements.

-   A [` :days `{.calibre4}]{.calibre_17} element is a positive integer.

-   A [` :movie `{.calibre4}]{.calibre_17} element is a map with a [` :title `{.calibre4}]{.calibre_17} and [` :type `{.calibre4}]{.calibre_17}.

-   A [` :type `{.calibre4}]{.calibre_17} is one of [` :regular `{.calibre4}]{.calibre_17}, [` :childrens `{.calibre4}]{.calibre_17}, or [` :new-release `{.calibre4}]{.calibre_17}.

-   A [` :title `{.calibre4}]{.calibre_17} is a string.

-   A [` :customer `{.calibre4}]{.calibre_17} is a map with a single [` :name `{.calibre4}]{.calibre_17} element.

-   A [` :name `{.calibre4}]{.calibre_17} is a string.

With this type specification in place, we can write a generator that produces rental orders that conform to the type. So first, here are the generators:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_207.html#filepos981207)

> > [[`(def gen-customer-name`{.calibre4}\
> > `  (gen/such-that not-empty gen/string-alphanumeric))`{.calibre4}\
> > \
> > `(def gen-customer`{.calibre4}\
> > `  (gen/fmap (fn [name] {:name name}) gen-customer-name))`{.calibre4}\
> > \
> > `(def gen-days (gen/elements (range 1 100)))`{.calibre4}\
> > \
> > `(def gen-movie-type`{.calibre4}\
> > `  (gen/elements [:regular :childrens :new-release]))`{.calibre4}\
> > \
> > `(def gen-movie`{.calibre4}\
> > `  (gen/fmap (fn [[title type]] {:title title :type type})`{.calibre4}\
> > `            (gen/tuple gen/string-alphanumeric gen-movie-type)))`{.calibre4}\
> > \
> > `(def gen-rental`{.calibre4}\
> > `  (gen/fmap (fn [[movie days]] {:movie movie :days days})`{.calibre4}\
> > `            (gen/tuple gen-movie gen-days)))`{.calibre4}\
> > \
> > `(def gen-rentals`{.calibre4}\
> > `  (gen/such-that not-empty (gen/vector gen-rental)))`{.calibre4}\
> > \
> > `(def gen-rental-order`{.calibre4}\
> > `  (gen/fmap (fn [[customer rentals]]`{.calibre4}\
> > `              {:customer customer :rentals rentals})`{.calibre4}\
> > `            (gen/tuple gen-customer gen-rentals)))`{.calibre4}\
> > \
> > `(def gen-policy (gen/elements`{.calibre4}\
> > `                  [(make-normal-policy)`{.calibre4}\
> > `                   (make-buy-two-get-one-free-policy)]))`{.calibre4}]{.calibre_3}]{.calibre_17}

I'm not going to explain the ins and outs of [` clojure.check `{.calibre4}]{.calibre_17} here, but I will walk through what the generators do.

::: calibre_11
 
:::

-   [` gen-policy `{.calibre4}]{.calibre_17} randomly selects one of the two policies.

-   [` gen-rental-order `{.calibre4}]{.calibre_17} creates a map from [` gen-customer `{.calibre4}]{.calibre_17} and [` gen-rentals `{.calibre4}]{.calibre_17}.

-   [` gen-rentals `{.calibre4}]{.calibre_17} creates a vector from [` gen-rentals `{.calibre4}]{.calibre_17} and ensures that it is not empty.

-   [` gen-rental `{.calibre4}]{.calibre_17} creates a map from [` gen-movie `{.calibre4}]{.calibre_17} and [` gen-days `{.calibre4}]{.calibre_17}.

-   [` gen-movie `{.calibre4}]{.calibre_17} creates a map from [` gen/string-alphanumeric `{.calibre4}]{.calibre_17} and [` gen-movie-type `{.calibre4}]{.calibre_17}.

-   [` gen-movie-type `{.calibre4}]{.calibre_17} selects from among the three types.

-   [` gen-days `{.calibre4}]{.calibre_17} selects between integers from 1 to 100.

-   [` gen-customer `{.calibre4}]{.calibre_17} creates a map with a name from [` gen-customer-name `{.calibre4}]{.calibre_17}.

-   [` gen-customer-name `{.calibre4}]{.calibre_17} generates a nonempty alphanumeric string.

Do you notice an eerie similarity between the type specification and the generator? So do I. Here are a few sample outputs from the generator:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_208.html#filepos981353)

> > [[`[`{.calibre4}\
> > ` {:customer {:name "5Q"},`{.calibre4}\
> > `  :rentals [{:movie {:title "", :type :new-release}, :days 52}]}`{.calibre4}\
> > \
> > ` {:customer {:name "3"},`{.calibre4}\
> > `  :rentals [{:movie {:title "", :type :new-release}, :days 51}]}`{.calibre4}\
> > \
> > ` {:customer {:name "XA"},`{.calibre4}\
> > `  :rentals [{:movie {:title "r", :type :regular}, :days 82}`{.calibre4}\
> > `            {:movie {:title "", :type :childrens}, :days 60}]}`{.calibre4}\
> > \
> > ` {:customer {:name "4v"},`{.calibre4}\
> > `  :rentals [{:movie {:title "3", :type :childrens}, :days 29}]}`{.calibre4}\
> > \
> > ` {:customer {:name "0rT"},`{.calibre4}\
> > `  :rentals [{:movie {:title "", :type :regular}, :days 42}`{.calibre4}\
> > `            {:movie {:title "94Y", :type :regular}, :days 34}`{.calibre4}\
> > `            {:movie {:title "D5", :type :new-release},`{.calibre4}\
> > `                     :days 58}]}`{.calibre4}\
> > \
> > ` {:customer {:name "ZFAK"},`{.calibre4}\
> > `  :rentals [{:movie {:title "H8", :type :regular}, :days 92}`{.calibre4}\
> > `            {:movie {:title "d6WS8", :type :regular}, :days 59}`{.calibre4}\
> > `            {:movie {:title "d", :type :regular}, :days 53}`{.calibre4}\
> > `            {:movie {:title "Yj8b7", :type :regular}, :days 58}`{.calibre4}\
> > `            {:movie {:title "Z2q70", :type :childrens},`{.calibre4}\
> > `                     :days 9}]}`{.calibre4}\
> > \
> > ` {:customer {:name "njGB0h"},`{.calibre4}\
> > `  :rentals [{:movie {:title "zk3UaE", :type :regular},`{.calibre4}\
> > `                     :days 53}]}`{.calibre4}\
> > \
> > ` {:customer {:name "wD"},`{.calibre4}\
> > `  :rentals [{:movie {:title "51L", :type :childrens},`{.calibre4}\
> > `             :days 17}]}`{.calibre4}\
> > \
> > ` {:customer {:name "2J5nzN"},`{.calibre4}\
> > `  :rentals [{:movie {:title "", :type :regular}, :days 64}`{.calibre4}\
> > `            {:movie {:title "sA17jv", :type :regular}, :days 85}`{.calibre4}\
> > `            {:movie {:title "27E41n", :type :new-release},`{.calibre4}\
> > `                     :days 85}`{.calibre4}\
> > `            {:movie {:title "Z20", :type :new-release}, :days 68}`{.calibre4}\
> > `            {:movie {:title "8j5B7h6S", :type :regular},`{.calibre4}\
> > `                     :days 76}`{.calibre4}\
> > `            {:movie {:title "vg", :type :childrens}, :days 30}]}`{.calibre4}\
> > \
> > ` {:customer {:name "wk"},`{.calibre4}\
> > `  :rentals [{:movie {:title "Kq6wbGG", :type :childrens},`{.calibre4}\
> > `                     :days 43}`{.calibre4}\
> > `            {:movie {:title "3S2DvUwv", :type :childrens},`{.calibre4}\
> > `                     :days 76}`{.calibre4}\
> > `            {:movie {:title "fdGW", :type :childrens}, :days 42}`{.calibre4}\
> > `            {:movie {:title "aS28X3P", :type :childrens},`{.calibre4}\
> > `                     :days 18}`{.calibre4}\
> > `            {:movie {:title "p", :type :childrens}, :days 83}`{.calibre4}\
> > `            {:movie {:title "xgC", :type :regular}, :days 84}`{.calibre4}\
> > `            {:movie {:title "CQoY", :type :childrens}, :days 23}`{.calibre4}\
> > `            {:movie {:title "38jWmKlhq", :type :regular},`{.calibre4}\
> > `                     :days 96}`{.calibre4}\
> > `            {:movie {:title "Liz8T", :type :regular}, :days 56}]}`{.calibre4}\
> > ` ]`{.calibre4}]{.calibre_3}]{.calibre_17}
>
> []{#index_split_028.html#filepos491788}

Just a bunch of random data that conforms nicely to the type of a [` rental-order `{.calibre4}]{.calibre_17}. But let's check that:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_210.html#filepos981645)

> > [[`(describe "Quick check statement policy"`{.calibre4}\
> > `  (it "generates valid rental orders"`{.calibre4}\
> > `    (should-be`{.calibre4}\
> > `      :result`{.calibre4}\
> > `      (tc/quick-check`{.calibre4}\
> > `        100`{.calibre4}\
> > `        (prop/for-all`{.calibre4}\
> > `          [rental-order gen-rental-order]`{.calibre4}\
> > `          (nil?`{.calibre4}\
> > `            (s/explain-data`{.calibre4}\
> > `              ::constructors/rental-order`{.calibre4}\
> > `              rental-order))))))`{.calibre4}]{.calibre_3}]{.calibre_17}

This is a nice little [` quick-check `{.calibre4}]{.calibre_17} that generates 100 random [` rental-order `{.calibre4}]{.calibre_17} objects and runs them through the [` clojure.spec/explain-data `{.calibre4}]{.calibre_17} function. That function makes sure that each rental order conforms to the [` ::constructors/rental-order `{.calibre4}]{.calibre_17} spec that we saw above. If it does, it returns [` nil `{.calibre4}]{.calibre_17}, which passes the [` quick-check `{.calibre4}]{.calibre_17}.

Now, does [` make-statement-data `{.calibre4}]{.calibre_17} create a valid [` statement-data `{.calibre4}]{.calibre_17} object? Let's check that using the same strategy as above:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_211.html#filepos981791)

> > [[`(s/def ::customer-name string?)`{.calibre4}\
> > `(s/def ::title string?)`{.calibre4}\
> > `(s/def ::price pos?)`{.calibre4}\
> > `(s/def ::movie (s/keys :req-un [::title ::price]))`{.calibre4}\
> > `(s/def ::movies (s/coll-of ::movie))`{.calibre4}\
> > `(s/def ::owed pos?)`{.calibre4}\
> > `(s/def ::points pos-int?)`{.calibre4}\
> > `(s/def ::statement-data (s/keys :req-un [::customer-name`{.calibre4}\
> > `                                         ::movies`{.calibre4}\
> > `                                         ::owed`{.calibre4}\
> > `                                         ::points]))`{.calibre4}\
> > \
> > `(it "produces valid statement data"`{.calibre4}\
> > `  (should-be`{.calibre4}\
> > `    :result`{.calibre4}\
> > `    (tc/quick-check`{.calibre4}\
> > `      100`{.calibre4}\
> > `      (prop/for-all`{.calibre4}\
> > `        [rental-order gen-rental-order`{.calibre4}\
> > `         policy gen-policy]`{.calibre4}\
> > `        (nil?`{.calibre4}\
> > `          (s/explain-data`{.calibre4}\
> > `            ::policy/statement-data`{.calibre4}\
> > `            (make-statement-data policy rental-order)))))))`{.calibre4}]{.calibre_3}]{.calibre_17}
>
> []{#index_split_028.html#filepos495138}

So here we see the [` clojure.spec `{.calibre4}]{.calibre_17} for the [` statement-data `{.calibre4}]{.calibre_17}, and the [` quick-check `{.calibre4}]{.calibre_17} that makes sure that the output of [` make-statement-data `{.calibre4}]{.calibre_17} conforms to it. Nice.

With all this passing, we can be pretty sure that the generator is generating valid rental orders. So now let's get on with the property checks.

One property we could check is to make sure that when [` make-statement-data `{.calibre4}]{.calibre_17} converts a [` rental-order `{.calibre4}]{.calibre_17} into a [` statement-data `{.calibre4}]{.calibre_17} the [` :owed `{.calibre4}]{.calibre_17} member of the [` statement-data `{.calibre4}]{.calibre_17} object is the sum of all the movies itemized in that object.

The [` quick-check `{.calibre4}]{.calibre_17} for this might be as follows:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_212.html#filepos981937)

> > [[`(it "statement data totals are consistent under all policies"`{.calibre4}\
> > `  (should-be`{.calibre4}\
> > `    :result`{.calibre4}\
> > `    (tc/quick-check`{.calibre4}\
> > `      100`{.calibre4}\
> > `      (prop/for-all`{.calibre4}\
> > `        [rental-order gen-rental-order`{.calibre4}\
> > `         policy gen-policy]`{.calibre4}\
> > `        (let [statement-data (make-statement-data`{.calibre4}\
> > `                               policy rental-order)`{.calibre4}\
> > `              prices (map :price (:movies statement-data))`{.calibre4}\
> > `              owed (:owed statement-data)]`{.calibre4}\
> > `          (= owed (reduce + prices)))))))`{.calibre4}]{.calibre_3}]{.calibre_17}

This [` quick-check `{.calibre4}]{.calibre_17} has a bug in it. Can you spot it?

Here's the output when I run it:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_213.html#filepos982083)

> > [[`{:shrunk`{.calibre4}\
> > ` {:total-nodes-visited 45,`{.calibre4}\
> > `  :depth 14,`{.calibre4}\
> > `  :pass? false,`{.calibre4}\
> > `  :result false,`{.calibre4}\
> > `  :result-data nil,`{.calibre4}\
> > `  :time-shrinking-ms 3,`{.calibre4}\
> > `  :smallest`{.calibre4}\
> > `    [{:customer {:name "0"},`{.calibre4}\
> > `      :rentals [{:movie {:title "", :type :regular}, :days 1}`{.calibre4}\
> > `                {:movie {:title "", :type :regular}, :days 1}`{.calibre4}\
> > `                {:movie {:title "", :type :regular}, :days 1}]}`{.calibre4}\
> > `     {:type`{.calibre4}\
> > `      :video-store.`{.calibre4}\
> > `        buy-two-get-one-free-policy/buy-two-get-one-free}]},`{.calibre4}\
> > `  :failed-after-ms 0,`{.calibre4}\
> > `  :num-tests 7,`{.calibre4}\
> > `  :seed 1672092997135,`{.calibre4}\
> > `  :fail`{.calibre4}\
> > `   [{:customer {:name "4s7u"},`{.calibre4}\
> > `     :rentals`{.calibre4}\
> > `     [{:movie {:title "i7jiVAd", :type :childrens}, :days 85}`{.calibre4}\
> > `      {:movie {:title "7MQM", :type :new-release}, :days 26}`{.calibre4}\
> > `      {:movie {:title "qlS4S", :type :new-release}, :days 99}`{.calibre4}\
> > `      {:movie {:title "X", :type :regular}, :days 87}`{.calibre4}\
> > `      {:movie {:title "w1cRbM", :type :regular}, :days 11}`{.calibre4}\
> > `      {:movie {:title "7Hb41O5", :type :regular}, :days 63}`{.calibre4}\
> > `      {:movie {:title "xWc", :type :childrens}, :days 41}]}`{.calibre4}\
> > `    {:type`{.calibre4}\
> > `     :video-store.`{.calibre4}\
> > `       buy-two-get-one-free-policy/buy-two-get-one-free}],`{.calibre4}\
> > `  :result false,`{.calibre4}\
> > `  :result-data nil,`{.calibre4}\
> > `  :failing-size 6,`{.calibre4}\
> > `  :pass? false}`{.calibre4}]{.calibre_3}]{.calibre_17}
>
> []{#index_split_028.html#filepos499491}

Yes, I know this looks awful; but this is where the real magic of [` quick-check `{.calibre4}]{.calibre_17} shines through, so bear with me.

First of all, do you see that top element named [` :shrunk `{.calibre4}]{.calibre_17}? That's a big clue to what is going on here. When [` quick-check `{.calibre4}]{.calibre_17} finds an error, it begins hunting for the smallest randomly generated input that continues to produce that error.

So look at the [` :fail `{.calibre4}]{.calibre_17} element. That's the [` rental-order `{.calibre4}]{.calibre_17} that caused the initial failure. Now look at the [` :smallest `{.calibre4}]{.calibre_17} element within the [` :shrunk `{.calibre4}]{.calibre_17} element. The [` quick-check `{.calibre4}]{.calibre_17} function managed to shrink the [` rental-order `{.calibre4}]{.calibre_17} down while preserving the failure. That's the smallest [` rental-order `{.calibre4}]{.calibre_17} that it could find that failed.

And why did it fail? Notice that there are three movies. Notice also that the policy is [` buy-two-get-one-free `{.calibre4}]{.calibre_17}. Ah, of course, under that policy the sum of the movies is [not]{.italic} equal to the [` :owed `{.calibre4}]{.calibre_17} element.

It's that shrinking behavior that makes property-based testing a diagnostic technique.

[[[Functional]{.calibre_3}]{.bold}]{.calibre1}

So why are tools like [` quick-check `{.calibre4}]{.calibre_17} not more popular in OO languages? Perhaps it's because they work best with pure functions. I imagine it's possible to set up generators and test properties in a mutable system, but it's likely a lot more complicated than in an immutable system.

::: {#index_split_028.html#calibre_pb_28 .mbp_pagebreak}
:::

[]{#index_split_029.html}

[[[14]{.calibre_3}]{.bold}]{.calibre1}

[[[GUI]{.calibre_3}]{.bold}]{.calibre1}

![](images/00137.jpg){.calibre_61}

Over the years, I have used two different GUI frameworks in functional programs. The first is named Quil,[]{#index_split_029.html#filepos502201}[[[[1]{.underline}]{.calibre_10}]{.calibre3}](#index_split_029.html#filepos502711) and it is based upon the popular Java framework named Processing.[]{#index_split_029.html#filepos502359}[[[[2]{.underline}]{.calibre_10}]{.calibre3}](#index_split_029.html#filepos502905) The second is SeeSaw,[]{#index_split_029.html#filepos502473}[[[[3]{.underline}]{.calibre_10}]{.calibre3}](#index_split_029.html#filepos503110) which is based upon the old Java Swing[]{#index_split_029.html#filepos502604}[[[[4]{.underline}]{.calibre_10}]{.calibre3}](#index_split_029.html#filepos503345) framework.

[[[1]{.underline}]{.calibre_10}](#index_split_029.html#filepos502201). [[[www.quil.info]{.underline}]{.calibre_10}](http://www.quil.info)

[[[2]{.underline}]{.calibre_10}](#index_split_029.html#filepos502359). [[[https://processing.org]{.underline}]{.calibre_10}](https://processing.org)

[[[3]{.underline}]{.calibre_10}](#index_split_029.html#filepos502473). [[[https://github.com/clj-commons/seesaw]{.underline}]{.calibre_10}](https://github.com/clj-commons/seesaw)

[[[4]{.underline}]{.calibre_10}](#index_split_029.html#filepos502604). [[[https://en.wikipedia.org/wiki/Swing\_(Java)]{.underline}]{.calibre_10}](https://en.wikipedia.org/wiki/Swing_(Java))

Quil is "functional," which makes it fun and easy to use in a "functional" program. SeeSaw is not functional at all. Indeed, it depends very strongly on mutable state that you must continuously update. This makes it a royal pain to use in a functional program. The difference is startling.

One of the first programs I wrote using Quil was [` spacewar `{.calibre4}]{.calibre_17}. I've mentioned it a few times in this book. If you'd like to see the program in action, you can go to [[[https://github.com/unclebob/spacewar]{.underline}]{.calibre_10}](https://github.com/unclebob/spacewar) where there is a ClojureScript version you can run in your browser. I did not write [` spacewar `{.calibre4}]{.calibre_17} to be used in ClojureScript; but Mike Fikes ported it over in a day or so. It actually works better in my browser than it does in native Clojure on my laptop.

[[[Turtle-Graphics in Quil]{.calibre_3}]{.bold}]{.calibre1}

Walking through the source code of [` spacewar `{.calibre4}]{.calibre_17} is beyond the scope of this book. However, there is a simpler Quil program that I wrote awhile back that is the perfect size. It's [` turtle-graphics `{.calibre4}]{.calibre_17}.[]{#index_split_029.html#filepos505056}[[[[5]{.underline}]{.calibre_10}]{.calibre3}](#index_split_029.html#filepos505152)

[[[5]{.underline}]{.calibre_10}](#index_split_029.html#filepos505056). [[[https://github.com/unclebob/turtle-graphics]{.underline}]{.calibre_10}](https://github.com/unclebob/turtle-graphics)

Turtle graphics[]{#index_split_029.html#filepos505455}[[[[6]{.underline}]{.calibre_10}]{.calibre3}](#index_split_029.html#filepos505926) are a simple set of commands that were invented for the Logo language in the late 1960s. Those commands controlled a robot called a [turtle]{.italic}. The robot sat on a large piece of paper and had a pen that []{#index_split_029.html#filepos505754}could be raised and lowered onto the paper. The robot could be told to move forward or backward a certain distance, or to turn a number of degrees left or right.

[[[6]{.underline}]{.calibre_10}](#index_split_029.html#filepos505455). [[[https://en.wikipedia.org/wiki/Turtle_graphics]{.underline}]{.calibre_10}](https://en.wikipedia.org/wiki/Turtle_graphics)

[[[Figure 14.1]{.underline}]{.calibre_10}](#index_split_029.html#filepos506409) is a picture of the inventor, Seymour Papert, with one of his turtles.

![](images/00146.jpg){#filepos506409 .calibre_62}

[[Figure 14.1.]{.bold}]{.calibre3}[ Seymour Papert with one of his turtles]{.calibre3}[]{#index_split_029.html#filepos506625}[[[[7]{.underline}]{.calibre_10}]{.calibre6}](#index_split_029.html#filepos506721)

[[[7]{.underline}]{.calibre_10}](#index_split_029.html#filepos506625). Courtesy of MIT Museum.

So, for example, if you'd like to draw a square, you might issue these commands:

> > [[`Pen down`{.calibre4}\
> > `Forward 10`{.calibre4}\
> > `Right 90`{.calibre4}\
> > `Forward 10`{.calibre4}\
> > `Right 90`{.calibre4}\
> > `Forward 10`{.calibre4}\
> > `Right 90`{.calibre4}\
> > `Forward 10`{.calibre4}\
> > `Pen up.`{.calibre4}]{.calibre_3}]{.calibre_17}

The original idea was to introduce children to programming by showing them how to control the turtle to draw interesting shapes. I don't know how well this worked for children, but it turned out to be pretty useful for programmers who wanted to draw complex designs on the screen. I once used a Logo system with turtle graphics on the Commodore 64 to write a pretty elaborate Lunar Lander game.

Anyway, awhile back, I thought it would be fun to have a turtle graphics system in Clojure so that I could easily investigate some interesting mathematical and geometric puzzles.

My goal was not to create a turtle graphics console on which you would type commands. Instead, I wanted a turtle graphics API that I could use to write graphical functions in Clojure.

So, for example, I wanted to write a program like this:

> > [[`(defn polygon [theta, len, n]`{.calibre4}\
> > `  (pen-down)`{.calibre4}\
> > `  (speed 1000)`{.calibre4}\
> > `  (dotimes [_ n]`{.calibre4}\
> > `    (forward len)`{.calibre4}\
> > `    (right theta)))`{.calibre4}\
> > \
> > `(defn turtle-script []`{.calibre4}\
> > `  (polygon 144 400 5))`{.calibre4}]{.calibre_3}]{.calibre_17}

That program draws the picture in [[[Figure 14.2]{.underline}]{.calibre_10}](#index_split_029.html#filepos508940). (Notice the little turtle sitting on the left vertex of the star.)

![](images/00114.jpg){#filepos508940 .calibre_63}

[[Figure 14.2.]{.bold}]{.calibre3}[ A star drawn using turtle graphics]{.calibre3}

The [` turtle-script `{.calibre4}]{.calibre_17} function is the entry point for the [` turtle-graphics `{.calibre4}]{.calibre_17} system. You put your drawing commands into it. In this case, I put a call to the [` polygon `{.calibre4}]{.calibre_17} function into it.

Perhaps you've noticed that the [` polygon `{.calibre4}]{.calibre_17} function does not appear to be functional because it doesn't produce a return value from its inputs. Instead, it has the side effect of drawing on the screen. Moreover, each of the commands mutates the state of the turtle. So [` turtle-graphics `{.calibre4}]{.calibre_17} programs are not functional.

And yet, the [` turtle-graphics `{.calibre4}]{.calibre_17} framework is "functional." Or rather, it is about as functional as a GUI program can be.[]{#index_split_029.html#filepos510164}[[[[8]{.underline}]{.calibre_10}]{.calibre3}](#index_split_029.html#filepos510336) After all, the point of a GUI program is to mutate the state of the screen.

[[[8]{.underline}]{.calibre_10}](#index_split_029.html#filepos510164). Although you might find this interesting: [[[https://fsharpforfunandprofit.com/posts/13-ways-of-looking-at-a-turtle/]{.underline}]{.calibre_10}](https://fsharpforfunandprofit.com/posts/13-ways-of-looking-at-a-turtle/).

The [` turtle-graphics `{.calibre4}]{.calibre_17} framework begins by configuring and invoking Quil:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_214.html#filepos982214)

> > [[`(defn ^:export -main [& args]`{.calibre4}\
> > `  (q/defsketch turtle-graphics`{.calibre4}\
> > `               :title "Turtle Graphics"`{.calibre4}\
> > `               :size [1000 1000]`{.calibre4}\
> > `               :setup setup`{.calibre4}\
> > `               :update update-state`{.calibre4}\
> > `               :draw draw-state`{.calibre4}\
> > `               :features [:keep-on-top]`{.calibre4}\
> > `               :middleware [m/fun-mode])`{.calibre4}\
> > `  args)`{.calibre4}]{.calibre_3}]{.calibre_17}

I'm not going to do a full tutorial on Quil here, but there are a few things I should point out. Take note of the [` :setup `{.calibre4}]{.calibre_17}, [` :update `{.calibre4}]{.calibre_17}, and [` :draw `{.calibre4}]{.calibre_17} elements. Each points to a function.

The [` setup `{.calibre4}]{.calibre_17} function will be called once at the start of the program.

The [` draw-state `{.calibre4}]{.calibre_17} function will be called 60 times a second in order to refresh the screen. Everything that should be on the screen must be drawn by the [` draw `{.calibre4}]{.calibre_17} function. The screen doesn't remember anything.

The [` update-state `{.calibre4}]{.calibre_17} function will be called just before the [` draw-state `{.calibre4}]{.calibre_17} function. This function is used to change the state of what is being drawn. Think of it as the function that moves the elements of the screen one 60th of a second into the future.

Think of this like a really simple loop:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_215.html#filepos982360)

> > [[`(loop [state (setup)]`{.calibre4}\
> > `  (draw-state state)`{.calibre4}\
> > `  (recur (update-state state)))`{.calibre4}]{.calibre_3}]{.calibre_17}

If you think of this as a tail recursive loop, then the contents of the screen are the tail recursive values. So even though we are mutating the contents of the screen, we are doing so at the tail of the recursion where the mutation is harmless.[]{#index_split_029.html#filepos513667}[[[[9]{.underline}]{.calibre_10}]{.calibre3}](#index_split_029.html#filepos513944) So, although not purely functional, it is as "functional" as any TCO[]{#index_split_029.html#filepos513832}[[[[10]{.underline}]{.calibre_10}]{.calibre3}](#index_split_029.html#filepos514070) system can be.

[[[9]{.underline}]{.calibre_10}](#index_split_029.html#filepos513667). Mostly harmless.

[[[10]{.underline}]{.calibre_10}](#index_split_029.html#filepos513832). Remember our discussion about tail call optimization back in [[[Chapter 1]{.underline}]{.calibre_10}](#index_split_013.html#filepos61201).

Here's my [` setup `{.calibre4}]{.calibre_17} function:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_216.html#filepos982505)

> > [[`(defn setup []`{.calibre4}\
> > `  (q/frame-rate 60)`{.calibre4}\
> > `  (q/color-mode :rgb)`{.calibre4}\
> > `  (let [state {:turtle (turtle/make)`{.calibre4}\
> > `               :channel channel}]`{.calibre4}\
> > `    (async/go`{.calibre4}\
> > `      (turtle-script)`{.calibre4}\
> > `      (prn "Turtle script complete"))`{.calibre4}\
> > `    state))`{.calibre4}]{.calibre_3}]{.calibre_17}

This starts out pretty simple. It sets the frame rate to 60fps and the color mode to RGB, and it creates the [` state `{.calibre4}]{.calibre_17} object that will be passed to [` update-state `{.calibre4}]{.calibre_17} and [` draw-state `{.calibre4}]{.calibre_17}.

The [` async/go `{.calibre4}]{.calibre_17} function starts up a new lightweight thread in which our [` turtle-script `{.calibre4}]{.calibre_17} will execute.

The [` state `{.calibre4}]{.calibre_17} object is composed of a [` channel `{.calibre4}]{.calibre_17} and the [` turtle `{.calibre4}]{.calibre_17}. We'll talk about the [` channel `{.calibre4}]{.calibre_17} later. For the moment, let's concentrate on the [` turtle `{.calibre4}]{.calibre_17}:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_217.html#filepos982651)

> > [[`(s/def ::position (s/tuple number? number?))`{.calibre4}\
> > `(s/def ::heading (s/and number? #(<= 0 % 360)))`{.calibre4}\
> > `(s/def ::velocity number?)`{.calibre4}\
> > `(s/def ::distance number?)`{.calibre4}\
> > `(s/def ::omega number?)`{.calibre4}\
> > `(s/def ::angle number?)`{.calibre4}\
> > `(s/def ::weight (s/and pos? number?))`{.calibre4}\
> > `(s/def ::state #{:idle :busy})`{.calibre4}\
> > `(s/def ::pen #{:up :down})`{.calibre4}\
> > `(s/def ::pen-start (s/or :nil nil?`{.calibre4}\
> > `                         :pos (s/tuple number? number?)))`{.calibre4}\
> > `(s/def ::line-start (s/tuple number? number?))`{.calibre4}\
> > `(s/def ::line-end (s/tuple number? number?))`{.calibre4}\
> > `(s/def ::line (s/keys :req-un [::line-start ::line-end]))`{.calibre4}\
> > `(s/def ::lines (s/coll-of ::line))`{.calibre4}\
> > `(s/def ::visible boolean?)`{.calibre4}\
> > `(s/def ::speed (s/and int? pos?))`{.calibre4}\
> > `(s/def ::turtle (s/keys :req-un [::position`{.calibre4}\
> > `                                 ::heading`{.calibre4}\
> > `                                 ::velocity`{.calibre4}\
> > `                                 ::distance`{.calibre4}\
> > `                                 ::omega`{.calibre4}\
> > `                                 ::angle`{.calibre4}\
> > `                                 ::pen`{.calibre4}\
> > `                                 ::weight`{.calibre4}\
> > `                                 ::speed`{.calibre4}\
> > `                                 ::lines`{.calibre4}\
> > `                                 ::visible`{.calibre4}\
> > `                                 ::state]`{.calibre4}\
> > `                        :opt-un [::pen-start]))`{.calibre4}\
> > `(defn make []`{.calibre4}\
> > `  {:post [(s/assert ::turtle %)]}`{.calibre4}\
> > `  {:position [0.0 0.0]`{.calibre4}\
> > `   :heading 0.0`{.calibre4}\
> > `   :velocity 0.0`{.calibre4}\
> > `   :distance 0.0`{.calibre4}\
> > `   :omega 0.0`{.calibre4}\
> > `   :angle 0.0`{.calibre4}\
> > `   :pen :up`{.calibre4}\
> > `   :weight 1`{.calibre4}\
> > `   :speed 5`{.calibre4}\
> > `   :visible true`{.calibre4}\
> > `   :lines []`{.calibre4}\
> > `   :state :idle})`{.calibre4}]{.calibre_3}]{.calibre_17}

This shows the type specification of the [` turtle `{.calibre4}]{.calibre_17}, followed by its constructor. Notice that the constructor checks the type as a [` :post `{.calibre4}]{.calibre_17} condition. The elements of the turtle are mostly self-explanatory. There's the XY position, the angular heading, the velocity, the up/down state of the pen, the drawing weight of the pen, the visibility state, and so on. The other elements will come to light soon enough.

How do we draw the turtle?

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_218.html#filepos982798)

> > [[`(defn draw-state [state]`{.calibre4}\
> > `  (q/background 240)`{.calibre4}\
> > `  (q/with-translation`{.calibre4}\
> > `    [500 500]`{.calibre4}\
> > `    (let [{:keys [turtle]} state]`{.calibre4}\
> > `      (turtle/draw turtle))))`{.calibre4}\
> > \
> > `——Turtle module——`{.calibre4}\
> > \
> > `(defn draw [turtle]`{.calibre4}\
> > `  (when (= :down (:pen turtle))`{.calibre4}\
> > `    (q/stroke 0)`{.calibre4}\
> > `    (q/stroke-weight (:weight turtle))`{.calibre4}\
> > `    (q/line (:pen-start turtle) (:position turtle)))`{.calibre4}\
> > \
> > `  (doseq [line (:lines turtle)]`{.calibre4}\
> > `    (q/stroke-weight (:line-weight line))`{.calibre4}\
> > `    (q/line (:line-start line) (:line-end line)))`{.calibre4}\
> > \
> > `  (when (:visible turtle)`{.calibre4}\
> > `    (q/stroke-weight 1)`{.calibre4}\
> > `    (let [[x y] (:position turtle)`{.calibre4}\
> > `          heading (q/radians (:heading turtle))`{.calibre4}\
> > `          base-left (- (/ WIDTH 2))`{.calibre4}\
> > `          base-right (/ WIDTH 2)`{.calibre4}\
> > `          tip HEIGHT]`{.calibre4}\
> > `      (q/stroke 0)`{.calibre4}\
> > `      (q/with-translation`{.calibre4}\
> > `        [x y]`{.calibre4}\
> > `        (q/with-rotation`{.calibre4}\
> > `          [heading]`{.calibre4}\
> > `          (q/line 0 base-left 0 base-right)`{.calibre4}\
> > `          (q/line 0 base-left tip 0)`{.calibre4}\
> > `          (q/line 0 base-right tip 0))))))`{.calibre4}]{.calibre_3}]{.calibre_17}

The [` draw-state `{.calibre4}]{.calibre_17} function, which is called by Quil 60 times each second, sets the background color of the screen to light gray, centers the drawing at (500, 500), and then calls [` turtle/draw `{.calibre4}]{.calibre_17}, which draws the current line in progress and then all the other lines that were previously drawn. Finally, it draws the turtle itself. Notice how Quil helps with translation and rotation.

So how do we update the turtle state?

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_219.html#filepos982944)

> > [[`(defn update-state [{:keys [channel] :as state}]`{.calibre4}\
> > `  (let [turtle (:turtle state)`{.calibre4}\
> > `        turtle (turtle/update-turtle turtle)]`{.calibre4}\
> > `    (assoc state :turtle (handle-commands channel turtle))))`{.calibre4}]{.calibre_3}]{.calibre_17}

The [` update-state `{.calibre4}]{.calibre_17} function calls [` turtle/update-turtle `{.calibre4}]{.calibre_17}. Then it calls [` handle-commands `{.calibre4}]{.calibre_17}, and there's that [` channel `{.calibre4}]{.calibre_17} again. Let's look at [` update-turtle `{.calibre4}]{.calibre_17} first:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_220.html#filepos983089)

> > [[`(defn update-position`{.calibre4}\
> > `  [{:keys [position velocity heading distance] :as turtle}]`{.calibre4}\
> > `  (let [step (min (q/abs velocity) distance)`{.calibre4}\
> > `        distance (- distance step)`{.calibre4}\
> > `        step (if (neg? velocity) (- step) step)`{.calibre4}\
> > `        radians (q/radians heading)`{.calibre4}\
> > `        [x y] position`{.calibre4}\
> > `        vx (* step (Math/cos radians))`{.calibre4}\
> > `        vy (* step (Math/sin radians))`{.calibre4}\
> > `        position [(+ x vx) (+ y vy)]]`{.calibre4}\
> > `    (assoc turtle :position position`{.calibre4}\
> > `                  :distance distance`{.calibre4}\
> > `                  :velocity (if (zero? distance) 0.0 velocity))))`{.calibre4}\
> > \
> > `(defn update-heading [{:keys [heading omega angle] :as turtle}]`{.calibre4}\
> > `  (let [angle-step (min (q/abs omega) angle)`{.calibre4}\
> > `        angle (- angle angle-step)`{.calibre4}\
> > `        angle-step (if (neg? omega) (- angle-step) angle-step)`{.calibre4}\
> > `        heading (mod (+ heading angle-step) 360)]`{.calibre4}\
> > `    (assoc turtle :heading heading`{.calibre4}\
> > `                  :angle angle`{.calibre4}\
> > `                  :omega (if (zero? angle) 0.0 omega))))`{.calibre4}\
> > \
> > `(defn make-line [{:keys [pen-start position weight]}]`{.calibre4}\
> > `  {:line-start pen-start`{.calibre4}\
> > `   :line-end position`{.calibre4}\
> > `   :line-weight weight})`{.calibre4}\
> > \
> > `(defn update-turtle [turtle]`{.calibre4}\
> > `  {:post [(s/assert ::turtle %)]}`{.calibre4}\
> > `  (if (= :idle (:state turtle))`{.calibre4}\
> > `    turtle`{.calibre4}\
> > `    (let [{:keys [distance`{.calibre4}\
> > `                  state`{.calibre4}\
> > `                  angle`{.calibre4}\
> > `                  lines`{.calibre4}\
> > `                  position`{.calibre4}\
> > `                  pen`{.calibre4}\
> > `                  pen-start] :as turtle}`{.calibre4}\
> > `          (-> turtle`{.calibre4}\
> > `              (update-position)`{.calibre4}\
> > `              (update-heading))`{.calibre4}\
> > `          done? (and (zero? distance)`{.calibre4}\
> > `                     (zero? angle))`{.calibre4}\
> > `          state (if done? :idle state)`{.calibre4}\
> > `          lines (if (and done? (= pen :down))`{.calibre4}\
> > `                  (conj lines (make-line turtle))`{.calibre4}\
> > `                  lines)`{.calibre4}\
> > `          pen-start (if (and done? (= pen :down))`{.calibre4}\
> > `                      position`{.calibre4}\
> > `                      pen-start)]`{.calibre4}\
> > `      (assoc turtle`{.calibre4}\
> > `             :state state`{.calibre4}\
> > `             :lines lines`{.calibre4}\
> > `             :pen-start pen-start))))`{.calibre4}]{.calibre_3}]{.calibre_17}

Notice that [` update-turtle `{.calibre4}]{.calibre_17} has a [` :post `{.calibre4}]{.calibre_17} condition that checks the type of the turtle after it has been updated. It's nice to know that when you update a big structure you haven't messed up some little part of it.

If the [` turtle `{.calibre4}]{.calibre_17}'s [` :state `{.calibre4}]{.calibre_17} is [` :idle `{.calibre4}]{.calibre_17}, meaning that it is neither moving nor rotating, then we don't make any changes. Otherwise, we update the position and heading of the [` turtle `{.calibre4}]{.calibre_17} and then [destructure]{.italic} its internals. We are done when the distance and angle remaining in the current animated motion are zero. And if we are done, we set the [` :state `{.calibre4}]{.calibre_17} to [` :idle `{.calibre4}]{.calibre_17}.

If we are done and the pen is down, then we add the line in progress to the list of previous lines, and we update the [` pen-start `{.calibre4}]{.calibre_17} to the current position to prepare for the next line.

Updating the position and heading are simple functions that do the necessary trig calculations to place the turtle in the proper position and orientation. They both use the turtle's [` :velocity `{.calibre4}]{.calibre_17} to adjust how big a step they take at each update.

Now on to handling the commands:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_222.html#filepos983381)

> > [[`(defn handle-commands [channel turtle]`{.calibre4}\
> > `  (loop [turtle turtle]`{.calibre4}\
> > `    (let [command (if (= :idle (:state turtle))`{.calibre4}\
> > `                    (async/poll! channel)`{.calibre4}\
> > `                    nil)]`{.calibre4}\
> > `      (if (nil? command)`{.calibre4}\
> > `        turtle`{.calibre4}\
> > `        (recur (turtle/handle-command turtle command))))))`{.calibre4}]{.calibre_3}]{.calibre_17}

If the turtle is [` :idle `{.calibre4}]{.calibre_17}, then we are ready for a command. So we poll the [` channel `{.calibre4}]{.calibre_17}. If there is a command on the [` channel `{.calibre4}]{.calibre_17}, we process it by calling [` turtle/handle-command `{.calibre4}]{.calibre_17}, and then repeat until no commands are left on the channel.

Handling each command is pretty straightforward:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_223.html#filepos983527)

> > [[`(defn pen-down [{:keys [pen position pen-start] :as turtle}]`{.calibre4}\
> > `  (assoc turtle :pen :down`{.calibre4}\
> > `                :pen-start (if (= :up pen) position pen-start)))`{.calibre4}\
> > \
> > `(defn pen-up [{:keys [pen lines] :as turtle}]`{.calibre4}\
> > `  (if (= :up pen)`{.calibre4}\
> > `    turtle`{.calibre4}\
> > `    (let [new-line (make-line turtle)`{.calibre4}\
> > `          lines (conj lines new-line)]`{.calibre4}\
> > `      (assoc turtle :pen :up`{.calibre4}\
> > `                    :pen-start nil`{.calibre4}\
> > `                    :lines lines))))`{.calibre4}\
> > \
> > `(defn forward [turtle [distance]]`{.calibre4}\
> > `  (assoc turtle :velocity (:speed turtle)`{.calibre4}\
> > `                :distance distance`{.calibre4}\
> > `                :state :busy))`{.calibre4}\
> > \
> > `(defn back [turtle [distance]]`{.calibre4}\
> > `  (assoc turtle :velocity (- (:speed turtle))`{.calibre4}\
> > `                :distance distance`{.calibre4}\
> > `                :state :busy))`{.calibre4}\
> > \
> > `(defn right [turtle [angle]]`{.calibre4}\
> > `  (assoc turtle :omega (* 2 (:speed turtle))`{.calibre4}\
> > `                :angle angle`{.calibre4}\
> > `                :state :busy))`{.calibre4}\
> > \
> > `(defn left [turtle [angle]]`{.calibre4}\
> > `  (assoc turtle :omega (* -2 (:speed turtle))`{.calibre4}\
> > `                :angle angle`{.calibre4}\
> > `                :state :busy))`{.calibre4}\
> > \
> > `(defn hide [turtle]`{.calibre4}\
> > `  (assoc turtle :visible false))`{.calibre4}\
> > \
> > `(defn show [turtle]`{.calibre4}\
> > `  (assoc turtle :visible true))`{.calibre4}\
> > \
> > `(defn weight [turtle [weight]]`{.calibre4}\
> > `  (assoc turtle :weight weight))`{.calibre4}\
> > \
> > `(defn speed [turtle [speed]]`{.calibre4}\
> > `  (assoc turtle :speed speed))`{.calibre4}\
> > \
> > `(defn handle-command [turtle [cmd & args]]`{.calibre4}\
> > `  (condp = cmd`{.calibre4}\
> > `    :forward (forward turtle args)`{.calibre4}\
> > `    :back (back turtle args)`{.calibre4}\
> > `    :right (right turtle args)`{.calibre4}\
> > `    :left (left turtle args)`{.calibre4}\
> > `    :pen-down (pen-down turtle)`{.calibre4}\
> > `    :pen-up (pen-up turtle)`{.calibre4}\
> > `    :hide (hide turtle)`{.calibre4}\
> > `    :show (show turtle)`{.calibre4}\
> > `    :weight (weight turtle args)`{.calibre4}\
> > `    :speed (speed turtle args)`{.calibre4}\
> > `    :else turtle))`{.calibre4}]{.calibre_3}]{.calibre_17}
>
> []{#index_split_029.html#filepos531486}

We simply translate the command tokens into function calls. Not really rocket science. The command functions manage the state of the turtle. Take for instance, the [` forward `{.calibre4}]{.calibre_17} command. It sets the [` turtle `{.calibre4}]{.calibre_17}'s [` :state `{.calibre4}]{.calibre_17} to [` :busy `{.calibre4}]{.calibre_17}, sets the turtle's [` :velocity `{.calibre4}]{.calibre_17}, and sets the [` :distance `{.calibre4}]{.calibre_17} it must move before going [` :idle `{.calibre4}]{.calibre_17} again.

OK, we're almost done. Now all we need to do is look at the way the [` turtle-script `{.calibre4}]{.calibre_17} function sends commands to the [` channel `{.calibre4}]{.calibre_17}:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_225.html#filepos983819)

> > [[`(def channel (async/chan))`{.calibre4}\
> > `(defn forward [distance] (async/>!! channel [:forward distance]))`{.calibre4}\
> > `(defn back [distance] (async/>!! channel [:back distance]))`{.calibre4}\
> > `(defn right [angle] (async/>!! channel [:right angle]))`{.calibre4}\
> > `(defn left [angle] (async/>!! channel [:left angle]))`{.calibre4}\
> > `(defn pen-up [] (async/>!! channel [:pen-up]))`{.calibre4}\
> > `(defn pen-down [] (async/>!! channel [:pen-down]))`{.calibre4}\
> > `(defn hide [] (async/>!! channel [:hide]))`{.calibre4}\
> > `(defn show [] (async/>!! channel [:show]))`{.calibre4}\
> > `(defn weight [weight] (async/>!! channel [:weight weight]))`{.calibre4}\
> > `(defn speed [speed] (async/>!! channel [:speed speed]))`{.calibre4}]{.calibre_3}]{.calibre_17}
>
> []{#index_split_029.html#filepos533449}

The [` async/>!! `{.calibre4}]{.calibre_17} function sends its argument to the [` channel `{.calibre4}]{.calibre_17}. If the [` channel `{.calibre4}]{.calibre_17} is full, it waits. That really wasn't very surprising, was it?

And with that, we can put all the turtle graphics commands we like into the [` turtle-script `{.calibre4}]{.calibre_17} function and watch the turtle dance around the screen drawing our pretty pictures.

You can see this framework in action in the videos at [[[www.youtube.com/@Cleancoders]{.underline}]{.calibre_10}](http://www.youtube.com/@Cleancoders); specifically, [The Euler Project]{.italic}, episodes 2.3, 2.2, 5, and 9.

::: {#index_split_029.html#calibre_pb_29 .mbp_pagebreak}
:::

[]{#index_split_030.html}

[[[15]{.calibre_3}]{.bold}]{.calibre1}

[[[Concurrency]{.calibre_3}]{.bold}]{.calibre1}

![](images/00143.jpg){.calibre_64}

Concurrency in functional programs is substantially less complicated than it is in programs that support mutable state. The reason, as I said back in [[[Chapter 1]{.underline}]{.calibre_10}](#index_split_013.html#filepos61201), is that you can't have concurrent update problems if you don't do updates. I also said that this means you can't have race conditions.

These "facts" remove much of the complication of dealing with multiple threads. Threads simply cannot interfere with one another if they are composed of pure functions.

Or can they?

While comforting, those "facts" are not precisely true. The purpose of this chapter is to show how multithreaded "functional" programs can still have race conditions.

To examine this, let's set up some interacting finite state machines. One of my favorite examples is the making of a telephone call in the 1960s. The sequence of events looked roughly like [[[Figure 15.1]{.underline}]{.calibre_10}](#index_split_030.html#filepos535949).

![](images/00067.jpg){#filepos535949 .calibre_65}

[[Figure 15.1.]{.bold}]{.calibre3}[ A message sequence chart of a telephone call]{.calibre3}

This is a [message sequence chart]{.italic}. Time is on the vertical axis, and all messages are angled because they all take time to send.

You may be unfamiliar with the telephony nomenclature I used here. Indeed, if you were born after the year 2000, you may be unfamiliar with telephones in general. So, for the sake of history and nostalgia, let me walk you through the process.

Bob wants to place a call to Alice. Bob lifts the telephone receiver off its hook[]{#index_split_030.html#filepos536765}[[[[1]{.underline}]{.calibre_10}]{.calibre3}](#index_split_030.html#filepos537612) and holds it to his ear. The telephone company (telco) sends a dial tone[]{#index_split_030.html#filepos536930}[[[[2]{.underline}]{.calibre_10}]{.calibre3}](#index_split_030.html#filepos537909) to the receiver. Upon hearing that tone, Bob dials[]{#index_split_030.html#filepos537073}[[[[3]{.underline}]{.calibre_10}]{.calibre3}](#index_split_030.html#filepos538147) Alice's number. The telco then sends a ringing voltage[]{#index_split_030.html#filepos537222}[[[[4]{.underline}]{.calibre_10}]{.calibre3}](#index_split_030.html#filepos538409) to Alice's phone and a ringback[]{#index_split_030.html#filepos537348}[[[[5]{.underline}]{.calibre_10}]{.calibre3}](#index_split_030.html#filepos538549) tone to Bob's receiver. Alice hears the ringing of her phone and lifts the receiver off the hook. The telco connects Bob to Alice, and Alice says "Hello" to Bob.

[[[1]{.underline}]{.calibre_10}](#index_split_030.html#filepos536765). Telephones in the early 20th century had a hook that the receiver hung on. By the 1960s, the hook had been replaced by a cradle that the receiver sat in; but it was still called the hook.

[[[2]{.underline}]{.calibre_10}](#index_split_030.html#filepos536930). This was a very recognizable sound that meant that the telephone system was ready for you to dial the number you wanted to call.

[[[3]{.underline}]{.calibre_10}](#index_split_030.html#filepos537073). The verb [dial]{.italic} means to enter the telephone number. In the early 1960s, this was accomplished by using a rotary dial on the face of the telephone.

[[[4]{.underline}]{.calibre_10}](#index_split_030.html#filepos537222). 90 volts in the United States.

[[[5]{.underline}]{.calibre_10}](#index_split_030.html#filepos537348). Another very distinct sound that was meant to entertain the caller while waiting for the called phone to be answered.

There are three finite state machines running in this scenario: Bob, telco, and Alice. Bob and Alice run separate instances of the User state machine[]{#index_split_030.html#filepos538966}[[[[6]{.underline}]{.calibre_10}]{.calibre3}](#index_split_030.html#filepos539393) shown in [[[Figure 15.2]{.underline}]{.calibre_10}](#index_split_030.html#filepos539189).

![](images/00013.jpg){#filepos539189 .calibre_66}

[[Figure 15.2.]{.bold}]{.calibre3}[ The User state machine]{.calibre3}

[[[6]{.underline}]{.calibre_10}](#index_split_030.html#filepos538966). These state machines are abbreviated to keep them simple. In reality, all the states would have transitions back to Idle.

The Telco state machine is shown in [[[Figure 15.3]{.underline}]{.calibre_10}](#index_split_030.html#filepos539822).

![](images/00328.jpg){#filepos539822 .calibre_67}

[[Figure 15.3.]{.bold}]{.calibre3}[ The Telco state machine]{.calibre3}

In these diagrams, the [` -> `{.calibre4}]{.calibre_17} symbol means to send the corresponding event to the other state machine.

So when Bob decides to make a call (the call event from the Idle state) the User state machine sends the off-hook event to the Telco. When the Telco is in the Waiting for Dial state and receives the Dial event from the User, it sends the Ring and Ringback events to the appropriate User state machines.

If you study these diagrams carefully, you should be able to see how the state machines and messages interact to allow Bob to call Alice.

We can write these state machines in Clojure quite simply:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_226.html#filepos983950)

> > [[`(def user-sm`{.calibre4}\
> > `  {:idle {:call [:calling caller-off-hook]`{.calibre4}\
> > `          :ring [:waiting-for-connection callee-off-hook]`{.calibre4}\
> > `          :disconnect [:idle nil]}`{.calibre4}\
> > `   :calling {:dialtone [:dialing dial]}`{.calibre4}\
> > `   :dialing {:ringback [:waiting-for-connection nil]}`{.calibre4}\
> > `   :waiting-for-connection {:connected [:talking talk]}`{.calibre4}\
> > `   :talking {:disconnect [:idle nil]}})`{.calibre4}\
> > \
> > `(def telco-sm`{.calibre4}\
> > `  {:idle {:caller-off-hook [:waiting-for-dial dialtone]`{.calibre4}\
> > `          :hangup [:idle nil]}`{.calibre4}\
> > `   :waiting-for-dial {:dial [:waiting-for-answer ring]}`{.calibre4}\
> > `   :waiting-for-answer {:callee-off-hook`{.calibre4}\
> > `                        [:waiting-for-hangup connect]}`{.calibre4}\
> > `   :waiting-for-hangup {:hangup [:idle disconnect]}})`{.calibre4}]{.calibre_3}]{.calibre_17}

Each state machine is simply a hash map of states, each of which contains a hash map of events that specify the new state and the action to be performed.

So when the [` user-sm `{.calibre4}]{.calibre_17} is in the [` :idle `{.calibre4}]{.calibre_17} state and it gets a [` :call `{.calibre4}]{.calibre_17} event, it transitions to the [` :calling `{.calibre4}]{.calibre_17} state and calls the [` caller-off-hook `{.calibre4}]{.calibre_17} function.

These state machines can be executed by the following [` transition `{.calibre4}]{.calibre_17} function:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_227.html#filepos984096)

> > [[`(defn transition [machine-agent event event-data]`{.calibre4}\
> > `  (swap! log conj (str (:name machine-agent) "<-" event))`{.calibre4}\
> > `  (let [state (:state machine-agent)`{.calibre4}\
> > `        sm (:machine machine-agent)`{.calibre4}\
> > `        result (get-in`{.calibre4}]{.calibre_3}]{.calibre_17}[[[[7]{.underline}]{.calibre_10}]{.calibre3}](#index_split_030.html#filepos543951)[[` sm [state event])]`{.calibre4}\
> > `    (if (nil? result)`{.calibre4}\
> > `      (do`{.calibre4}\
> > `        (swap! log conj "TILT!")`{.calibre4}\
> > `        machine-agent)`{.calibre4}\
> > `      (do`{.calibre4}\
> > \
> > `        (when (second result)`{.calibre4}\
> > `          ((second result) machine-agent event-data))`{.calibre4}\
> > `        (assoc machine-agent :state (first result))))))`{.calibre4}]{.calibre_3}]{.calibre_17}
>
> []{#index_split_030.html#filepos543931}

[[[7]{.underline}]{.calibre_10}](#index_split_030.html#filepos543931). The [` get-in `{.calibre4}]{.calibre_17} function returns an element from a nested map. [` (get-in {:a {:b 2}} [:a :b]) `{.calibre4}]{.calibre_17} returns [` 2 `{.calibre4}]{.calibre_17}.

The [` log `{.calibre4}]{.calibre_17} variable is an [` atom `{.calibre4}]{.calibre_17} that is simply used to accumulate a set of logging statements so that we can watch the operation of the state machines. Notice that this function takes the [` machine-agent `{.calibre4}]{.calibre_17} and returns it with the new state in place. This means we can use it with Clojure's [` agent `{.calibre4}]{.calibre_17} STM facility.

An [` agent `{.calibre4}]{.calibre_17} is initialized with a data structure and then serializes all updates to that data structure, thereby eliminating all concurrent update issues. Here are the functions that create the two different [` agent `{.calibre4}]{.calibre_17}s:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_228.html#filepos984242)

> > [[`(defn make-user-agent [name]`{.calibre4}\
> > `  (agent {:state :idle :name name :machine user-sm}))`{.calibre4}\
> > \
> > `(defn make-telco-agent [name]`{.calibre4}\
> > `  (agent {:state :idle :name name :machine telco-sm}))`{.calibre4}]{.calibre_3}]{.calibre_17}

We send events to our agents by using the [` agent `{.calibre4}]{.calibre_17}'s [` send `{.calibre4}]{.calibre_17} function:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_229.html#filepos984388)

> > [[`(send caller transition :call [telco caller callee])`{.calibre4}]{.calibre_3}]{.calibre_17}

In this example, we are [` send `{.calibre4}]{.calibre_17}ing the [` transition `{.calibre4}]{.calibre_17} function to the [` caller `{.calibre4}]{.calibre_17} agent. The [` send `{.calibre4}]{.calibre_17} function returns immediately and queues up the [` transition `{.calibre4}]{.calibre_17} function to be executed in the [` agent `{.calibre4}]{.calibre_17}'s thread. The arguments to the [` transition `{.calibre4}]{.calibre_17} function are the event ([` :call `{.calibre4}]{.calibre_17}) and the data that should be passed to the action function. In this case, the data is a list of the three [` agent `{.calibre4}]{.calibre_17}s that represent the finite state machines in the system.

The action functions are as follows:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_230.html#filepos984533)

> > [[`(defn caller-off-hook`{.calibre4}\
> > `  [sm-agent [telco caller callee :as call-data]]`{.calibre4}\
> > `  (swap! log conj (str  (:name @caller) " goes off hook."))`{.calibre4}\
> > `  (send telco transition :caller-off-hook call-data))`{.calibre4}\
> > \
> > `(defn dial [sm-agent [telco caller callee :as call-data]]`{.calibre4}\
> > `  (swap! log conj (str (:name @caller) " dials"))`{.calibre4}\
> > `  (send telco transition :dial call-data))`{.calibre4}\
> > \
> > `(defn callee-off-hook`{.calibre4}\
> > `  [sm-agent [telco caller callee :as call-data]]`{.calibre4}\
> > `  (swap! log conj (str (:name @callee) " goes off hook"))`{.calibre4}\
> > `  (send telco transition :callee-off-hook call-data))`{.calibre4}\
> > \
> > `(defn talk [sm-agent [telco caller callee :as call-data]]`{.calibre4}\
> > `  (swap! log conj (str (:name sm-agent) " talks."))`{.calibre4}\
> > `  (Thread/sleep 10)`{.calibre4}\
> > `  (swap! log conj (str (:name sm-agent) " hangs up."))`{.calibre4}\
> > `  (send telco transition :hangup call-data))`{.calibre4}\
> > \
> > `(defn dialtone [sm-agent [telco caller callee :as call-data]]`{.calibre4}\
> > `  (swap! log conj (str "dialtone to " (:name @caller)))`{.calibre4}\
> > `  (send caller transition :dialtone call-data))`{.calibre4}\
> > \
> > `(defn ring [sm-agent [telco caller callee :as call-data]]`{.calibre4}\
> > `  (swap! log conj (str "telco rings " (:name @callee)))`{.calibre4}\
> > `  (send callee transition :ring call-data)`{.calibre4}\
> > `  (send caller transition :ringback call-data))`{.calibre4}\
> > \
> > `(defn connect [sm-agent [telco caller callee :as call-data]]`{.calibre4}\
> > `  (swap! log conj "telco connects")`{.calibre4}\
> > `  (send caller transition :connected call-data)`{.calibre4}\
> > `  (send callee transition :connected call-data))`{.calibre4}\
> > \
> > `(defn disconnect [sm-agent [telco caller callee :as call-data]]`{.calibre4}\
> > `  (swap! log conj "disconnect")`{.calibre4}\
> > `  (send callee transition :disconnect call-data)`{.calibre4}\
> > `  (send caller transition :disconnect call-data))`{.calibre4}]{.calibre_3}]{.calibre_17}

The second argument in each of the action functions is [destructured]{.italic}.[]{#index_split_030.html#filepos549642}[[[[8]{.underline}]{.calibre_10}]{.calibre3}](#index_split_030.html#filepos550196) So, for example, the [` call-data `{.calibre4}]{.calibre_17} sent to [` caller-off-hook `{.calibre4}]{.calibre_17} is a list, the first element of which will be placed in [` telco `{.calibre4}]{.calibre_17}, the second in [` caller `{.calibre4}]{.calibre_17}, the third in [` callee `{.calibre4}]{.calibre_17}, and the whole list in [` call-data `{.calibre4}]{.calibre_17}.

[[[8]{.underline}]{.calibre_10}](#index_split_030.html#filepos549642). In short, destructuring is a convenient way of breaking a complex data element into named components. See the Clojure documentation for more details.

Given this implementation, we should be able to make a call between Bob and Alice by executing the following code. I have written it in the form of a test:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_231.html#filepos984679)

> > [[`(it "should make and receive call"`{.calibre4}\
> > `  (let [caller (make-user "Bob")`{.calibre4}\
> > `        callee (make-user "Alice")`{.calibre4}\
> > `        telco (make-telco "telco")]`{.calibre4}\
> > `    (reset! log [])`{.calibre4}\
> > `    (send caller transition :call [telco caller callee])`{.calibre4}\
> > `    (Thread/sleep 100)`{.calibre4}\
> > `    (prn @log)`{.calibre4}\
> > `    (should= :idle (:state @caller))`{.calibre4}\
> > `    (should= :idle (:state @callee))`{.calibre4}\
> > `    (should= :idle (:state @telco))))`{.calibre4}]{.calibre_3}]{.calibre_17}

This test passes, which means that all the state machines returned to the idle state by the time 100ms had passed. The log output looks like this:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_232.html#filepos984825)

> > [[`"Bob<-:call" "Bob goes off hook"`{.calibre4}\
> > `"telco<-:caller-off-hook" "dialtone to Bob"`{.calibre4}\
> > `"Bob<-:dialtone" "Bob dials"`{.calibre4}\
> > `"telco<-:dial" "telco rings Alice"`{.calibre4}\
> > `"Alice<-:ring" "Alice goes off hook"`{.calibre4}\
> > `"Bob<-:ringback"`{.calibre4}\
> > `"telco<-:callee-off-hook" "telco connects"`{.calibre4}\
> > `"Bob<-:connected" "Bob talks"`{.calibre4}\
> > `"Alice<-:connected" "Alice talks"`{.calibre4}\
> > `"Bob hangs up"`{.calibre4}\
> > `"Alice hangs up"`{.calibre4}\
> > `"telco<-:hangup" "disconnect"`{.calibre4}\
> > `"Alice<-:disconnect"`{.calibre4}\
> > `"Bob<-:disconnect"`{.calibre4}\
> > `"telco<-:hangup"`{.calibre4}]{.calibre_3}]{.calibre_17}
>
> []{#index_split_030.html#filepos552559}

You can see how the threads interleaved with one another, while all three finite state machines worked together to drive the call to a successful completion.

The three agents have mutable state; but there can be no concurrent update problems because the agents serialize their operations. So no race conditions, right?

Not so fast there, Newt. Let's investigate another scenario.

What I'm about to show you in [[[Figure 15.4]{.underline}]{.calibre_10}](#index_split_030.html#filepos553708), is a race condition that existed in the telephone system in the '60s.[]{#index_split_030.html#filepos553315}[[[[9]{.underline}]{.calibre_10}]{.calibre3}](#index_split_030.html#filepos553503) Once again, we begin with Bob calling Alice. But this time Alice is just about to call Bob.

[[[9]{.underline}]{.calibre_10}](#index_split_030.html#filepos553315). It probably still exists today if you use landlines.

![](images/00151.jpg){#filepos553708 .calibre_68}

[[Figure 15.4.]{.bold}]{.calibre3}[ The race condition in the telephone system]{.calibre3}

Do you see what went wrong? Those crossed lines are the problem. That's a race condition. The telco tried to ring Alice's phone; but before it could make the sound, Alice picked up the receiver in order to call Bob. From the point of view of the telco, everything is fine. It rang the phone and Alice picked up. So the telco happily connects Bob and Alice. But Alice is sitting there waiting for a dial tone; and Bob is confused because nobody has said hello and the ringback tone has stopped.

The most likely outcome is that both parties hang up without talking to each other. Alternatively, Alice might say something and Bob might respond, and they'd get into the comic routine of who called who.

Can we make our state machines emulate this fault? Here's the setup, once again posed as a test:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_233.html#filepos984971)

> > [[`(it "should race"`{.calibre4}\
> > `  (let [caller (make-user "Bob")`{.calibre4}\
> > `        callee (make-user "Alice")`{.calibre4}\
> > `        telco1 (make-telco "telco1")`{.calibre4}\
> > `        telco2 (make-telco "telco2")]`{.calibre4}\
> > `    (reset! log [])`{.calibre4}\
> > `    (send caller transition :call [telco1 caller callee])`{.calibre4}\
> > `    (send callee transition :call [telco2 callee caller])`{.calibre4}\
> > `    (Thread/sleep 100)`{.calibre4}\
> > `    (prn @log)`{.calibre4}\
> > `    (should= :idle (:state @caller))`{.calibre4}\
> > `    (should= :idle (:state @callee))`{.calibre4}\
> > `    (should= :idle (:state @telco1))`{.calibre4}\
> > `    (should= :idle (:state @telco2))))`{.calibre4}]{.calibre_3}]{.calibre_17}

Notice that we now have four state machines: one for Bob, one for Alice, and one telco for each of the two calls. The test fails. After 100ms, the state machines have not returned to the Idle state.

So, what does the log tell us?

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_234.html#filepos985117)

> > [[`"Bob<-:call" "Bob goes off hook"`{.calibre4}\
> > `"telco1<-:caller-off-hook"`{.calibre4}\
> > `"Alice<-:call" "Alice goes off hook"`{.calibre4}\
> > `"telco2<-:caller-off-hook"`{.calibre4}\
> > `"dialtone to Bob"`{.calibre4}\
> > `"Bob<-:dialtone" "Bob dials"`{.calibre4}\
> > `"telco1<-:dial" "telco rings Alice"`{.calibre4}\
> > `"Bob<-:ringback"`{.calibre4}\
> > `"Alice<-:ring" "TILT!" …`{.calibre4}]{.calibre_3}]{.calibre_17}
>
> []{#index_split_030.html#filepos556826}

This took me several tries, because the window for that particular race condition is pretty narrow. But there it is. See that [` TILT! `{.calibre4}]{.calibre_17}? That's what our [` transition `{.calibre4}]{.calibre_17} function puts in the log if it is ever asked to make an invalid transition. Alice is still in the [` :calling `{.calibre4}]{.calibre_17} state waiting for the [` :dialtone `{.calibre4}]{.calibre_17} event, and has no way to deal with the [` :ring `{.calibre4}]{.calibre_17} event.

The bottom line is that race conditions are still possible even though concurrent updates are not. That's because it is always possible to construct interacting state machines that get out of sync with one another.

[[[Conclusion]{.calibre_3}]{.bold}]{.calibre1}

Somewhere around the turn of the century, Moore's law died. Clock rates hit a maximum of about 3GHz and then just stopped increasing. To drive more throughput, hardware engineers started putting more processors on their chips. We went through the dual-core stage and the quad-core stage---and we thought we were going to see a doubling in cores every other year or so. We started to fret about the possibility of dealing with machines that had 32, or 64, or 128 cores.

This is about the time functional languages started to gain in popularity. The thought was that since functional programs don't mutate data, multicore operations would be made much simpler. If you are working with pure functions, it is theoretically easy to spread those functions out over a plethora of cores.

But Moore's law wasn't done dying. It died for clock speed a few years before it died for component density. So, for the past decade or more, our []{#index_split_030.html#filepos558905}processors have been quad core (don't talk to me about hyperthreading); and that is not likely to change. This has decreased the fear of the 128-core processor and lessened the urgency behind functional programming.

And that's probably a good thing because, as this chapter has shown, the reasoning was somewhat faulty to begin with. Race conditions might be more common in threads that have mutable variables, but in any system where there are concurrent finite state machines, the possibility exists that race conditions might drive them out of sync with one another.

::: {#index_split_030.html#calibre_pb_30 .mbp_pagebreak}
:::

[]{#index_split_031.html}

[[V]{.calibre_3}]{.calibre2}

[[Design Patterns]{.calibre_3}]{.calibre2}

The idea of design patterns[]{#index_split_031.html#filepos559826}[[[[1]{.underline}]{.calibre_10}]{.calibre3}](#index_split_031.html#filepos560238) was one of the most profound in the software industry. It ranks up there with structured programming, object-oriented programming, and functional programming. It told us that applications consist, in part, of repeatable and reusable elements. Those elements solved problems common to many, if not all, applications.

[[[1.]{.underline}]{.calibre_10}](#index_split_031.html#filepos559826) The definitive work on this topic was Erich Gamma, Richard Helm, Ralph Johnson, and John Vlissides, [Design Patterns: Elements of Reusable Object-Oriented Software]{.italic} (Addison-Wesley, 1994).

Of course, like all good ideas in software, design patterns have been misunderstood, overused, abused, and even discarded as archaic or specific to only very narrow contexts. This is a shame, because design patterns are eminently useful.

::: {#index_split_031.html#calibre_pb_31 .mbp_pagebreak}
:::

[]{#index_split_032.html}

[[[16]{.calibre_3}]{.bold}]{.calibre1}

[[[Design Patterns Review]{.calibre_3}]{.bold}]{.calibre1}

![](images/00026.jpg){.calibre_69}

A [design pattern]{.italic} is a named solution to a common problem in a particular context. Yes, I know, another word salad. So let me tell you a story.

Long ago, in a decade far, far away, I was a prolific writer on a social network called comp.object.[]{#index_split_032.html#filepos561529}[[[[2]{.underline}]{.calibre_10}]{.calibre3}](#index_split_032.html#filepos561672) In this group, we debated issues of OO design.

[[[2]{.underline}]{.calibre_10}](#index_split_032.html#filepos561529). A newsgroup within the vast array of newsgroups transmitted by Network News Transport Protocol (NNTP) over Unix-to-Unix copy (UUCP) and the Internet.

One day someone posed a simple problem and suggested that we all solve it in our own way and then debate the result. The problem was:

[Given a switch and a light, make the switch turn the light on.]{.italic}

The debates raged for months.

The simplest solution was, of course, [[[Figure 16.1]{.underline}]{.calibre_10}](#index_split_032.html#filepos562500).

![](images/00102.jpg){#filepos562500 .calibre_70}

[[Figure 16.1.]{.bold}]{.calibre3}[ The simplest solution for the switch and the light]{.calibre3}

The [` Switch `{.calibre4}]{.calibre_17} class[]{#index_split_032.html#filepos562832}[[[[3]{.underline}]{.calibre_10}]{.calibre3}](#index_split_032.html#filepos563060) calls the [` TurnOn `{.calibre4}]{.calibre_17} method of the [` Light `{.calibre4}]{.calibre_17} class.

[[[3]{.underline}]{.calibre_10}](#index_split_032.html#filepos562832). Remember, this was an OO forum. Don't get hung up on the word [class]{.italic}.

The objection to this was that the [` Switch `{.calibre4}]{.calibre_17} class could be used to turn on other things like [` Fan `{.calibre4}]{.calibre_17}s or [` Television `{.calibre4}]{.calibre_17}s. Therefore, the [` Switch `{.calibre4}]{.calibre_17} class should not know about the [` Light `{.calibre4}]{.calibre_17} class. An abstraction should be imposed between the two, as shown in [[[Figure 16.2]{.underline}]{.calibre_10}](#index_split_032.html#filepos563870).

![](images/00244.jpg){#filepos563870 .calibre_71}

[[Figure 16.2.]{.bold}]{.calibre3}[ The Abstract Server]{.calibre3}

Now the [` Switch `{.calibre4}]{.calibre_17} class uses an interface named [` Switchable `{.calibre4}]{.calibre_17}. The [` Light `{.calibre4}]{.calibre_17} class implements [` Switchable `{.calibre4}]{.calibre_17}.

This solves the problem. Now we could have any number of devices controlled by the [` Switch `{.calibre4}]{.calibre_17}. This solution is one of the simplest expressions []{#index_split_032.html#filepos564613}of the DIP, the OCP, and the LSP. It also has a name. It's called [Abstract Server]{.italic}.[]{#index_split_032.html#filepos564711}[[[[4]{.underline}]{.calibre_10}]{.calibre3}](#index_split_032.html#filepos564807)

[[[4]{.underline}]{.calibre_10}](#index_split_032.html#filepos564711). Robert C. Martin, [Agile Software Development: Principles, Patterns, and Practices]{.italic} (Pearson, 2002), 318.

If we were on a team discussing how to protect our [` Switch `{.calibre4}]{.calibre_17} class from being explicitly coupled to our [` Light `{.calibre4}]{.calibre_17} class, someone on the team could pipe up and say, "We could use an Abstract Server." If all the team members knew that name and what it implied, they could quickly decide whether that solution was appropriate or not.

That's a design pattern, a named solution to a problem in a particular context. The value of design patterns is that the names and the solutions are canonical, and therefore, people who are familiar with that canon can understand one another simply by using the name. You say "[[[Abstract Server]{.underline}]{.calibre_10}](#index_split_032.html#filepos570391)" and I immediately understand that you mean "impose an interface between the client and the server."

But what about the context part of the design pattern? Well, let's go back to our team. Someone has just suggested using the Abstract Server pattern. Another team member says, "No, you don't understand, we don't own the [` Light `{.calibre4}]{.calibre_17} class; it's part of a third-party library, so we can't alter it to implement an interface."

So, the context of the problem is that we want to decouple [` Switch `{.calibre4}]{.calibre_17} from [` Light `{.calibre4}]{.calibre_17}, but we can't modify [` Light `{.calibre4}]{.calibre_17}. So someone else on the team says, "Well, we could use an [Adapter]{.italic}."

If you were on the team and didn't know what the Adapter pattern was, you wouldn't understand their suggestion. But if you were aware of the design patterns canon, you could swiftly assess the suggestion. Again, the benefit of design patterns is knowing the names and the canonical forms so that you can quickly apply them.

The Adapter pattern looks like [[[Figure 16.3]{.underline}]{.calibre_10}](#index_split_032.html#filepos567348).

![](images/00194.jpg){#filepos567348 .calibre_72}

[[Figure 16.3.]{.bold}]{.calibre3}[ The object form of the Adapter pattern]{.calibre3}

The [` LightAdapter `{.calibre4}]{.calibre_17} implements the [` Switchable `{.calibre4}]{.calibre_17} interface and forwards the [` TurnOn `{.calibre4}]{.calibre_17} call to the [` Light `{.calibre4}]{.calibre_17}. Even before this is drawn on the whiteboard, everyone on the team can see it in their minds because they know the design patterns canon. So they all nod in agreement with the idea.

Just as they are about to move on to the next issue, someone on the team says, "Wait, which form of the Adapter should we use?"

It turns out that the canonical name for a design pattern does not necessarily describe a single solution. Some of the patterns have multiple forms. The Adapter is one such pattern. It could look like [[[Figure 16.3]{.underline}]{.calibre_10}](#index_split_032.html#filepos567348), or it could look like [[[Figure 16.4]{.underline}]{.calibre_10}](#index_split_032.html#filepos568703).

![](images/00241.jpg){#filepos568703 .calibre_72}

[[Figure 16.4.]{.bold}]{.calibre3}[ The class form of the Adapter pattern]{.calibre3}

The former is called the [object]{.italic} form of the Adapter because the [` LightAdapter `{.calibre4}]{.calibre_17} is its own object. The latter is the [class]{.italic} form of the Adapter because the [` LightAdapter `{.calibre4}]{.calibre_17} is a subclass of [` Light `{.calibre4}]{.calibre_17}.

The team members debate the two forms for a moment and come to the decision that the class form of the Adapter is sufficient for the moment and will relieve them of the complication of constructing a separate [` LightAdapter `{.calibre4}]{.calibre_17} object.

[[[Patterns in Functional Programming]{.calibre_3}]{.bold}]{.calibre1}

Among the strange rumors we have heard over the years is that design patterns are hacks to get around the problems created by OO languages and that in functional languages they are not necessary.

As you'll see in the pages that follow, there are indeed aspects of certain design patterns that appear to be workarounds for certain inadequacies in OO languages; but this is hardly applicable to all design patterns. Moreover, even those particular design patterns have a more general form in which they are applicable in functional languages.

[[[Abstract Server]{.calibre_3}]{.bold}]{.calibre1}

![](images/00178.jpg){.calibre_73}

So, what does the Abstract Server look like in a functional language?

Consider the [` Switch/Light `{.calibre4}]{.calibre_17} problem again. Here's how we might express it in Clojure:

> > [[`(defn turn-on-light []`{.calibre4}\
> > `  ;turn on the bloody light!`{.calibre4}\
> > `  )`{.calibre4}\
> > \
> > `(defn engage-switch []`{.calibre4}\
> > `  ;Some other stuff. . .`{.calibre4}\
> > `  (turn-on-light))`{.calibre4}]{.calibre_3}]{.calibre_17}

OK, that's not rocket science. However, the original problem is immediately evident. Our [` engage-switch `{.calibre4}]{.calibre_17} function has a direct dependency on [` turn-on-light `{.calibre4}]{.calibre_17}, which means we can't use it to turn on a fan or a television or anything else. So, what should we do?

We can use the Abstract Server pattern, of course. All we need to do is insert an abstract interface between the [` engage-switch `{.calibre4}]{.calibre_17} function and the [` turn-on-light `{.calibre4}]{.calibre_17} function. We could do that by simply passing a function argument. Let's call this the [function]{.italic} form of the Abstract Server:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_235.html#filepos985248)

> > [[`(defn engage-switch [turn-on-function]`{.calibre4}\
> > `  ;Some other stuff. . .`{.calibre4}\
> > `  (turn-on-function))`{.calibre4}]{.calibre_3}]{.calibre_17}

That works in the simplest case. But let's make the problem just a bit more interesting. Let's say that our [` engage-switch `{.calibre4}]{.calibre_17} function must turn the light both on and off at various times. Perhaps it's part of some home security system with special timers for the lights. This changes the original problem to look like this:

> > [[`(defn turn-on-light []`{.calibre4}\
> > `  ;turn on the bloody light!`{.calibre4}\
> > `  )`{.calibre4}\
> > \
> > `(defn turn-off-light []`{.calibre4}\
> > `  ;Criminy! just turn it off!`{.calibre4}\
> > `  )`{.calibre4}\
> > \
> > `(defn engage-switch []`{.calibre4}\
> > `  ;Some other stuff...`{.calibre4}\
> > `  (turn-on-light)`{.calibre4}\
> > `  ;Some more other stuff...`{.calibre4}\
> > `  (turn-off-light))`{.calibre4}]{.calibre_3}]{.calibre_17}
>
> []{#index_split_032.html#filepos573383}

Now the [` engage-switch `{.calibre4}]{.calibre_17} function is twice as coupled to the light. We could use the same function form of the Abstract Server, but it's a bit ugly passing in two arguments. So let's pass in a single vtable argument. We'll call this the [vtable]{.italic} form of the Abstract Server:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_236.html#filepos985393)

> > [[`(defn make-switchable-light []`{.calibre4}\
> > `  {:on turn-on-light`{.calibre4}\
> > `   :off turn-off-light})`{.calibre4}\
> > \
> > `(defn engage-switch [switchable]`{.calibre4}\
> > `  ;Some other stuff...`{.calibre4}\
> > `  ((:on switchable))`{.calibre4}\
> > `  ;Some more other stuff...`{.calibre4}\
> > `  ((:off switchable)))`{.calibre4}]{.calibre_3}]{.calibre_17}

Yeah, that's actually pretty nice. And since Clojure is a dynamically typed language, we don't have the problem that an inheritance or implements relationship would cause.

Of course, we could have solved this with the [multi-method]{.italic} form of the Abstract Server pattern:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_237.html#filepos985539)

> > [[`(defmulti turn-on :type)`{.calibre4}\
> > `(defmulti turn-off :type)`{.calibre4}\
> > \
> > `(defmethod turn-on :light [switchable]`{.calibre4}\
> > `  (turn-on-light))`{.calibre4}\
> > \
> > `(defmethod turn-off :light [switchable]`{.calibre4}\
> > `  (turn-off-light))`{.calibre4}\
> > \
> > `(defn engage-switch [switchable]`{.calibre4}\
> > `  ;Some other stuff...`{.calibre4}\
> > `  (turn-on switchable)`{.calibre4}\
> > `  ;Some more other stuff...`{.calibre4}\
> > `  (turn-off switchable))`{.calibre4}]{.calibre_3}]{.calibre_17}
>
> []{#index_split_032.html#filepos575468}

I tested this using the following test:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_238.html#filepos985685)

> > [[`(describe "switch/light"`{.calibre4}\
> > `  (with-stubs)`{.calibre4}\
> > `  (it "turns light on and off"`{.calibre4}\
> > `    (with-redefs [turn-on-light (stub :turn-on-light)`{.calibre4}\
> > `                  turn-off-light (stub :turn-off-light)]`{.calibre4}\
> > `      (engage-switch `{.calibre4}]{.calibre_3}]{.calibre_17}[[`{:type :light}`{.calibre4}]{.calibre_3}]{.bold}[[`)`{.calibre4}\
> > `      (should-have-invoked :turn-on-light)`{.calibre4}\
> > `      (should-have-invoked :turn-off-light))))`{.calibre4}]{.calibre_3}]{.calibre_17}

The two stubs mock out the target functions. We invoke the [` engage-switch `{.calibre4}]{.calibre_17} function with the [` {:type :light} `{.calibre4}]{.calibre_17} argument. Then we test that the two target functions were, in fact, called.

I'll leave the [protocol/record]{.italic} form of the Abstract Server pattern as an exercise. At this point, it should be clear that the pattern is both applicable and useful in a functional language.

[[[Adapter]{.calibre_3}]{.bold}]{.calibre1}

![](images/00229.jpg){.calibre_74}

The Adapter pattern is used whenever you have a client who wants to use a server, but the interface that the client expects and the interface that the server expresses are incompatible.

As an example, let's suppose that we have the [` engage-switch `{.calibre4}]{.calibre_17} function from the preceding discussion, but we want to pass it a third-party [` :variable-light `{.calibre4}]{.calibre_17}. The [` turn-on-light `{.calibre4}]{.calibre_17} function of the [` :variable-light `{.calibre4}]{.calibre_17} accepts an argument for the intensity of the light: [` 0 `{.calibre4}]{.calibre_17} for off and [` 100 `{.calibre4}]{.calibre_17} for full on.

The interface of the [` :variable-light `{.calibre4}]{.calibre_17} does not match the expectation of the [` engage-switch `{.calibre4}]{.calibre_17} function. So we need an Adapter.

Perhaps the simplest form of the Adapter might look like this:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_239.html#filepos985831)

> > [[`(defn turn-on-light [intensity]`{.calibre4}\
> > `  ;Turn it on with intensity.`{.calibre4}\
> > `  )`{.calibre4}\
> > \
> > `(defmulti turn-on :type)`{.calibre4}\
> > `(defmulti turn-off :type)`{.calibre4}\
> > \
> > `(defmethod turn-on :variable-light [switchable]`{.calibre4}\
> > `  (turn-on-light 100))`{.calibre4}\
> > \
> > `(defmethod turn-off :variable-light [switchable]`{.calibre4}\
> > `  (turn-on-light 0))`{.calibre4}\
> > \
> > `(defn engage-switch [switchable]`{.calibre4}\
> > `  ;Some other stuff...`{.calibre4}\
> > `  (turn-on switchable)`{.calibre4}\
> > `  ;Some more other stuff...`{.calibre4}\
> > `  (turn-off switchable))`{.calibre4}]{.calibre_3}]{.calibre_17}

I tested this with the following test:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_240.html#filepos985977)

> > [[`(describe "Adapter"`{.calibre4}\
> > `  (with-stubs)`{.calibre4}\
> > `  (it "turns light on and off"`{.calibre4}\
> > `    (with-redefs [turn-on-light (stub :turn-on-light)]`{.calibre4}\
> > `      (engage-switch {:type :variable-light})`{.calibre4}\
> > `      (should-have-invoked :turn-on-light {:times 1 :with [100]})`{.calibre4}\
> > `      (should-have-invoked :turn-on-light {:times 1 :with [0]}))))`{.calibre4}]{.calibre_3}]{.calibre_17}

If I were to draw this structure in the UML, I'd likely draw something like [[[Figure 16.5]{.underline}]{.calibre_10}](#index_split_032.html#filepos580282).

![](images/00288.jpg){#filepos580282 .calibre_75}

[[Figure 16.5.]{.bold}]{.calibre3}[ The object form of the Adapter pattern]{.calibre3}

The [` defmulti `{.calibre4}]{.calibre_17} functions correspond to the [` Switchable `{.calibre4}]{.calibre_17} interface. The [` {:type :variable-light} `{.calibre4}]{.calibre_17} object, coupled to the two [` defmethod `{.calibre4}]{.calibre_17} functions, corresponds to the [` VariableLightAdapter `{.calibre4}]{.calibre_17}. The [` EngageSwitch `{.calibre4}]{.calibre_17} and [` VariableLight `{.calibre4}]{.calibre_17} "classes" correspond to the two functions that we are trying to adapt.

Perhaps you don't find this convincing. After all, it's just a simple little program with a couple of [` defmulti `{.calibre4}]{.calibre_17} functions. There's no obvious OO structure like that shown in the UML. So let's impose that structure by splitting up the source files.

We begin with the [` switchable `{.calibre4}]{.calibre_17} interface. In the [` ns `{.calibre4}]{.calibre_17} statement, I used the convention that [` turn-on-light `{.calibre4}]{.calibre_17} was the overall namespace for the project that contains the [` switchable `{.calibre4}]{.calibre_17} namespace:

> > [[`(ns turn-on-light.switchable)`{.calibre4}\
> > \
> > `(defmulti turn-on :type)`{.calibre4}\
> > `(defmulti turn-off :type)`{.calibre4}]{.calibre_3}]{.calibre_17}

This is a polymorphic interface. Notice that it has no source code dependencies. Also, keep in mind that the [` ns `{.calibre4}]{.calibre_17} statement in Clojure has the same kind of source file requirement that Java has for classes. The source []{#index_split_032.html#filepos582448}file and the namespace have to have corresponding names.[]{#index_split_032.html#filepos582511}[[[[5]{.underline}]{.calibre_10}]{.calibre3}](#index_split_032.html#filepos582726) So, as we move the elements of this code into separate namespaces, we are also moving them into separate source files.

[[[5]{.underline}]{.calibre_10}](#index_split_032.html#filepos582511). In particular, the [` turn-on-light.switchable `{.calibre4}]{.calibre_17} namespace must be in a file named [` switchable.clj `{.calibre4}]{.calibre_17} within a directory named [` turn_on_light `{.calibre4}]{.calibre_17}.

Next, let's see the [` engage-switch `{.calibre4}]{.calibre_17} and [` variable-light `{.calibre4}]{.calibre_17} namespaces:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_241.html#filepos986123)

> > [[`(ns turn-on-light.engage-switch`{.calibre4}\
> > `  (:require [turn-on-light.switchable :as s]))`{.calibre4}\
> > \
> > `(defn engage-switch [switchable]`{.calibre4}\
> > `  ;Some other stuff...`{.calibre4}\
> > `  (s/turn-on switchable)`{.calibre4}\
> > `  ;Some more other stuff...`{.calibre4}\
> > `  (s/turn-off switchable))`{.calibre4}\
> > \
> > `————————————————`{.calibre4}\
> > \
> > `(ns turn-on-light.variable-light)`{.calibre4}\
> > \
> > `(defn turn-on-light [intensity]`{.calibre4}\
> > `  ;Turn it on with intensity.`{.calibre4}\
> > `  )`{.calibre4}]{.calibre_3}]{.calibre_17}

No real surprises here. The [` engage-switch `{.calibre4}]{.calibre_17} namespace depends upon the [` switchable `{.calibre4}]{.calibre_17} interface. The [` variable-light `{.calibre4}]{.calibre_17} namespace has no outgoing source code dependencies.

The [` variable-light-adapter `{.calibre4}]{.calibre_17} namespace connects the [` switchable `{.calibre4}]{.calibre_17} interface to the [` variable-light `{.calibre4}]{.calibre_17}. Notice the [` make-adapter `{.calibre4}]{.calibre_17} constructor. The tests will use that:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_242.html#filepos986269)

> > [[`(ns turn-on-light.variable-light-adapter`{.calibre4}\
> > `  (:require [turn-on-light.switchable :as s]`{.calibre4}\
> > `            [turn-on-light.variable-light :as v-l]))`{.calibre4}\
> > `(defn make-adapter []`{.calibre4}\
> > `  {:type :variable-light})`{.calibre4}\
> > \
> > `(defmethod s/turn-on :variable-light [switchable]`{.calibre4}\
> > `  (v-l/turn-on-light 100))`{.calibre4}\
> > \
> > `(defmethod s/turn-off :variable-light [switchable]`{.calibre4}\
> > `  (v-l/turn-on-light 0))`{.calibre4}]{.calibre_3}]{.calibre_17}
>
> []{#index_split_032.html#filepos585587}

And lastly, the test ties everything together in a nice, neat little ball by depending upon all the concrete namespaces:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_243.html#filepos986415)

> > [[`(ns turn-on-light.turn-on-spec`{.calibre4}\
> > `  (:require [speclj.core :refer :all]`{.calibre4}\
> > `            [turn-on-light.engage-switch :refer :all]`{.calibre4}\
> > `            [turn-on-light.variable-light :as v-l]`{.calibre4}\
> > `            [turn-on-light.variable-light-adapter`{.calibre4}\
> > `              :as v-l-adapter]))`{.calibre4}\
> > \
> > `(describe "Adapter"`{.calibre4}\
> > `  (with-stubs)`{.calibre4}\
> > `  (it "turns light on and off"`{.calibre4}\
> > `    (with-redefs [v-l/turn-on-light (stub :turn-on-light)]`{.calibre4}\
> > `      (engage-switch (v-l-adapter/make-adapter))`{.calibre4}\
> > `      (should-have-invoked :turn-on-light`{.calibre4}\
> > `                           {:times 1 :with [100]})`{.calibre4}\
> > `      (should-have-invoked :turn-on-light`{.calibre4}\
> > `                           {:times 1 :with [0]}))))`{.calibre4}]{.calibre_3}]{.calibre_17}

Look through those source code dependencies and compare them to the UML diagram, and you'll see that they match perfectly.

So which form of the Adapter pattern was this? We might call it the multi-method form; but it is also the object form.

Would it be possible, in Clojure, to build the class form of the Adapter pattern? No, because Clojure does not have inheritance of []{#index_split_032.html#filepos587478}implementation, and that's what the class form of the Adapter pattern depends upon.

So, although the Adapter pattern is not language specific, there are forms that are. It would not be possible, for example, to create the multi-method form of the Adapter pattern in Java.

[[Is That Really an Adapter Object?]{.calibre_3}]{.bold}

Perhaps you think that since the only data element in the [` variable-light-adapter `{.calibre4}]{.calibre_17} is the [` :type `{.calibre4}]{.calibre_17}, it is not really worthy of being called an object. OK then, here is a different version of the [` variable-light-adapter `{.calibre4}]{.calibre_17} that you might find more convincing:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_244.html#filepos986561)

> > [[`(ns turn-on-light.variable-light-adapter`{.calibre4}\
> > `  (:require [turn-on-light.switchable :as s]`{.calibre4}\
> > `            [turn-on-light.variable-light :as v-l]))`{.calibre4}\
> > \
> > `(defn make-adapter [`{.calibre4}]{.calibre_3}]{.calibre_17}[[`min-intensity max-intensity`{.calibre4}]{.calibre_3}]{.bold}[[`]`{.calibre4}\
> > `  {:type :variable-light`{.calibre4}\
> > `   `{.calibre4}]{.calibre_3}]{.calibre_17}[[`:min-intensity min-intensity`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `   `{.calibre4}]{.calibre_3}]{.calibre_17}[[`:max-intensity max-intensity`{.calibre4}]{.calibre_3}]{.bold}[[`})`{.calibre4}\
> > \
> > `(defmethod s/turn-on :variable-light [variable-light]`{.calibre4}\
> > `  (v-l/turn-on-light (`{.calibre4}]{.calibre_3}]{.calibre_17}[[`:max-intensity variable-light`{.calibre4}]{.calibre_3}]{.bold}[[`)))`{.calibre4}\
> > \
> > `(defmethod s/turn-off :variable-light [variable-light]`{.calibre4}\
> > `  (v-l/turn-on-light (`{.calibre4}]{.calibre_3}]{.calibre_17}[[`:min-intensity variable-light`{.calibre4}]{.calibre_3}]{.bold}[[`)))`{.calibre4}\
> > \
> > `————————`{.calibre4}\
> > \
> > `(ns turn-on-light.turn-on-spec`{.calibre4}\
> > `  (:require [speclj.core :refer :all]`{.calibre4}\
> > `            [turn-on-light.engage-switch :refer :all]`{.calibre4}\
> > `            [turn-on-light.variable-light :as v-l]`{.calibre4}\
> > `            [turn-on-light.variable-light-adapter`{.calibre4}\
> > `              :as v-l-adapter]))`{.calibre4}\
> > `(describe "Adapter"`{.calibre4}\
> > `  (with-stubs)`{.calibre4}\
> > `  (it "turns light on and off"`{.calibre4}\
> > `    (with-redefs [v-l/turn-on-light (stub :turn-on-light)]`{.calibre4}\
> > `      (engage-switch (v-l-adapter/make-adapter 5 90))`{.calibre4}\
> > `      (should-have-invoked :turn-on-light`{.calibre4}\
> > `                           {:times 1 :with [`{.calibre4}]{.calibre_3}]{.calibre_17}[[`90`{.calibre4}]{.calibre_3}]{.bold}[[`]})`{.calibre4}\
> > `      (should-have-invoked :turn-on-light`{.calibre4}\
> > `                           {:times 1 :with [`{.calibre4}]{.calibre_3}]{.calibre_17}[[`5`{.calibre4}]{.calibre_3}]{.bold}[[`]}))))`{.calibre4}]{.calibre_3}]{.calibre_17}
>
> []{#index_split_032.html#filepos591043}

By now, you should be convinced that this is the Adapter pattern, right out of the GOF[]{#index_split_032.html#filepos591190}[[[[6]{.underline}]{.calibre_10}]{.calibre3}](#index_split_032.html#filepos591568) book. You should also be expecting that many of the other GOF patterns can be expressed in functional languages like Clojure. And, perhaps more importantly, you should be thinking about namespace/source file structures as part of the design and architecture of functional programs.

[[[6]{.underline}]{.calibre_10}](#index_split_032.html#filepos591190). [GOF]{.italic} is the affectionate name we gave to the [Design Patterns]{.italic} book back in the '90s. It stands for "Gang of Four" because there were four authors: Erich Gamma, John Vlissides, Ralph Johnson, and Richard Helm.

[[[Command]{.calibre_3}]{.bold}]{.calibre1}

![](images/00236.jpg){.calibre_76}

Of all the design patterns in the GOF book, [Command]{.italic} is the one that intrigues me the most. Not because it is complicated, but because it is [simple]{.italic}. Very, very simple.

As an aside, this is also what intrigues me about Clojure. As I said in the introduction to this book, Clojure is semantically rich but syntactically trivial. Well, the Command pattern has the same attributes. Its richness is in its outrageous simplicity.

In C++, we might write the Command pattern as follows:

> > [[`class Command {`{.calibre4}\
> > `  public:`{.calibre4}\
> > `    virtual void execute() = 0;`{.calibre4}\
> > `};`{.calibre4}]{.calibre_3}]{.calibre_17}

That's it. Just one abstract class (interface) with a single, pure, virtual (abstract) function. So simple. But there are just so many interesting things you can do with this pattern. For a deep dive into this richness, see the corresponding chapter in [Agile Software Development: Principles, Patterns, and Practices]{.italic}.[]{#index_split_032.html#filepos593363}[[[[7]{.underline}]{.calibre_10}]{.calibre3}](#index_split_032.html#filepos593459)

[[[7]{.underline}]{.calibre_10}](#index_split_032.html#filepos593363). Martin, [Agile Software Development]{.italic}, p. 181.

In a functional language like Clojure, you might think that this pattern just disappears. After all, if you want to pass a command to some other function, you can just pass the [` command `{.calibre4}]{.calibre_17} function. You don't need to make an object out of it, because in functional languages, functions [are]{.italic} objects:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_245.html#filepos986707)

> > [[`(ns command.core)`{.calibre4}\
> > \
> > `(defn execute []`{.calibre4}\
> > `  )`{.calibre4}\
> > \
> > `(defn some-app [command]`{.calibre4}\
> > `  ;Some other stuff. . .`{.calibre4}\
> > `  (command)`{.calibre4}]{.calibre_3}]{.calibre_17}[[[[8]{.underline}]{.calibre_10}]{.calibre3}](#index_split_032.html#filepos595158)[[\
> > `  ;Some more other stuff. . .`{.calibre4}\
> > `  )`{.calibre4}\
> > \
> > `———————`{.calibre4}\
> > \
> > `(ns command.core-spec`{.calibre4}\
> > `  (:require [speclj.core :refer :all]`{.calibre4}\
> > `            [command.core :refer :all]))`{.calibre4}\
> > \
> > `(describe "command"`{.calibre4}\
> > `  (with-stubs)`{.calibre4}\
> > `  (it "executes the command"`{.calibre4}\
> > `    (with-redefs [execute (stub :execute)]`{.calibre4}\
> > `      (some-app execute)`{.calibre4}\
> > `      (should-have-invoked :execute))))`{.calibre4}]{.calibre_3}]{.calibre_17}
>
> []{#index_split_032.html#filepos595138}

[[[8]{.underline}]{.calibre_10}](#index_split_032.html#filepos595138). The careful reader will recognize that the command, as it is written, is not a pure (referentially transparent) function. It should be clear, however, that pure functions can be passed in the manner shown.

As you can see, the test passes the [` execute `{.calibre4}]{.calibre_17} function to [` some-app `{.calibre4}]{.calibre_17}, and the [` some-app `{.calibre4}]{.calibre_17} function invokes that command. No big deal.

Now, what if you wanted to create the command with a data element that will get passed as an argument to the execute function? In C++, we'd do that this way (pardon the inline functions):

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_246.html#filepos986853)

> > [[`class CommandWithArgument : public Command {`{.calibre4}\
> > `  public:`{.calibre4}\
> > `    CommandWithArgument(int argument)`{.calibre4}\
> > `    :argument(argument)`{.calibre4}\
> > `    {}`{.calibre4}\
> > \
> > `    virtual void execute()`{.calibre4}\
> > `    {theFunctionToExecute(argument);}`{.calibre4}\
> > \
> > `  private:`{.calibre4}\
> > `    int argument;`{.calibre4}\
> > \
> > `    void theFunctionToExecute(int argument)`{.calibre4}\
> > `    {`{.calibre4}\
> > `      //do something with that argument!`{.calibre4}\
> > `    }`{.calibre4}\
> > `};`{.calibre4}]{.calibre_3}]{.calibre_17}

In Clojure we'd do it like this, once again demonstrating that functions, in functional languages, are actually objects:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_247.html#filepos986999)

> > [[`(describe "command"`{.calibre4}\
> > `  (with-stubs)`{.calibre4}\
> > `  (it "executes the command"`{.calibre4}\
> > `    (with-redefs [execute (stub :execute)]`{.calibre4}\
> > `      (some-app `{.calibre4}]{.calibre_3}]{.calibre_17}[[`(partial execute :the-argument)`{.calibre4}]{.calibre_3}]{.bold}[[`)`{.calibre4}\
> > `      (should-have-invoked :execute `{.calibre4}]{.calibre_3}]{.calibre_17}[[`{:with [:the-argument]}`{.calibre4}]{.calibre_3}]{.bold}[[`))))`{.calibre4}\
> > \
> > `—————`{.calibre4}\
> > \
> > `(defn execute [`{.calibre4}]{.calibre_3}]{.calibre_17}[[`argument`{.calibre4}]{.calibre_3}]{.bold}[[`]`{.calibre4}\
> > `  )`{.calibre4}\
> > \
> > `(defn some-app [command]`{.calibre4}\
> > `  ;Some other stuff. . .`{.calibre4}\
> > `  (command)`{.calibre4}\
> > `  ;Some more other stuff. . .`{.calibre4}\
> > `  )`{.calibre4}]{.calibre_3}]{.calibre_17}

[[Undo]{.calibre_3}]{.bold}

One of the more useful variations of the Command pattern can be seen in the following C++ code:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_248.html#filepos987145)

> > [[`class UndoableCommand : public Command {`{.calibre4}\
> > `  public:`{.calibre4}\
> > `    virtual void undo() = 0;`{.calibre4}\
> > `};`{.calibre4}]{.calibre_3}]{.calibre_17}

That [` undo() `{.calibre4}]{.calibre_17} function opens up so many interesting possibilities.

Long ago, I worked on a GUI application that was an analog of AutoCAD. It was a drawing tool for architectural floor plans, roof plans, property line plans, and so on. The GUI was a typical palette/canvas. Users clicked in the palette to select the function they wanted, such as [Add a Room]{.italic}, and then they'd click in the canvas for placement and size.

Every click in the palette caused the appropriate derivative of the [` UndoableCommand `{.calibre4}]{.calibre_17} to be instantiated and executed. The execution managed the mouse/keyboard gestures in the canvas and then made the appropriate modifications to the internal data model. Thus, there was an [` UndoableCommand `{.calibre4}]{.calibre_17} derivative for every different function that the palette could offer.

When an [` UndoableCommand `{.calibre4}]{.calibre_17} had finished execution, it was pushed onto the [undo]{.italic} stack. Whenever the user clicked on the [undo]{.italic} icon in the palette, the [` UndoableCommand `{.calibre4}]{.calibre_17} on the top of the [undo]{.italic} stack was popped off and its [` undo `{.calibre4}]{.calibre_17} function was called.

As an [` UndoableCommand `{.calibre4}]{.calibre_17} object executed, it recorded what it did in such a way that the [` undo `{.calibre4}]{.calibre_17} function could reverse those changes. In C++, that recording was kept in the member variables of the particular [` UndoableCommand `{.calibre4}]{.calibre_17} object itself:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_249.html#filepos987290)

> > [[`class AddRoomCommand : public UndoableCommand {`{.calibre4}\
> > `  public:`{.calibre4}\
> > `    virtual void execute() {`{.calibre4}\
> > `      // manage canvas events to add room`{.calibre4}\
> > `      // record what was done in theAddedRoom`{.calibre4}\
> > `    }`{.calibre4}\
> > \
> > `    virtual void undo() {`{.calibre4}\
> > `      // remove theAddedRoom from the canvas`{.calibre4}\
> > `    }`{.calibre4}\
> > \
> > `  private:`{.calibre4}\
> > `    Room* theAddedRoom;`{.calibre4}\
> > `};`{.calibre4}]{.calibre_3}]{.calibre_17}

This is not functional, because the [` AddRoomCommand `{.calibre4}]{.calibre_17} object is mutable. But in a functional language, we can simply have the [` execute `{.calibre4}]{.calibre_17} function create a new instance of [` UndoableCommand `{.calibre4}]{.calibre_17}. Something like this:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_250.html#filepos987436)

> > [[`(ns command.undoable-command)`{.calibre4}\
> > \
> > `(defmulti execute :type)`{.calibre4}\
> > `(defmulti undo :type)`{.calibre4}\
> > \
> > `—————`{.calibre4}\
> > \
> > `(ns command.add-room-command`{.calibre4}\
> > `  (:require [command.undoable-command :as uc]))`{.calibre4}\
> > \
> > `(defn add-room []`{.calibre4}\
> > `  ;stuff that adds rooms to the canvas`{.calibre4}\
> > `  ;and returns the added room`{.calibre4}\
> > `  )`{.calibre4}\
> > \
> > `(defn delete-room [room]`{.calibre4}\
> > `  ;stuff that deletes the specified room from the canvas`{.calibre4}\
> > `  )`{.calibre4}\
> > \
> > `(defn make-add-room-command []`{.calibre4}\
> > `  {:type :add-room-command})`{.calibre4}\
> > \
> > `(defmethod uc/execute :add-room-command [command]`{.calibre4}\
> > `  (assoc (make-add-room-command) :the-added-room (add-room)))`{.calibre4}\
> > \
> > `(defmethod uc/undo :add-room-command [command]`{.calibre4}\
> > `  (delete-room (:the-added-room command)))`{.calibre4}\
> > \
> > `——————`{.calibre4}\
> > \
> > `(ns command.core`{.calibre4}\
> > `  (:require [command.undoable-command :as uc]`{.calibre4}\
> > `            [command.add-room-command :as ar]))`{.calibre4}\
> > \
> > `(defn gui-app [actions]`{.calibre4}\
> > `  (loop [actions actions`{.calibre4}\
> > `         undo-list (list)]`{.calibre4}\
> > `    (if (empty? actions)`{.calibre4}\
> > `      :DONE`{.calibre4}\
> > `      (condp = (first actions)`{.calibre4}\
> > `        :add-room-action`{.calibre4}\
> > `        (let [executed-command (uc/execute`{.calibre4}\
> > `                                 (ar/make-add-room-command))]`{.calibre4}\
> > `          (recur (rest actions)`{.calibre4}\
> > `                 (conj undo-list executed-command)))`{.calibre4}\
> > \
> > `        :undo-action`{.calibre4}\
> > `        (let [command-to-undo (first undo-list)]`{.calibre4}\
> > `          (uc/undo command-to-undo)`{.calibre4}\
> > `          (recur (rest actions)`{.calibre4}\
> > `                 (rest undo-list)))`{.calibre4}\
> > `        :TILT))))`{.calibre4}\
> > \
> > `————————`{.calibre4}\
> > \
> > `(ns command.core-spec`{.calibre4}\
> > `  (:require [speclj.core :refer :all]`{.calibre4}\
> > `            [command.core :refer :all]`{.calibre4}\
> > `            [command.add-room-command :as ar]))`{.calibre4}\
> > \
> > `(describe "command"`{.calibre4}\
> > `  (with-stubs)`{.calibre4}\
> > `  (it "executes the command"`{.calibre4}\
> > `    (with-redefs [ar/add-room (stub :add-room {:return :a-room})`{.calibre4}\
> > `                  ar/delete-room (stub :delete-room)]`{.calibre4}\
> > `      (gui-app [:add-room-action :undo-action])`{.calibre4}\
> > `      (should-have-invoked :add-room)`{.calibre4}\
> > `      (should-have-invoked :delete-room {:with [:a-room]}))))`{.calibre4}]{.calibre_3}]{.calibre_17}
>
> []{#index_split_032.html#filepos604889}

We create the [` undoable-command `{.calibre4}]{.calibre_17} interface using [` defmulti `{.calibre4}]{.calibre_17} functions. We implement that interface in the [` add-room-command `{.calibre4}]{.calibre_17} namespace, and we simulate the GUI in the [` gui-app `{.calibre4}]{.calibre_17} function of the [` command.core `{.calibre4}]{.calibre_17} namespace.

The test stubs out the low-level functions of the [` add-room-command `{.calibre4}]{.calibre_17} and makes sure they are called correctly. It calls the [` gui-app `{.calibre4}]{.calibre_17} with a list of [` palette-actions `{.calibre4}]{.calibre_17}.

The two methods of the [` add-room-command `{.calibre4}]{.calibre_17} are polymorphically dispatched. That might not seem necessary for the [` execute `{.calibre4}]{.calibre_17} case, since the [` gui-app `{.calibre4}]{.calibre_17} has just created the [` add-room-command `{.calibre4}]{.calibre_17} object. But were we to add more commands to this system, the polymorphic dispatch of [` execute `{.calibre4}]{.calibre_17} would become more necessary.

The polymorphic dispatch of [` undo `{.calibre4}]{.calibre_17} is clearly necessary, even in this small example, because by the time the [` :undo-action `{.calibre4}]{.calibre_17} is received from the palette, we have no idea which command is being undone.

Here, again, we see that as we add complexity to the application, the canonical form of the GOF pattern begins to assert itself. With the single method command, we could get away with using plain old functions (function objects, really). But when the application needed a richer kind of command, we fell back on the GOF style.

[[[Composite]{.calibre_3}]{.bold}]{.calibre1}

![](images/00298.jpg){.calibre_77}

[Composite]{.italic} continues the theme of semantic richness and syntactic triviality. It is a wonderful example of the old handle/body approach that []{#index_split_032.html#filepos607406}I first read about in one of Jim Coplien's books.[]{#index_split_032.html#filepos607464}[[[[9]{.underline}]{.calibre_10}]{.calibre3}](#index_split_032.html#filepos607700) The structure of the Composite pattern is depicted in the UML in [[[Figure 16.6]{.underline}]{.calibre_10}](#index_split_032.html#filepos607944).

[[[9]{.underline}]{.calibre_10}](#index_split_032.html#filepos607464). James O. Coplien, [Advanced C++ Programming Styles and Idioms]{.italic} (Addison-Wesley, 1991).

![](images/00066.jpg){#filepos607944 .calibre_78}

[[Figure 16.6.]{.bold}]{.calibre3}[ The Composite pattern]{.calibre3}

Our old friend the [` Switchable `{.calibre4}]{.calibre_17} interface is implemented by our other old friends, the [` Light `{.calibre4}]{.calibre_17} and the [` VariableLight `{.calibre4}]{.calibre_17}. The [` CompositeSwitchable `{.calibre4}]{.calibre_17} also implements [` Switchable `{.calibre4}]{.calibre_17} and contains a list of other instances of [` Switchable `{.calibre4}]{.calibre_17}.

The implementation of [` TurnOn `{.calibre4}]{.calibre_17} and [` TurnOff `{.calibre4}]{.calibre_17} in the [` CompositeSwitchable `{.calibre4}]{.calibre_17} simply propagates calls of the same functions to all the instances in the list. Thus, when you call [` TurnOn `{.calibre4}]{.calibre_17} on an instance of a [` CompositeSwitchable `{.calibre4}]{.calibre_17}, it will call [` TurnOn `{.calibre4}]{.calibre_17} on all the [` Switchable `{.calibre4}]{.calibre_17} instances it contains.

In Java, we might implement [` CompositeSwitchable `{.calibre4}]{.calibre_17} as follows:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_252.html#filepos987728)

> > [[`public class CompositeSwitchable implements Switchable {`{.calibre4}\
> > `  private List<Switchable> switchables = new ArrayList<>();`{.calibre4}\
> > \
> > `  public void addSwitchable(Switchable s) {`{.calibre4}\
> > `    switchables.add(s):`{.calibre4}\
> > `  }`{.calibre4}\
> > \
> > `  public void turnOn() {`{.calibre4}\
> > `    for (var s : switchables)`{.calibre4}\
> > `      s.turnOn();`{.calibre4}\
> > `  }`{.calibre4}\
> > \
> > `  public void turnOff() {`{.calibre4}\
> > `    for (var s : switchables)`{.calibre4}\
> > `      s.turnOff();`{.calibre4}\
> > `  }`{.calibre4}\
> > `}`{.calibre4}]{.calibre_3}]{.calibre_17}
>
> []{#index_split_032.html#filepos610302}

In a functional language, like Clojure, the temptation is to avoid the Composite pattern and simply use the [` map `{.calibre4}]{.calibre_17} or [` doseq `{.calibre4}]{.calibre_17} function, as you can see in the test below:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_253.html#filepos987874)

> > [[`(ns composite-example.switchable)`{.calibre4}\
> > \
> > `(defmulti turn-on :type)`{.calibre4}\
> > `(defmulti turn-off :type)`{.calibre4}\
> > \
> > `—————`{.calibre4}\
> > \
> > `(ns composite-example.light`{.calibre4}\
> > `  (:require [composite-example.switchable :as s]))`{.calibre4}\
> > \
> > `(defn make-light [] {:type :light})`{.calibre4}\
> > \
> > `(defn turn-on-light [])`{.calibre4}\
> > `(defn turn-off-light [])`{.calibre4}\
> > \
> > `(defmethod s/turn-on :light [switchable]`{.calibre4}\
> > `  (turn-on-light))`{.calibre4}\
> > \
> > `(defmethod s/turn-off :light [switchable]`{.calibre4}\
> > `  (turn-off-light))`{.calibre4}\
> > \
> > `———————`{.calibre4}\
> > \
> > `(ns composite-example.variable-light`{.calibre4}\
> > `  (:require [composite-example.switchable :as s]))`{.calibre4}\
> > \
> > `(defn make-variable-light [] {:type :variable-light})`{.calibre4}\
> > \
> > `(defn set-light-intensity [intensity])`{.calibre4}\
> > \
> > `(defmethod s/turn-on :variable-light [switchable]`{.calibre4}\
> > `  (set-light-intensity 100))`{.calibre4}\
> > \
> > `(defmethod s/turn-off :variable-light [switchable]`{.calibre4}\
> > `  (set-light-intensity 0))`{.calibre4}\
> > \
> > `———————————`{.calibre4}\
> > \
> > `(ns composite-example.core-spec`{.calibre4}\
> > `  (:require [speclj.core :refer :all]`{.calibre4}\
> > `            [composite-example`{.calibre4}\
> > `             [light :as l]`{.calibre4}\
> > `             [variable-light :as v]`{.calibre4}\
> > `             [switchable :as s]]))`{.calibre4}\
> > \
> > `(describe "composite-switchable"`{.calibre4}\
> > `  (with-stubs)`{.calibre4}\
> > `  (it "turns all on"`{.calibre4}\
> > `    (with-redefs`{.calibre4}\
> > `      [l/turn-on-light (stub :turn-on-light)`{.calibre4}\
> > `       v/set-light-intensity (stub :set-light-intensity)]`{.calibre4}\
> > `      (let [switchables [(l/make-light) (v/make-variable-light)]]`{.calibre4}\
> > `        (`{.calibre4}]{.calibre_3}]{.calibre_17}[[`doseq`{.calibre4}]{.calibre_3}]{.bold}[[` [s-able switchables] (s/turn-on s-able))`{.calibre4}\
> > `        (should-have-invoked :turn-on-light)`{.calibre4}\
> > `        (should-have-invoked :set-light-intensity`{.calibre4}\
> > `                             {:with [100]})))))`{.calibre4}]{.calibre_3}]{.calibre_17}

This accomplishes the goal of turning on all the lights, but it does so at the expense of externalizing the plurality of the lights. The point of the Composite pattern is to hide that plurality. So let's use the actual Composite pattern:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_255.html#filepos988166)

> > [[`(ns composite-example.composite-switchable`{.calibre4}\
> > `  (:require [composite-example.switchable :as s]))`{.calibre4}\
> > \
> > `(defn make-composite-switchable []`{.calibre4}\
> > `  {:type :composite-switchable`{.calibre4}\
> > `   :switchables []})`{.calibre4}\
> > \
> > `(defn add [composite-switchable switchable]`{.calibre4}\
> > `  (update composite-switchable :switchables conj switchable))`{.calibre4}\
> > \
> > `(defmethod s/turn-on :composite-switchable [c-switchable]`{.calibre4}\
> > `  (doseq [s-able (:switchables c-switchable)]`{.calibre4}\
> > `    (s/turn-on s-able)))`{.calibre4}\
> > \
> > `(defmethod s/turn-off :composite-switchable [c-switchable]`{.calibre4}\
> > `  (doseq [s-able (:switchables c-switchable)]`{.calibre4}\
> > `    (s/turn-off s-able)))`{.calibre4}\
> > \
> > `——————`{.calibre4}\
> > \
> > `(ns composite-example.core-spec`{.calibre4}\
> > `  (:require [speclj.core :refer :all]`{.calibre4}\
> > `            [composite-example`{.calibre4}\
> > `             [light :as l]`{.calibre4}\
> > `             [variable-light :as v]`{.calibre4}\
> > `             [switchable :as s]`{.calibre4}\
> > `             `{.calibre4}]{.calibre_3}]{.calibre_17}[[`[composite-switchable :as cs]`{.calibre4}]{.calibre_3}]{.bold}[[`]))`{.calibre4}\
> > \
> > `(describe "composite-switchable"`{.calibre4}\
> > `  (with-stubs)`{.calibre4}\
> > `  (it "turns all on"`{.calibre4}\
> > `    (with-redefs`{.calibre4}\
> > `      [l/turn-on-light (stub :turn-on-light)`{.calibre4}\
> > `       v/set-light-intensity (stub :set-light-intensity)]`{.calibre4}\
> > `      `{.calibre4}]{.calibre_3}]{.calibre_17}[[`(let [group (-> (cs/make-composite-switchable)`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `                      `{.calibre4}]{.calibre_3}]{.calibre_17}[[`(cs/add (l/make-light))`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `                      `{.calibre4}]{.calibre_3}]{.calibre_17}[[`(cs/add (v/make-variable-light)))]`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `        `{.calibre4}]{.calibre_3}]{.calibre_17}[[`(s/turn-on group)`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `        (should-have-invoked :turn-on-light)`{.calibre4}\
> > `        (should-have-invoked :set-light-intensity`{.calibre4}\
> > `                             {:with [100]})))))`{.calibre4}]{.calibre_3}]{.calibre_17}

The [` composite-switchable `{.calibre4}]{.calibre_17} implements the [` switchable `{.calibre4}]{.calibre_17} interface. The [` add `{.calibre4}]{.calibre_17} function is functional in that it returns a new [` composite-switchable `{.calibre4}]{.calibre_17} with the argument added to the [` :switchables `{.calibre4}]{.calibre_17} list. The [` turn-on `{.calibre4}]{.calibre_17} and [` turn-off `{.calibre4}]{.calibre_17}
[]{#index_split_032.html#filepos616793}methods use [` doseq `{.calibre4}]{.calibre_17} to iterate through the [` :switchables `{.calibre4}]{.calibre_17} list and propagate the appropriate function call. Finally, the test creates the [` composite-switchable `{.calibre4}]{.calibre_17}, adds a [` light `{.calibre4}]{.calibre_17} and [` variable-light `{.calibre4}]{.calibre_17}, and then invokes [` turn-on `{.calibre4}]{.calibre_17}. And we see both lights turned on appropriately.

[[Functional?]{.calibre_3}]{.bold}

At this point, you might be thinking that this is all well and good for objects that have side effects, like lights and variable lights. Indeed, the entire [` switchable `{.calibre4}]{.calibre_17} interface is oriented around the side effect of turning something on or off. So is this pattern only for objects with side effects?

Let's consider a [` shape `{.calibre4}]{.calibre_17} abstraction that looks like this:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_256.html#filepos988312)

> > [[`(ns composite-example.shape`{.calibre4}\
> > `  (:require [clojure.spec.alpha :as s]))`{.calibre4}\
> > \
> > `(s/def ::type keyword?)`{.calibre4}\
> > `(s/def ::shape-type (s/keys :req [::type]))`{.calibre4}\
> > \
> > `(defmulti translate (fn [shape dx dy] (::type shape)))`{.calibre4}\
> > `(defmulti scale (fn [shape factor] (::type shape)))`{.calibre4}]{.calibre_3}]{.calibre_17}

It's a straightforward interface with two methods: [` translate `{.calibre4}]{.calibre_17} and [` scale `{.calibre4}]{.calibre_17}. I also added a type specification for safety's sake. (This would be a good time to brush up on the double-colon syntax of namespaced keywords.) Every [` shape `{.calibre4}]{.calibre_17} will be a map that has a [` ::shape/type `{.calibre4}]{.calibre_17} element.

The [` circle `{.calibre4}]{.calibre_17} and [` square `{.calibre4}]{.calibre_17} implementations are also pretty straightforward, including their type specifications:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_257.html#filepos988458)

> > [[`(ns composite-example.circle`{.calibre4}\
> > `  (:require [clojure.spec.alpha :as s]`{.calibre4}\
> > `            [composite-example.shape :as shape]))`{.calibre4}\
> > \
> > `(s/def ::center (s/tuple number? number?))`{.calibre4}\
> > `(s/def ::radius number?)`{.calibre4}\
> > `(s/def ::circle (s/keys :req [::shape/type`{.calibre4}\
> > `                              ::radius`{.calibre4}\
> > `                              ::center]))`{.calibre4}\
> > \
> > `(defn make-circle [center radius]`{.calibre4}\
> > `  {:post [(s/valid? ::circle %)]}`{.calibre4}\
> > `  {::shape/type ::circle`{.calibre4}\
> > `   ::center center`{.calibre4}\
> > `   ::radius radius})`{.calibre4}\
> > \
> > `(defmethod shape/translate ::circle [circle dx dy]`{.calibre4}\
> > `  {:pre [(s/valid? ::circle circle)`{.calibre4}\
> > `         (number? dx) (number? dy)]`{.calibre4}\
> > `   :post [(s/valid? ::circle %)]}`{.calibre4}\
> > `  (let [[x y] (::center circle)]`{.calibre4}\
> > `    (assoc circle ::center [(+ x dx) (+ y dy)])))`{.calibre4}\
> > \
> > `(defmethod shape/scale ::circle [circle factor]`{.calibre4}\
> > `  {:pre [(s/valid? ::circle circle)`{.calibre4}\
> > `         (number? factor)]`{.calibre4}\
> > `   :post [(s/valid? ::circle %)]}`{.calibre4}\
> > `  (let [radius (::radius circle)]`{.calibre4}\
> > `    (assoc circle ::radius (* radius factor))))`{.calibre4}\
> > \
> > `———————`{.calibre4}\
> > \
> > `(ns composite-example.square`{.calibre4}\
> > `  (:require [clojure.spec.alpha :as s]`{.calibre4}\
> > `            [composite-example.shape :as shape]))`{.calibre4}\
> > \
> > `(s/def ::top-left (s/tuple number? number?))`{.calibre4}\
> > `(s/def ::side number?)`{.calibre4}\
> > `(s/def ::square (s/keys :req [::shape/type`{.calibre4}\
> > `                              ::side`{.calibre4}\
> > `                              ::top-left]))`{.calibre4}\
> > \
> > `(defn make-square [top-left side]`{.calibre4}\
> > `  {:post [(s/valid? ::square %)]}`{.calibre4}\
> > `  {::shape/type ::square`{.calibre4}\
> > `   ::top-left top-left`{.calibre4}\
> > `   ::side side})`{.calibre4}\
> > \
> > `(defmethod shape/translate ::square [square dx dy]`{.calibre4}\
> > `  {:pre [(s/valid? ::square square)`{.calibre4}\
> > `         (number? dx) (number? dy)]`{.calibre4}\
> > `   :post [(s/assert ::square %)]}`{.calibre4}\
> > `  (let [[x y] (::top-left square)]`{.calibre4}\
> > `    (assoc square ::top-left [(+ x dx) (+ y dy)])))`{.calibre4}\
> > \
> > `(defmethod shape/scale ::square [square factor]`{.calibre4}\
> > `  {:pre [(s/valid? ::square square)`{.calibre4}\
> > `         (number? factor)]`{.calibre4}\
> > `   :post [(s/valid? ::square %)]}`{.calibre4}\
> > `  (let [side (::side square)]`{.calibre4}\
> > `    (assoc square ::side (* side factor))))`{.calibre4}]{.calibre_3}]{.calibre_17}
>
> []{#index_split_032.html#filepos622333}

Notice the [` :pre `{.calibre4}]{.calibre_17} and [` :post `{.calibre4}]{.calibre_17} conditions on the methods. I'm using these to check the types coming into and going out of the functions. You could rightly be concerned about the runtime penalty of all those checks. I'd either globally disable[]{#index_split_032.html#filepos622723}[[[[10]{.underline}]{.calibre_10}]{.calibre3}](#index_split_032.html#filepos622920) them, or strategically comment them out once I was happy that my types were being managed properly.

[[[10]{.underline}]{.calibre_10}](#index_split_032.html#filepos622723). There is a compile-time switch that disables all asserts, including [` :pre `{.calibre4}]{.calibre_17} and [` :post `{.calibre4}]{.calibre_17}.

Notice that the [` translate `{.calibre4}]{.calibre_17} and [` scale `{.calibre4}]{.calibre_17} functions return new [` shape `{.calibre4}]{.calibre_17} instances. They are fully functional in their behavior.

So, now let's look at [` composite-shape `{.calibre4}]{.calibre_17}:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_259.html#filepos988750)

> > [[`(ns composite-example.composite-shape`{.calibre4}\
> > `  (:require [clojure.spec.alpha :as s]`{.calibre4}\
> > `            [composite-example.shape :as shape]))`{.calibre4}\
> > \
> > `(s/def ::shapes (s/coll-of ::shape/shape-type))`{.calibre4}\
> > `(s/def ::composite-shape (s/keys :req [::shape/type`{.calibre4}\
> > `                                       ::shapes]))`{.calibre4}\
> > \
> > `(defn make []`{.calibre4}\
> > `  {:post [(s/assert ::composite-shape %)]}`{.calibre4}\
> > `  {::shape/type ::composite-shape`{.calibre4}\
> > `   ::shapes []})`{.calibre4}\
> > \
> > `(defn add [cs shape]`{.calibre4}\
> > `  {:pre [(s/valid? ::composite-shape cs)`{.calibre4}\
> > `         (s/valid? ::shape/shape-type shape)]`{.calibre4}\
> > `   :post [(s/valid? ::composite-shape %)]}`{.calibre4}\
> > `  (update cs ::shapes conj shape))`{.calibre4}\
> > \
> > `(defmethod shape/translate ::composite-shape [cs dx dy]`{.calibre4}\
> > `  {:pre [(s/valid? ::composite-shape cs)`{.calibre4}\
> > `         (number? dx) (number? dy)]`{.calibre4}\
> > `   :post [(s/valid? ::composite-shape %)]}`{.calibre4}\
> > `  (let [translated-shapes (map #(shape/translate % dx dy)`{.calibre4}\
> > `                               (::shapes cs))]`{.calibre4}\
> > `    (assoc cs ::shapes translated-shapes)))`{.calibre4}\
> > \
> > `(defmethod shape/scale ::composite-shape [cs factor]`{.calibre4}\
> > `  {:pre [(s/valid? ::composite-shape cs)`{.calibre4}\
> > `         (number? factor)]`{.calibre4}\
> > `   :post [(s/valid? ::composite-shape %)]}`{.calibre4}\
> > `  (let [scaled-shapes (map #(shape/scale % factor)`{.calibre4}\
> > `                           (::shapes cs))]`{.calibre4}\
> > `    (assoc cs ::shapes scaled-shapes)))`{.calibre4}]{.calibre_3}]{.calibre_17}

We've seen this pattern before in the [` light `{.calibre4}]{.calibre_17}/[` variable-light `{.calibre4}]{.calibre_17} example. This time, however, the [` composite-shape `{.calibre4}]{.calibre_17} returns a new [` composite-shape `{.calibre4}]{.calibre_17} with the new [` shape `{.calibre4}]{.calibre_17} instances. And so it is functional.

For those of you who are curious, here are the tests I used:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_260.html#filepos988896)

> > [[`(ns composite-example.core-spec`{.calibre4}\
> > `  (:require [speclj.core :refer :all]`{.calibre4}\
> > `            [composite-example`{.calibre4}\
> > `             [square :as square]`{.calibre4}\
> > `             [shape :as shape]`{.calibre4}\
> > `             [circle :as circle]`{.calibre4}\
> > `             [composite-shape :as cs]]))`{.calibre4}\
> > \
> > `(describe "square"`{.calibre4}\
> > `  (it "translates"`{.calibre4}\
> > `    (let [s (square/make-square [3 4] 1)`{.calibre4}\
> > `          translated-square (shape/translate s 1 1)]`{.calibre4}\
> > `      (should= [4 5] (::square/top-left translated-square))`{.calibre4}\
> > `      (should= 1 (::square/side translated-square))))`{.calibre4}\
> > \
> > `  (it "scales"`{.calibre4}\
> > `    (let [s (square/make-square [1 2] 2)`{.calibre4}\
> > `          scaled-square (shape/scale s 5)]`{.calibre4}\
> > `      (should= [1 2] (::square/top-left scaled-square))`{.calibre4}\
> > `      (should= 10 (::square/side scaled-square)))))`{.calibre4}\
> > \
> > `(describe "circle"`{.calibre4}\
> > `  (it "translates"`{.calibre4}\
> > `    (let [c (circle/make-circle [3 4] 10)`{.calibre4}\
> > `          translated-circle (shape/translate c 2 3)]`{.calibre4}\
> > `      (should= [5 7] (::circle/center translated-circle))`{.calibre4}\
> > `      (should= 10 (::circle/radius translated-circle))))`{.calibre4}\
> > \
> > `  (it "scales"`{.calibre4}\
> > `    (let [c (circle/make-circle [1 2] 2)`{.calibre4}\
> > `          scaled-circle (shape/scale c 5)]`{.calibre4}\
> > `      (should= [1 2] (::circle/center scaled-circle))`{.calibre4}\
> > `      (should= 10 (::circle/radius scaled-circle)))))`{.calibre4}\
> > \
> > `(describe "composite shape"`{.calibre4}\
> > `  (it "translates"`{.calibre4}\
> > `    (let [cs (-> (cs/make)`{.calibre4}\
> > `                 (cs/add (square/make-square [0 0] 1))`{.calibre4}\
> > `                 (cs/add (circle/make-circle [10 10] 10)))`{.calibre4}\
> > `          translated-cs (shape/translate cs 3 4)]`{.calibre4}\
> > `      (should= #{{::shape/type ::square/square`{.calibre4}\
> > `                  ::square/top-left [3 4]`{.calibre4}\
> > `                  ::square/side 1}`{.calibre4}\
> > `                 {::shape/type ::circle/circle`{.calibre4}\
> > `                  ::circle/center [13 14]`{.calibre4}\
> > `                  ::circle/radius 10}}`{.calibre4}\
> > `               (set (::cs/shapes translated-cs)))))`{.calibre4}\
> > \
> > `  (it "scales"`{.calibre4}\
> > `    (let [cs (-> (cs/make)`{.calibre4}\
> > `                 (cs/add (square/make-square [0 0] 1))`{.calibre4}\
> > `                 (cs/add (circle/make-circle [10 10] 10)))`{.calibre4}\
> > `          scaled-cs (shape/scale cs 12)]`{.calibre4}\
> > `      (should= #{{::shape/type ::square/square`{.calibre4}\
> > `                  ::square/top-left [0 0]`{.calibre4}\
> > `                  ::square/side 12}`{.calibre4}\
> > `                 {::shape/type ::circle/circle`{.calibre4}\
> > `                  ::circle/center [10 10]`{.calibre4}\
> > `                  ::circle/radius 120}}`{.calibre4}\
> > `               (set (::cs/shapes scaled-cs))))))`{.calibre4}]{.calibre_3}]{.calibre_17}
>
> []{#index_split_032.html#filepos629815}

You may have noticed that as we proceed in these chapters, I'm using more of the nuanced features of Clojure. This is intentional. I expect that as you read this book, you will have a good Clojure reference nearby, so I'm giving you a series of opportunities to look things up and get more familiar with the language.

As we have seen, Composite is yet another GOF pattern that fits well into the functional world. Once we start taking advantage of polymorphic dispatch, with either vtables, multi-methods, or protocol/record structures, the GOF patterns fit right in, more or less as the GOF described them.

[[[Decorator]{.calibre_3}]{.bold}]{.calibre1}

![](images/00320.jpg){.calibre_79}

Yet another of the handle/body patterns is [Decorator]{.italic}. The Decorator pattern is a way to add functionality to a type model without directly modifying the type model.

For example, let's continue with our [` shape `{.calibre4}]{.calibre_17} project. We have a [` shape `{.calibre4}]{.calibre_17} type model that supports [` circle `{.calibre4}]{.calibre_17} and [` square `{.calibre4}]{.calibre_17} subtypes. Within that type model, so long as it conforms to the LSP, we can [` translate `{.calibre4}]{.calibre_17} and [` scale `{.calibre4}]{.calibre_17} any of the subtypes of [` shape `{.calibre4}]{.calibre_17} without knowing the explicit subtype we are manipulating.

Now let's add a new, optional functionality: a [` journaled-shape `{.calibre4}]{.calibre_17}. A [` journaled-shape `{.calibre4}]{.calibre_17} is a [` shape `{.calibre4}]{.calibre_17} that remembers the operations that have been performed on it since its creation. We want to be able to keep journals on [` square `{.calibre4}]{.calibre_17}s and [` circle `{.calibre4}]{.calibre_17}s; but only certain [` square `{.calibre4}]{.calibre_17}s and [` circle `{.calibre4}]{.calibre_17}s. We don't want every [` circle `{.calibre4}]{.calibre_17} and [` square `{.calibre4}]{.calibre_17} to be journaled, because the memory and processing penalty is too high.

Now, of course, we could implement this by adding a [` :journaled? `{.calibre4}]{.calibre_17} flag to the [` shape `{.calibre4}]{.calibre_17} abstraction and then putting an [` if `{.calibre4}]{.calibre_17} statement in the [` circle `{.calibre4}]{.calibre_17} and [` square `{.calibre4}]{.calibre_17} implementations. But that's messy. What we really want is a way to add this functionality without changing the [` shape `{.calibre4}]{.calibre_17} abstraction or any of its subtypes, including [` circle `{.calibre4}]{.calibre_17}, [` square `{.calibre4}]{.calibre_17}, and [` composite-shape `{.calibre4}]{.calibre_17} (the OCP).

Enter the Decorator pattern. The UML looks like [[[Figure 16.7]{.underline}]{.calibre_10}](#index_split_032.html#filepos633479).

![](images/00011.jpg){#filepos633479 .calibre_80}

[[Figure 16.7.]{.bold}]{.calibre3}[ The Decorator pattern]{.calibre3}

I've included the [` composite-shape `{.calibre4}]{.calibre_17} because it is currently part of the [` shape `{.calibre4}]{.calibre_17} type model. The [` journaled-shape `{.calibre4}]{.calibre_17} is the Decorator. The [` journaled-shape `{.calibre4}]{.calibre_17} derives from [` shape `{.calibre4}]{.calibre_17} and holds a reference to a [` shape `{.calibre4}]{.calibre_17}. When [` translate `{.calibre4}]{.calibre_17} or [` scale `{.calibre4}]{.calibre_17} is called on a [` journaled-shape `{.calibre4}]{.calibre_17} it creates an entry in the journal and then delegates the call to the contained [` shape `{.calibre4}]{.calibre_17}.

Here's the Clojure implementation:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_262.html#filepos989188)

> > [[`(ns decorator-example.journaled-shape`{.calibre4}\
> > `  (:require [decorator-example.shape :as shape]`{.calibre4}\
> > `            [clojure.spec.alpha :as s]))`{.calibre4}\
> > \
> > `(s/def ::journal-entry`{.calibre4}\
> > `       (s/or :translate (s/tuple #{:translate}`{.calibre4}]{.calibre_3}]{.calibre_17}[[[[11]{.underline}]{.calibre_10}]{.calibre3}](#index_split_032.html#filepos636999)[[` number? number?)`{.calibre4}\
> > `             :scale (s/tuple #{:scale} number?)))`{.calibre4}\
> > `(s/def ::journal (s/coll-of ::journal-entry))`{.calibre4}\
> > `(s/def ::shape ::shape/shape-type)`{.calibre4}\
> > `(s/def ::journaled-shape (s/and`{.calibre4}\
> > `                           (s/keys :req [::shape/type`{.calibre4}\
> > `                                         ::journal`{.calibre4}\
> > `                                         ::shape])`{.calibre4}\
> > `                           #(= ::journaled-shape`{.calibre4}\
> > `                               (::shape/type %))))`{.calibre4}\
> > \
> > `(defn make [shape]`{.calibre4}\
> > `  {:post [(s/valid? ::journaled-shape %)]}`{.calibre4}\
> > `  {::shape/type ::journaled-shape`{.calibre4}\
> > `   ::journal []`{.calibre4}\
> > `   ::shape shape})`{.calibre4}\
> > \
> > `(defmethod shape/translate ::journaled-shape [js dx dy]`{.calibre4}\
> > `  {:pre [(s/valid? ::journaled-shape js)`{.calibre4}\
> > `         (number? dx) (number? dy)]`{.calibre4}\
> > `   :post [(s/valid? ::journaled-shape %)]}`{.calibre4}\
> > `  (-> js (update ::journal conj [:translate dx dy])`{.calibre4}\
> > `      (assoc ::shape (shape/translate (::shape js) dx dy))))`{.calibre4}\
> > \
> > `(defmethod shape/scale ::journaled-shape [js factor]`{.calibre4}\
> > `  {:pre [(s/valid? ::journaled-shape js)`{.calibre4}\
> > `         (number? factor)]`{.calibre4}\
> > `   :post [(s/valid? ::journaled-shape %)]}`{.calibre4}\
> > `  (-> js (update ::journal conj [:scale factor])`{.calibre4}\
> > `      (assoc ::shape (shape/scale (::shape js) factor))))`{.calibre4}]{.calibre_3}]{.calibre_17}
>
> []{#index_split_032.html#filepos636979}

[[[11]{.underline}]{.calibre_10}](#index_split_032.html#filepos636979). A set can be used as a function that tests for membership.

The [` ::journaled-shape `{.calibre4}]{.calibre_17} object has [` ::shape `{.calibre4}]{.calibre_17} and [` ::journal `{.calibre4}]{.calibre_17} fields. The [` ::journal `{.calibre4}]{.calibre_17} field is a collection of [` ::journal-entry `{.calibre4}]{.calibre_17} tuples that are of the form [` [:translate dx dy] `{.calibre4}]{.calibre_17} or [` [:scale factor] `{.calibre4}]{.calibre_17} where [` dx `{.calibre4}]{.calibre_17}, [` dy `{.calibre4}]{.calibre_17}, and [` factor `{.calibre4}]{.calibre_17} are numbers. The [` ::shape `{.calibre4}]{.calibre_17} field must contain a valid [` shape `{.calibre4}]{.calibre_17}.

The [` make `{.calibre4}]{.calibre_17} constructor creates a valid [` journaled-shape `{.calibre4}]{.calibre_17} (as checked by the [` :post `{.calibre4}]{.calibre_17} condition).

The [` translate `{.calibre4}]{.calibre_17} and [` scale `{.calibre4}]{.calibre_17} functions add the appropriate journal entry to the [` ::journal `{.calibre4}]{.calibre_17} and then delegate their respective functions to the [` ::shape `{.calibre4}]{.calibre_17}, returning a new [` journaled-shape `{.calibre4}]{.calibre_17} with the updated [` ::journal `{.calibre4}]{.calibre_17} and the modified [` ::shape `{.calibre4}]{.calibre_17}.

Here's the test. I only tested the [` journaled-shape `{.calibre4}]{.calibre_17} with a [` square `{.calibre4}]{.calibre_17} because if it works for [` square `{.calibre4}]{.calibre_17}, it will work for every [` shape `{.calibre4}]{.calibre_17}:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_263.html#filepos989334)

> > [[`(describe "journaled shape decorator"`{.calibre4}\
> > `  (it "journals scale and translate operations"`{.calibre4}\
> > `    (let [jsd (-> (js/make (square/make-square [0 0] 1))`{.calibre4}\
> > `                  (shape/translate 2 3)`{.calibre4}\
> > `                  (shape/scale 5))]`{.calibre4}\
> > `      (should= [[:translate 2 3] [:scale 5]]`{.calibre4}\
> > `               (::js/journal jsd))`{.calibre4}\
> > `      (should= {::shape/type ::square/square`{.calibre4}\
> > `                ::square/top-left [2 3]`{.calibre4}\
> > `                ::square/side 5}`{.calibre4}\
> > `               (::js/shape jsd)))))`{.calibre4}]{.calibre_3}]{.calibre_17}

We make a [` journaled-shape `{.calibre4}]{.calibre_17} with a [` square `{.calibre4}]{.calibre_17} in it. We [` translate `{.calibre4}]{.calibre_17} and [` scale `{.calibre4}]{.calibre_17} it, and then we make sure the [` ::journal `{.calibre4}]{.calibre_17} has recorded the [` translate `{.calibre4}]{.calibre_17} and [` scale `{.calibre4}]{.calibre_17} calls and that the [` square `{.calibre4}]{.calibre_17} has the translated and scaled values.

Once again, I've included the type specifications just to give you a challenge and to demonstrate how they can be used. Frankly, however, I think the tests do an adequate job of checking the types; so in real life, I doubt I would use such detailed type specifications for this kind of small problem. On the other hand, it is kind of nice to see the types all spelled out like that.

In any case, notice that the [` journaled-shape `{.calibre4}]{.calibre_17} Decorator will work for any [` shape `{.calibre4}]{.calibre_17}, including a [` composite-shape `{.calibre4}]{.calibre_17}. So we have effectively added a new functionality to the type model without making any changes to the existing element of that type model. That's the OCP at work.

[[[Visitor]{.calibre_3}]{.bold}]{.calibre1}

![](images/00327.jpg){.calibre_28}

Oh, no! Not the. . . [Visitor]{.italic}! Yes, we're going to investigate the much-maligned Visitor pattern. Visitor is not one of the handle/body patterns. It has its own unique structure that, as we'll see, is complicated by certain language choices.

The purpose of the Visitor pattern is similar to that of the Decorator pattern. We want to add a new function to an existing type model without changing that type model (the OCP). The Decorator is appropriate when the new function is independent of the other subtypes in the type model. Look back at the [` journaled-shape `{.calibre4}]{.calibre_17} to verify this constraint. The journaling was independent of whether the contained shape was a [` circle `{.calibre4}]{.calibre_17} or a [` square `{.calibre4}]{.calibre_17}. The [` journaled-shape `{.calibre4}]{.calibre_17} Decorator never knew the subtype of the contained [` shape `{.calibre4}]{.calibre_17}.

We use the Visitor pattern when the function we wish to add is [dependent]{.italic} upon the subtypes in the type model.

So, for example, what if we wanted to add a function to our shape abstraction for converting the shape to a string for serialization purposes? We could add a [` to-string `{.calibre4}]{.calibre_17} function to the [` shape `{.calibre4}]{.calibre_17} interface. Easy-peasy.

But wait! What if one of our customers wanted the shapes in XML? I suppose we could add a [` to-xml `{.calibre4}]{.calibre_17} function as well as the [` to-string `{.calibre4}]{.calibre_17} function.

But, wait again! What if another of our customers wanted the shapes in JSON, and yet another wanted them in YAML, and. . .

At some point, you realize that there is no end to these data formats and that customers are going to continually ask you for more and more and more. And you don't want to pollute the [` shape `{.calibre4}]{.calibre_17} interface with all those horrible methods.

The Visitor pattern gives us a way out of this dilemma. The UML looks something like [[[Figure 16.8]{.underline}]{.calibre_10}](#index_split_032.html#filepos644502).

![](images/00046.jpg){#filepos644502 .calibre_81}

[[Figure 16.8.]{.bold}]{.calibre3}[ The Visitor pattern]{.calibre3}

The first thing I want to point out is the 90-degree rotation of the [` Shape `{.calibre4}]{.calibre_17} subtypes into methods in the [` ShapeVisitor `{.calibre4}]{.calibre_17}. Each of the subtypes, [` Square `{.calibre4}]{.calibre_17} and [` Circle `{.calibre4}]{.calibre_17}, is the type of the argument of a [` visit `{.calibre4}]{.calibre_17} function in the [` ShapeVisitor `{.calibre4}]{.calibre_17}. I call the subtype-to-method transformation a 90-degree rotation because it pleases some neurons in my hindbrain.

We see our [` Shape `{.calibre4}]{.calibre_17} abstraction and all its subtypes over on the left. On the right, we see the [` ShapeVisitor `{.calibre4}]{.calibre_17} hierarchy. The pattern adds the [` accept `{.calibre4}]{.calibre_17}
[]{#index_split_032.html#filepos645672}function to the [` Shape `{.calibre4}]{.calibre_17} interface. That function takes a single argument, which is a [` ShapeVisitor `{.calibre4}]{.calibre_17}. This violates the OCP, but only once.

In Java, the implementation of the [` accept `{.calibre4}]{.calibre_17} function is trivial:

> > [[`void accept(ShapeVisitor v) {`{.calibre4}\
> > `  v.visit(this);`{.calibre4}\
> > `}`{.calibre4}]{.calibre_3}]{.calibre_17}

If you've never studied the Visitor pattern before, then this might be a little difficult to follow. So take your time and walk through this with me.

Let's say we want a JSON string for some [` Shape `{.calibre4}]{.calibre_17} we've got. In Java, or C++ or other similar languages, here's how we'd get it:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_264.html#filepos989480)

> > [[`Shape s = // get a shape without knowing the subtype`{.calibre4}\
> > `ShapeVisitor v = new JsonVisitor();`{.calibre4}\
> > `s.accept(v);`{.calibre4}\
> > `String json = v.getJson();`{.calibre4}]{.calibre_3}]{.calibre_17}

We get a [` Shape `{.calibre4}]{.calibre_17} object from somewhere. We create the [` JsonVisitor `{.calibre4}]{.calibre_17}. We pass the [` JsonVisitor `{.calibre4}]{.calibre_17} to our [` Shape `{.calibre4}]{.calibre_17} using the [` accept `{.calibre4}]{.calibre_17} method. The [` accept `{.calibre4}]{.calibre_17} method polymorphically dispatches to the proper subtype of [` Shape `{.calibre4}]{.calibre_17}---let's say it's a [` Square `{.calibre4}]{.calibre_17}. The [` accept `{.calibre4}]{.calibre_17} method of [` Square `{.calibre4}]{.calibre_17} calls [` visit(this) `{.calibre4}]{.calibre_17} on the [` JsonVisitor `{.calibre4}]{.calibre_17}. The type of [` this `{.calibre4}]{.calibre_17} is [` Square `{.calibre4}]{.calibre_17}, so the [` visit(Square s) `{.calibre4}]{.calibre_17} function of the [` JsonVisitor `{.calibre4}]{.calibre_17} is called. That function generates the JSON string for the [` Square `{.calibre4}]{.calibre_17} and saves it in a member variable of the [` JsonVisitor `{.calibre4}]{.calibre_17}. The [` getJson() `{.calibre4}]{.calibre_17} function returns the contents of that member variable.

You may have to read that over a few times to follow it. This is a technique called [double-dispatch]{.italic}. The first dispatch deploys to the subtype of the [` Shape `{.calibre4}]{.calibre_17}, so now we know the type of that subtype. The second dispatch deploys to the proper subtype of the visitor passing along the true type of the subtype.

If you followed all of that, you can see that each of the derivatives of the [` ShapeVisitor `{.calibre4}]{.calibre_17} is a new "method" of the [` Shape `{.calibre4}]{.calibre_17} type model, but the only []{#index_split_032.html#filepos649292}thing we had to add to [` Shape `{.calibre4}]{.calibre_17} was the [` accept `{.calibre4}]{.calibre_17} method. So \~(the OCP). You should also now understand why we couldn't use a Decorator. The new functions depend strongly on the subtypes. You can't make a JSON string for a [` Square `{.calibre4}]{.calibre_17} if you don't know it's a [` Square `{.calibre4}]{.calibre_17}.

Now, I told you all that so I could tell you this. All that horrible complexity is there because of a language constraint. Yes, yes. . . this is where all those design pattern naysayers actually do have a point. The Visitor pattern is as complex as it is because of a particular language feature.

What feature is that? [Closed classes]{.italic}.

[[To Close, or to Clojure?]{.calibre_3}]{.bold}

In languages like C++ and Java, we create classes that are [closed]{.italic}. What that means is that we cannot add a new method to a class by putting that new method's declaration in a new source file. If we want to add a new method to a class, in a closed language, we have to open the source file of that class and add the method [within]{.italic} the definition of that class.

Clojure does not have this constraint. Neither, to some extent, does C#. Indeed, many languages allow you to add methods to classes without changing the source file that contains the declaration of those classes.

The reason Clojure does not have this constraint is that classes are not a feature of the language. We create them by convention, not by syntax.

So, wait, does that mean we don't need the Decorator or Visitor pattern in Clojure? No, it doesn't mean that at all. Indeed, as we saw, we still need the Decorator in its GOF form. How else would you do the [` journaled-shape `{.calibre4}]{.calibre_17}?

However, the GOF form of the Visitor is not necessary in languages that have open classes. Or rather, some of the details of the GOF form are not necessary.

So let me show you this particular Visitor in Clojure. First, the tests:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_265.html#filepos989625)

> > [[`(ns visitor-example.core-spec`{.calibre4}\
> > `  (:require [speclj.core :refer :all]`{.calibre4}\
> > `            [visitor-example`{.calibre4}\
> > `             [square :as square]`{.calibre4}\
> > `             [json-shape-visitor :as jv]`{.calibre4}\
> > `             [circle :as circle]]))`{.calibre4}\
> > \
> > `(describe "shape-visitor"`{.calibre4}\
> > `  (it "makes json square"`{.calibre4}\
> > `    (should= "{\"top-left\": [0,0], \"side\": 1}"`{.calibre4}\
> > `             (jv/to-json (square/make [0 0] 1))))`{.calibre4}\
> > \
> > `  (it "makes json circle"`{.calibre4}\
> > `    (should= "{\"center\": [3,4], \"radius\": 1}"`{.calibre4}\
> > `             (jv/to-json (circle/make [3 4] 1)))))`{.calibre4}]{.calibre_3}]{.calibre_17}

This shouldn't be too surprising; although you should pay special attention to the source code dependencies. This test needs pretty much everything.

Now let's remember what the [` shape `{.calibre4}]{.calibre_17} type model looks like. Just to keep things simple, I've removed all the [` clojure.spec `{.calibre4}]{.calibre_17} type specifications:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_266.html#filepos989771)

> > [[`(ns visitor-example.shape)`{.calibre4}\
> > \
> > `(defmulti translate (fn [shape dx dy] (::type shape)))`{.calibre4}\
> > `(defmulti scale (fn [shape factor] (::type shape)))`{.calibre4}\
> > \
> > `———————`{.calibre4}\
> > \
> > `(ns visitor-example.square`{.calibre4}\
> > `  (:require`{.calibre4}\
> > `    [visitor-example.shape :as shape]))`{.calibre4}\
> > \
> > `(defn make [top-left side]`{.calibre4}\
> > `  {::shape/type ::square`{.calibre4}\
> > `   ::top-left top-left`{.calibre4}\
> > `   ::side side})`{.calibre4}\
> > \
> > `(defmethod shape/translate ::square [square dx dy]`{.calibre4}\
> > `  (let [[x y] (::top-left square)]`{.calibre4}\
> > `    (assoc square ::top-left [(+ x dx) (+ y dy)])))`{.calibre4}\
> > \
> > `(defmethod shape/scale ::square [square factor]`{.calibre4}\
> > `  (let [side (::side square)]`{.calibre4}\
> > `    (assoc square ::side (* side factor))))`{.calibre4}\
> > \
> > `————————`{.calibre4}\
> > \
> > `(ns visitor-example.circle`{.calibre4}\
> > `  (:require`{.calibre4}\
> > `    [visitor-example.shape :as shape]))`{.calibre4}\
> > \
> > `(defn make [center radius]`{.calibre4}\
> > `  {::shape/type ::circle`{.calibre4}\
> > `   ::center center`{.calibre4}\
> > `   ::radius radius})`{.calibre4}\
> > \
> > `(defmethod shape/translate ::circle [circle dx dy]`{.calibre4}\
> > `  (let [[x y] (::center circle)]`{.calibre4}\
> > `    (assoc circle ::center [(+ x dx) (+ y dy)])))`{.calibre4}\
> > \
> > `(defmethod shape/scale ::circle [circle factor]`{.calibre4}\
> > `  (let [radius (::radius circle)]`{.calibre4}\
> > `    (assoc circle ::radius (* radius factor))))`{.calibre4}]{.calibre_3}]{.calibre_17}

That should all look pretty familiar. Now for the [` json-shape-visitor `{.calibre4}]{.calibre_17}:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_267.html#filepos989918)

> > [[`(ns visitor-example.json-shape-visitor`{.calibre4}\
> > `  (:require [visitor-example`{.calibre4}\
> > `             [shape :as shape]`{.calibre4}\
> > `             [circle :as circle]`{.calibre4}\
> > `             [square :as square]]))`{.calibre4}\
> > \
> > `(defmulti to-json ::shape/type)`{.calibre4}\
> > \
> > `(defmethod to-json ::square/square [square]`{.calibre4}\
> > `  (let [{:keys [::square/top-left`{.calibre4}]{.calibre_3}]{.calibre_17}[[[[12]{.underline}]{.calibre_10}]{.calibre3}](#index_split_032.html#filepos656563)[[` ::square/side]} square`{.calibre4}\
> > `        [x y] top-left]`{.calibre4}\
> > `    (format "{\"top-left\": [%s,%s], \"side\": %s}" x y side)))`{.calibre4}\
> > \
> > `(defmethod to-json ::circle/circle [circle]`{.calibre4}\
> > `  (let [{:keys [::circle/center ::circle/radius]} circle`{.calibre4}\
> > `        [x y] center]`{.calibre4}\
> > `    (format "{\"center\": [%s,%s], \"radius\": %s}" x y radius)))`{.calibre4}]{.calibre_3}]{.calibre_17}
>
> []{#index_split_032.html#filepos656543}

[[[12]{.underline}]{.calibre_10}](#index_split_032.html#filepos656543). The namespaced keyword [destructuring]{.italic} creates a local var named for the local part of the key---[` top-left `{.calibre4}]{.calibre_17} in this case.

Look at this carefully. That [` defmulti `{.calibre4}]{.calibre_17} in the [` json-shape-visitor `{.calibre4}]{.calibre_17} adds the [` to-json `{.calibre4}]{.calibre_17} method directly into the [` shape `{.calibre4}]{.calibre_17} type model. You probably understand it well enough at this point; but do you see [why]{.italic} this is a Visitor?

Can you see the 90-degree rotation from subtypes to functions?

Just like the Java version of the Visitor, all the subtypes for the [` to-json `{.calibre4}]{.calibre_17} operation are gathered into the [` json-shape-visitor `{.calibre4}]{.calibre_17} module.

If you follow all the source code dependencies and compare them to the UML diagram, you'll see that they are all there. The only things missing are the [` ShapeVisitor `{.calibre4}]{.calibre_17} interface and the dual dispatch. Those were just there to get around the fact that languages like C++ and Java have closed classes.

This tells us that the GOF got this pattern a bit wrong. The dual dispatch is ancillary to the Visitor pattern and is only necessary in languages with closed classes.

[[The 90-degree Problem]{.calibre_3}]{.bold}

But wait. That 90-degree rotation has a problem. Whenever you have a module that has methods for each of the subtypes of some type model, that module must be changed whenever the type model is changed. For example, if we were to add a [` triangle `{.calibre4}]{.calibre_17} to our [` shape `{.calibre4}]{.calibre_17} hierarchy, our []{#index_split_032.html#filepos658766}[` json-shape-visitor `{.calibre4}]{.calibre_17} would need a [` ::triangle/triangle defmethod `{.calibre4}]{.calibre_17} of [` to-json `{.calibre4}]{.calibre_17}. This violates the OCP.

This is also a problem because it violates the [Dependency Rule]{.italic} of [Clean Architecture]{.italic}[]{#index_split_032.html#filepos659145}[[[[13]{.underline}]{.calibre_10}]{.calibre3}](#index_split_032.html#filepos659562) by forcing higher-level modules to have source code dependencies upon lower-level modules across an architectural boundary.[]{#index_split_032.html#filepos659362}[[[[14]{.underline}]{.calibre_10}]{.calibre3}](#index_split_032.html#filepos659742) This is shown in the UML in [[[Figure 16.9]{.underline}]{.calibre_10}](#index_split_032.html#filepos659939).

[[[13]{.underline}]{.calibre_10}](#index_split_032.html#filepos659145). Robert C. Martin, [Clean Architecture]{.italic} (Pearson, 2017), p. 203.

[[[14]{.underline}]{.calibre_10}](#index_split_032.html#filepos659362). Martin, [Clean Architecture]{.italic}, p. 159.

![](images/00094.jpg){#filepos659939 .calibre_82}

[[Figure 16.9.]{.bold}]{.calibre3}[ Violation of the Dependency Rule]{.calibre3}

In general, we want the [` shape `{.calibre4}]{.calibre_17} implementations to be plug-ins to the [` App `{.calibre4}]{.calibre_17}. But the [` json-shape-visitor `{.calibre4}]{.calibre_17} thwarts that because the only way for our [` App `{.calibre4}]{.calibre_17} to emit JSON is to invoke the [` json-shape-visitor `{.calibre4}]{.calibre_17}, which depends directly on [` circle `{.calibre4}]{.calibre_17} and [` square `{.calibre4}]{.calibre_17}.

In Java, C#, and C++, we can solve this by using an [abstract factory]{.italic}, which the [` App `{.calibre4}]{.calibre_17} could use to instantiate the [` visitor `{.calibre4}]{.calibre_17} object without depending directly upon it.

In Clojure, we have another---and much better---option. We can just separate the interface of the [` json-shape-visitor `{.calibre4}]{.calibre_17} from its implementation as follows:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_268.html#filepos990064)

> > [[`(ns visitor-example.json-shape-visitor`{.calibre4}\
> > `  (:require [visitor-example`{.calibre4}\
> > `             [shape :as shape]]))`{.calibre4}\
> > `(defmulti to-json ::shape/type)`{.calibre4}\
> > \
> > `————————`{.calibre4}\
> > \
> > `(ns visitor-example.json-shape-visitor`{.calibre4}]{.calibre_3}]{.calibre_17}[[`-implementation`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `  (:require [visitor-example`{.calibre4}\
> > `             `{.calibre4}]{.calibre_3}]{.calibre_17}[[`[json-shape-visitor :as v]`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `             [circle :as circle]`{.calibre4}\
> > `             [square :as square]]))`{.calibre4}\
> > \
> > `(defmethod `{.calibre4}]{.calibre_3}]{.calibre_17}[[`v/`{.calibre4}]{.calibre_3}]{.bold}[[`to-json ::square/square [square]`{.calibre4}\
> > `  (let [{:keys [::square/top-left ::square/side]} square`{.calibre4}\
> > `        [x y] top-left]`{.calibre4}\
> > `    (format "{\"top-left\": [%s,%s], \"side\": %s}" x y side)))`{.calibre4}\
> > \
> > `(defmethod `{.calibre4}]{.calibre_3}]{.calibre_17}[[`v/`{.calibre4}]{.calibre_3}]{.bold}[[`to-json ::circle/circle [circle]`{.calibre4}\
> > `  (let [{:keys [::circle/center ::circle/radius]} circle`{.calibre4}\
> > `        [x y] center]`{.calibre4}\
> > `    (format "{\"center\": [%s,%s], \"radius\": %s}" x y radius)))`{.calibre4}]{.calibre_3}]{.calibre_17}

The trick to this is to make sure that the [` json-shape-visitor-implementation `{.calibre4}]{.calibre_17} module is [` require `{.calibre4}]{.calibre_17}d by [` main `{.calibre4}]{.calibre_17} so that the [` defmethod `{.calibre4}]{.calibre_17}s are properly registered with the [` defmulti `{.calibre4}]{.calibre_17}:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_269.html#filepos990210)

> > [[`(ns visitor-example.main`{.calibre4}\
> > `  (:require [visitor-example`{.calibre4}\
> > `             [json-shape-visitor-implementation]]))`{.calibre4}]{.calibre_3}]{.calibre_17}

Typically, [` main `{.calibre4}]{.calibre_17} is invoked before any part of the application, and thus, the application does not have a source code dependency on [` main `{.calibre4}]{.calibre_17}.[]{#index_split_032.html#filepos664232}[[[[15]{.underline}]{.calibre_10}]{.calibre3}](#index_split_032.html#filepos664470) Unfortunately, my tests do not have access to a true [` main `{.calibre4}]{.calibre_17}, so the dependency has to be included:

[[[15]{.underline}]{.calibre_10}](#index_split_032.html#filepos664232). Martin, [Clean Architecture]{.italic}, p. 231.

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_270.html#filepos990355)

> > [[`(ns visitor-example.core-spec`{.calibre4}\
> > `  (:require [speclj.core :refer :all]`{.calibre4}\
> > `            [visitor-example`{.calibre4}\
> > `             [square :as square]`{.calibre4}\
> > `             [json-shape-visitor :as jv]`{.calibre4}\
> > `             [circle :as circle]`{.calibre4}\
> > `             `{.calibre4}]{.calibre_3}]{.calibre_17}[[`[main]`{.calibre4}]{.calibre_3}]{.bold}[[`]))`{.calibre4}\
> > \
> > `(describe "shape-visitor"`{.calibre4}\
> > `  (it "makes json square"`{.calibre4}\
> > `    (should= "{\"top-left\": [0,0], \"side\": 1}"`{.calibre4}\
> > `             (jv/to-json (square/make [0 0] 1))))`{.calibre4}\
> > \
> > `  (it "makes json circle"`{.calibre4}\
> > `    (should= "{\"center\": [3,4], \"radius\": 1}"`{.calibre4}\
> > `             (jv/to-json (circle/make [3 4] 1)))))`{.calibre4}]{.calibre_3}]{.calibre_17}
>
> []{#index_split_032.html#filepos665792}

So there it is, a functional, and architecturally competent, Visitor in Clojure. As the UML in [[[Figure 16.10]{.underline}]{.calibre_10}](#index_split_032.html#filepos666205) shows, all the dependencies cross the architectural boundary pointing to the higher-level (abstract) side of that boundary. Hallelujah!

![](images/00134.jpg){#filepos666205 .calibre_83}

[[Figure 16.10.]{.bold}]{.calibre3}[ Functional and architecturally competent Visitor]{.calibre3}

So the Visitor pattern is a case where the GOF form was polluted by the language constraints of the day. In 1995, when the GOF book was published, closed classes were considered a necessary attribute of statically typed languages and were therefore almost ubiquitous.

[[[Abstract Factory]{.calibre_3}]{.bold}]{.calibre1}

![](images/00183.jpg){.calibre_84}

The DIP advises us to avoid source code dependencies upon things that are both volatile and concrete. So we create abstract structures and try to route our dependencies upon them. However, when we create instances of objects, we often have to violate that advice; and this can cause architectural difficulties, as shown by the UML in [[[Figure 16.11]{.underline}]{.calibre_10}](#index_split_032.html#filepos667480).

![](images/00188.jpg){#filepos667480 .calibre_85}

[[Figure 16.11.]{.bold}]{.calibre3}[ DIP violation due to creation]{.calibre3}

The [` App `{.calibre4}]{.calibre_17} in [[[Figure 16.11]{.underline}]{.calibre_10}](#index_split_032.html#filepos667480) uses the [` Shape `{.calibre4}]{.calibre_17} interface. Everything it needs to do can be done through that interface, with one exception. The [` App `{.calibre4}]{.calibre_17} must create instances of the [` Circle `{.calibre4}]{.calibre_17} and [` Square `{.calibre4}]{.calibre_17} derivatives; and that forces the [` App `{.calibre4}]{.calibre_17} to hang source code dependencies upon the corresponding modules.

We've actually seen this situation in our previous examples. Consider, for example, the code from the tests from the [` visitor-example `{.calibre4}]{.calibre_17} earlier in this chapter. Notice that the test requires source code dependencies upon [` square `{.calibre4}]{.calibre_17} and [` circle `{.calibre4}]{.calibre_17} for the sole purpose of calling those [` make `{.calibre4}]{.calibre_17} functions:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_271.html#filepos990501)

> > [[`(ns visitor-example.core-spec`{.calibre4}\
> > `  (:require [speclj.core :refer :all]`{.calibre4}\
> > `            [visitor-example`{.calibre4}\
> > `             [square :as square]`{.calibre4}\
> > `             [json-shape-visitor :as jv]`{.calibre4}\
> > `             [circle :as circle]]))`{.calibre4}\
> > \
> > `(describe "shape-visitor"`{.calibre4}\
> > `  (it "makes json square"`{.calibre4}\
> > `    (should= "{\"top-left\": [0,0], \"side\": 1}"`{.calibre4}\
> > `             (jv/to-json (square/make [0 0] 1))))`{.calibre4}\
> > \
> > `  (it "makes json circle"`{.calibre4}\
> > `    (should= "{\"center\": [3,4], \"radius\": 1}"`{.calibre4}\
> > `             (jv/to-json (circle/make [3 4] 1)))))`{.calibre4}]{.calibre_3}]{.calibre_17}

Perhaps this seems a small price to pay. But if, as shown in [[[Figure 16.12]{.underline}]{.calibre_10}](#index_split_032.html#filepos670197), we add an architectural boundary to that UML diagram, the true cost becomes clear.

![](images/00225.jpg){#filepos670197 .calibre_86}

[[Figure 16.12.]{.bold}]{.calibre3}[ Violation of the Dependency Rule across the architectural boundary]{.calibre3}

Here we can see that the [Dependency Rule]{.italic} of [Clean Architecture]{.italic}[]{#index_split_032.html#filepos670563}[[[[16]{.underline}]{.calibre_10}]{.calibre3}](#index_split_032.html#filepos671263) has been violated by that [` <creates> `{.calibre4}]{.calibre_17} dependency. That rule states that all source code dependencies that cross an architectural boundary must point toward the higher-level side of that boundary. The [` Circle `{.calibre4}]{.calibre_17} and [` Square `{.calibre4}]{.calibre_17} modules are low-level details that are plug-ins to the [` App `{.calibre4}]{.calibre_17}. Thus, to preserve the architecture, we need to somehow deal with those [` <creates> `{.calibre4}]{.calibre_17} dependencies.

[[[16]{.underline}]{.calibre_10}](#index_split_032.html#filepos670563). Robert C. Martin, [Clean Architecture]{.italic} (Pearson, 2017).

The [Abstract Factory]{.italic} pattern provides a good solution. It looks like [[[Figure 16.13]{.underline}]{.calibre_10}](#index_split_032.html#filepos671675).

![](images/00278.jpg){#filepos671675 .calibre_87}

[[Figure 16.13.]{.bold}]{.calibre3}[ Abstract Factory pattern resolves Dependency Rule]{.calibre3}

All the source code dependencies that cross the boundary now point toward the higher-level side, so the Dependency Rule violation has been resolved. The [` Circle `{.calibre4}]{.calibre_17} and [` Square `{.calibre4}]{.calibre_17} can still be independent plug-ins to the [` App `{.calibre4}]{.calibre_17}. The [` App `{.calibre4}]{.calibre_17} can still create [` Circle `{.calibre4}]{.calibre_17} and [` Square `{.calibre4}]{.calibre_17} instances but indirectly through the [` ShapeFactory `{.calibre4}]{.calibre_17} interface, which inverts the source code dependency (the DIP).

This is easy to implement in Clojure. All we need is the [` shape-factory `{.calibre4}]{.calibre_17} interface and its implementation:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_272.html#filepos990647)

> > [[`(ns abstract-factory-example.shape-factory)`{.calibre4}\
> > \
> > `(defmulti make-circle`{.calibre4}\
> > `  (fn [factory center radius] (::type factory)))`{.calibre4}\
> > \
> > `(defmulti make-square`{.calibre4}\
> > `  (fn [factory top-left side] (::type factory)))`{.calibre4}\
> > \
> > `—————`{.calibre4}\
> > \
> > `(ns abstract-factory-example.shape-factory-implementation`{.calibre4}\
> > `  (:require [abstract-factory-example`{.calibre4}\
> > `             [shape-factory :as factory]`{.calibre4}\
> > `             [square :as square]`{.calibre4}\
> > `             [circle :as circle]]))`{.calibre4}\
> > \
> > `(defn make []`{.calibre4}\
> > `  {::factory/type ::implementation})`{.calibre4}\
> > \
> > `(defmethod factory/make-square ::implementation`{.calibre4}\
> > `  [factory top-left side]`{.calibre4}\
> > `  (square/make top-left side))`{.calibre4}\
> > \
> > `(defmethod factory/make-circle ::implementation`{.calibre4}\
> > `  [factory center radius]`{.calibre4}\
> > `  (circle/make center radius))`{.calibre4}]{.calibre_3}]{.calibre_17}

And with that, we can write a test that simulates our [` App `{.calibre4}]{.calibre_17}:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_273.html#filepos990793)

> > [[`(ns abstract-factory-example.core-spec`{.calibre4}\
> > `  (:require [speclj.core :refer :all]`{.calibre4}\
> > `            [abstract-factory-example`{.calibre4}\
> > `             [shape :as shape]`{.calibre4}\
> > `             [shape-factory :as factory]`{.calibre4}\
> > `             [main :as main]]))`{.calibre4}\
> > \
> > `(describe "Shape Factory"`{.calibre4}\
> > `  (before-all (main/init))`{.calibre4}\
> > `  (it "creates a square"`{.calibre4}\
> > `    (let [square (factory/make-square`{.calibre4}\
> > `                   @main/shape-factory`{.calibre4}\
> > `                   [100 100] 10)]`{.calibre4}\
> > `      (should= "Square top-left: [100,100] side: 10"`{.calibre4}\
> > `               (shape/to-string square))))`{.calibre4}\
> > `  (it "creates a circle"`{.calibre4}\
> > `      (let [circle (factory/make-circle`{.calibre4}\
> > `                     @main/shape-factory`{.calibre4}\
> > `                     [100 100] 10)]`{.calibre4}\
> > `        (should= "Circle center: [100,100] radius: 10"`{.calibre4}\
> > `                 (shape/to-string circle)))))`{.calibre4}]{.calibre_3}]{.calibre_17}

The first thing to notice about this test is that it has no source file dependencies on [` circle `{.calibre4}]{.calibre_17} or [` square `{.calibre4}]{.calibre_17}. It depends only on the two interfaces: [` shape `{.calibre4}]{.calibre_17} and [` shape-factory `{.calibre4}]{.calibre_17}. That was our architectural goal.

But what is that [` main `{.calibre4}]{.calibre_17} dependency? Do you see the [` (before-all (main/init)) `{.calibre4}]{.calibre_17} line at the start of the test? That tells the test runner to call [` (main/init) `{.calibre4}]{.calibre_17} before any of the tests. This simulates the [` main `{.calibre4}]{.calibre_17} module initializing everything before starting the [` App `{.calibre4}]{.calibre_17}.

Here's [` main `{.calibre4}]{.calibre_17}:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_274.html#filepos990939)

> > [[`(ns abstract-factory-example.main`{.calibre4}\
> > `  (:require [abstract-factory-example`{.calibre4}\
> > `            [shape-factory-implementation :as imp]]))`{.calibre4}\
> > \
> > `(def shape-factory (atom nil))`{.calibre4}\
> > \
> > `(defn init[]`{.calibre4}\
> > `  (reset! shape-factory (imp/make)))`{.calibre4}]{.calibre_3}]{.calibre_17}

Oh, HO! We've got a global [` atom `{.calibre4}]{.calibre_17} named [` shape-factory `{.calibre4}]{.calibre_17}! And that [` atom `{.calibre4}]{.calibre_17} is being initialized to the [` shape-factory-implementation `{.calibre4}]{.calibre_17} by the [` init `{.calibre4}]{.calibre_17} function.

So, looking back at the test, we see that the [` make-circle `{.calibre4}]{.calibre_17} and [` make-square `{.calibre4}]{.calibre_17} methods were passing the dereferenced [` atom `{.calibre4}]{.calibre_17}.

Setting a global like this is a pretty common strategy for dealing with factories. The main program creates the concrete factory implementations and then loads it into a global that everyone can access. In a statically typed []{#index_split_032.html#filepos678316}language, that global would have the type of the interface [` ShapeFactory `{.calibre4}]{.calibre_17}. In dynamically typed languages, no such type declaration is required.

[[90 Degrees Again]{.calibre_3}]{.bold}

Look at that UML diagram in [[[Figure 16.13]{.underline}]{.calibre_10}](#index_split_032.html#filepos671675) again. Do you see the 90-degree rotation in the [` ShapeFactory `{.calibre4}]{.calibre_17}? You can see it in the [` shape-factory `{.calibre4}]{.calibre_17} code too. The [` ShapeFactory `{.calibre4}]{.calibre_17} (and the [` shape-factory `{.calibre4}]{.calibre_17}) have methods that correspond to the subtypes of [` Shape `{.calibre4}]{.calibre_17}.

The problem that this caused for Visitor is also present here, although in a slightly different form. Whenever a new subtype of [` shape `{.calibre4}]{.calibre_17} is added, the [` shape-factory `{.calibre4}]{.calibre_17} must be modified. That violates the OCP because we must modify a module on the high-level side of the architectural boundary. If the OCP matters at all, it matters most especially across such boundaries. Study that UML diagram until you see what I mean.

We can resolve this problem by replacing the 90-degree rotation with a single method that takes an opaque token. Something like this:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_275.html#filepos991085)

> > [[`(ns abstract-factory-example.shape-factory)`{.calibre4}\
> > \
> > `(defmulti `{.calibre4}]{.calibre_3}]{.calibre_17}[[`make`{.calibre4}]{.calibre_3}]{.bold}[[` (fn [factory `{.calibre4}]{.calibre_3}]{.calibre_17}[[`type & args`{.calibre4}]{.calibre_3}]{.bold}[[`] (::type factory)))`{.calibre4}\
> > \
> > `——————————`{.calibre4}\
> > \
> > `(ns abstract-factory-example.shape-factory-implementation`{.calibre4}\
> > `  (:require [abstract-factory-example`{.calibre4}\
> > `             [shape-factory :as factory]`{.calibre4}\
> > `             [square :as square]`{.calibre4}\
> > `             [circle :as circle]]))`{.calibre4}\
> > \
> > `(defn make []`{.calibre4}\
> > `  {::factory/type ::implementation})`{.calibre4}\
> > \
> > `(defmethod factory/`{.calibre4}]{.calibre_3}]{.calibre_17}[[`make`{.calibre4}]{.calibre_3}]{.bold}[[` ::implementation`{.calibre4}\
> > `  [factory type `{.calibre4}]{.calibre_3}]{.calibre_17}[[`& args`{.calibre4}]{.calibre_3}]{.bold}[[`]`{.calibre4}\
> > `  `{.calibre4}]{.calibre_3}]{.calibre_17}[[`(condp = type`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `    `{.calibre4}]{.calibre_3}]{.calibre_17}[[`:square (apply square/make args)`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `    `{.calibre4}]{.calibre_3}]{.calibre_17}[[`:circle (apply circle/make args))`{.calibre4}]{.calibre_3}]{.bold}[[`)`{.calibre4}\
> > \
> > `————————————————`{.calibre4}\
> > \
> > `(ns abstract-factory-example.core-spec`{.calibre4}\
> > `  (:require [speclj.core :refer :all]`{.calibre4}\
> > `            [abstract-factory-example`{.calibre4}\
> > `             [shape :as shape]`{.calibre4}\
> > `             [shape-factory :as factory]`{.calibre4}\
> > `             [main :as main]]))`{.calibre4}\
> > \
> > `(describe "Shape Factory"`{.calibre4}\
> > `  (before-all (main/init))`{.calibre4}\
> > `  (it "creates a square"`{.calibre4}\
> > `    (let [square (factory/make`{.calibre4}\
> > `                   @main/shape-factory`{.calibre4}\
> > `                   `{.calibre4}]{.calibre_3}]{.calibre_17}[[`:square`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `                   [100 100] 10)]`{.calibre4}\
> > `      (should= "Square top-left: [100,100] side: 10"`{.calibre4}\
> > `               (shape/to-string square))))`{.calibre4}\
> > \
> > `  (it "creates a circle"`{.calibre4}\
> > `      (let [circle (factory/make`{.calibre4}\
> > `                     @main/shape-factory`{.calibre4}\
> > `                     `{.calibre4}]{.calibre_3}]{.calibre_17}[[`:circle`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `                     [100 100] 10)]`{.calibre4}\
> > `        (should= "Circle center: [100,100] radius: 10"`{.calibre4}\
> > `                 (shape/to-string circle)))))`{.calibre4}]{.calibre_3}]{.calibre_17}

Notice that the argument passed into [` shape-factory/make `{.calibre4}]{.calibre_17} is opaque. That is, it is not defined by any of the other modules, including---and especially---the [` square `{.calibre4}]{.calibre_17} and [` circle `{.calibre4}]{.calibre_17} modules. The [` :square `{.calibre4}]{.calibre_17} and [` :circle `{.calibre4}]{.calibre_17} keywords are not namespaced, nor are they declared anywhere. They are simply opaque values that happen to have names. I might as well have used [` 1 `{.calibre4}]{.calibre_17} for [` square `{.calibre4}]{.calibre_17} and [` 2 `{.calibre4}]{.calibre_17} for [` circle `{.calibre4}]{.calibre_17}, or used [` "square" `{.calibre4}]{.calibre_17} and [` "circle" `{.calibre4}]{.calibre_17} strings.

This opacity is the key to this solution. If we ever need to add a [` triangle `{.calibre4}]{.calibre_17} subtype, nothing above the boundary line will have to change (the OCP).

[[Type Safety?]{.calibre_3}]{.bold}

In a statically typed language, like Java, this technique abandons type safety. Opaque values cannot be type safe. There is no way, for example, to use an [` enum `{.calibre4}]{.calibre_17} in Java to solve this issue.

In Clojure, we aren't concerned about static type safety, but what about dynamic type specifications? We're out of luck there too. There is no way to gain an advantage by using [` clojure.spec `{.calibre4}]{.calibre_17} since all errors, either with or without [` clojure.spec `{.calibre4}]{.calibre_17}, will be runtime errors.

For example, nothing stops me from calling [` shape-factory/make `{.calibre4}]{.calibre_17} with [` :sqare `{.calibre4}]{.calibre_17} (intentionally misspelled). The [` condp `{.calibre4}]{.calibre_17} in [` shape-factory-implementation `{.calibre4}]{.calibre_17} will simply throw an exception. If I were to set up some type constraint in [` clojure.spec `{.calibre4}]{.calibre_17} forcing the [` type `{.calibre4}]{.calibre_17} argument of [` shape-factory/make `{.calibre4}]{.calibre_17} to be either [` :square `{.calibre4}]{.calibre_17} or [` :circle `{.calibre4}]{.calibre_17}, it would still just throw a runtime exception.

There is no escape from this in any language. Whether in Java, C++, Ruby, Clojure, or C#, if you want to maintain the OCP across architectural boundaries (and you usually do), then at some point across that boundary you are going to have to abandon type safety and rely on runtime exceptions. This is just simply software physics.

[[[Conclusion]{.calibre_3}]{.bold}]{.calibre1}

I'll leave the rest of the GOF patterns, and any other patterns you might be familiar with, as an exercise. By now, I'm pretty sure you understand that functional languages that have facilities similar to Clojure are as OO as Java, C#, Ruby, and Python, and that the patterns described in the GOF book generally apply so long as the constraint of immutability is enforced.

And as for [Singleton]{.italic}: Just create one.

[[[Postscript: OO Poison?]{.calibre_3}]{.bold}]{.calibre1}

![](images/00025.jpg){.calibre_88}

I thought it wise to revisit here my hope and goal from the introduction. By now, it should be clear that functional programming and OOP are compatible and mutually beneficial styles.

The design pattern examples that I have presented so far are not unusual. Clojure programmers frequently use [` defmulti `{.calibre4}]{.calibre_17} and [` defmethod `{.calibre4}]{.calibre_17} to express polymorphism. They typically use maps to express encapsulated data structures (i.e., objects). They often even build constructors for those objects. They might not realize it, but they are building OO programs.

What might seem unusual to some functional programmers, and even to some Clojure programmers, is the way I have organized the source files and namespaces. That organization is so reminiscent of Java, C++, C#, Ruby, and even Python that it screams "OO" to folks who'd thought that they'd left OO behind many long years ago.

It should be very clear by now that Clojure is every bit as object oriented as Java, C++, C#, Python, and Ruby. Clojure is also as functional as F#, Scala, Elixir, and (dare I say it?) Haskell.

Let's examine the OO claim just a bit.

Clojure does not have inheritance; but it does have at least three very effective mechanisms of polymorphism. At least two of those mechanisms support open classes.

Clojure does not have [` public `{.calibre4}]{.calibre_17}/[` private `{.calibre4}]{.calibre_17}/[` protected `{.calibre4}]{.calibre_17} modifiers; but it does have namespaced keywords and dynamic type specification, which allows encapsulation to be strongly expressed and dynamically, if not statically, enforced. Clojure also has private functions (created with [` defn- `{.calibre4}]{.calibre_17}) that can only be seen within the containing source file.

Clojure supports, but does not enforce, a source file and namespace structure that affords the same architectural partitioning we find so familiar in any of the (so-called) enterprise languages.

And so Clojure is an OO/functional[]{#index_split_032.html#filepos689890}[[[[17]{.underline}]{.calibre_10}]{.calibre3}](#index_split_032.html#filepos690205) language. As are, to one extent or another, languages like Scala, Elixir, and F#, to name just a few. And, since that is true, the OO mindset is still a perfectly valid way of modeling applications in those languages.

[[[17]{.underline}]{.calibre_10}](#index_split_032.html#filepos689890). OOFL? FOOL? Hmm, perhaps we should avoid the acronyms.

We can still describe our functional programs using interfaces and classes, types and subtypes. We can still partition the source files and manage their dependencies in order to create robust, independently deployable and independently developable architectures. Nothing in that regard has changed at all.

What [has]{.italic} changed is the extra constraint that functional programming places upon us, which is the elimination, or at least the strong sequestration, []{#index_split_032.html#filepos690920}of side effects. Our classes and modules will strongly prefer immutable, as opposed to mutable, objects. But they are still objects, and they can still be expressed and organized as classes that implement interfaces.

And that means that the vast majority of the design principles and design patterns that we found so helpful in OO languages still apply, and are still useful, in functional languages like Clojure and others.

::: {#index_split_032.html#calibre_pb_32 .mbp_pagebreak}
:::

[]{#index_split_033.html}

[[VI]{.calibre_3}]{.calibre2}

[[Case Study]{.calibre_3}]{.calibre2}

::: {#index_split_033.html#calibre_pb_33 .mbp_pagebreak}
:::

[]{#index_split_034.html}

[[[17]{.calibre_3}]{.bold}]{.calibre1}

[[[Wa-Tor]{.calibre_3}]{.bold}]{.calibre1}

![](images/00289.jpg){.calibre_89}

In the final chapter of this book, you and I are going to play a little game about a little game. The little game our little game will be about is called [Wa-Tor]{.italic}; a simple little cellular automaton described by A. K. Dewdney in the December 1984 issue of [Scientific American]{.italic}.[]{#index_split_034.html#filepos692303}[[[[1]{.underline}]{.calibre_10}]{.calibre3}](#index_split_034.html#filepos692561) The game you and I are going to play is to [pretend]{.italic} that Wa-Tor is an enterprise-level application requiring significant effort in architecture and design.

[[[1]{.underline}]{.calibre_10}](#index_split_034.html#filepos692303). Alas, [SciAm]{.italic}, I knew it well. . .

I mean, honestly, I could hack together Wa-Tor in a few hours and walk away happy. But for this chapter, I want us to really think about the issues as though this were a 50 mega line of code (LOC) monster.

So what is Wa-Tor?[]{#index_split_034.html#filepos693020}[[[[2]{.underline}]{.calibre_10}]{.calibre3}](#index_split_034.html#filepos693612) The Wikipedia article referenced in the footnote should give you all the information you need to understand it in the required depth (which is not much). But essentially, Wa-Tor is a typical predator/prey simulation using fish and sharks. The fish move around randomly and occasionally reproduce. The sharks also move around randomly but will eat a fish if one is adjacent. Sharks will occasionally reproduce if they eat enough fish. Sharks will die if they do not eat a fish before they starve.

[[[2]{.underline}]{.calibre_10}](#index_split_034.html#filepos693020). [[[https://en.wikipedia.org/wiki/Wa-Tor]{.underline}]{.calibre_10}](https://en.wikipedia.org/wiki/Wa-Tor)

The world that the fish and sharks live in has no land; it's all water. Moreover, the top meets the bottom and the left meets the right, so the world is topologically a torus. Thus, Wa-Tor stands for WAter TORus.

We'll talk more about the features of the program later. For the moment, what are the architectural and design considerations?

Let's start with the basics. SRP. Who are the actors---whom do we want to keep separate?

In most large enterprise systems, there are many different actors. But in this little app, there are only two to worry about. There are the user experience (UX) designers, who will undoubtedly change their minds a dozen or so []{#index_split_034.html#filepos694682}times before they actually like what they see on the screen. And then there are the modelers who will also likely fiddle with the internal shark/fish behavior and might possibly add more animals to the mix.

So we start out with [[[Figure 17.1]{.underline}]{.calibre_10}](#index_split_034.html#filepos695133), a very obvious and very traditional partitioning.

![](images/00318.jpg){#filepos695133 .calibre_90}

[[Figure 17.1.]{.bold}]{.calibre3}[ The obvious and traditional partitioning of Wa-Tor]{.calibre3}

The [` WatorUI `{.calibre4}]{.calibre_17} component is lower level[]{#index_split_034.html#filepos695485}[[[[3]{.underline}]{.calibre_10}]{.calibre3}](#index_split_034.html#filepos696003) than the [` WatorModel `{.calibre4}]{.calibre_17} component. According to the Dependency Rule, this means that the source code dependencies must cross the architectural boundary pointing toward the [` WatorModel `{.calibre4}]{.calibre_17}. Because of this, the [` WatorUI `{.calibre4}]{.calibre_17} will be a plug-in to the [` WatorModel `{.calibre4}]{.calibre_17}.

[[[3]{.underline}]{.calibre_10}](#index_split_034.html#filepos695485). The definition of high and low "level" that I'm using here is "distance from I/O." See Robert C. Martin, [Clean Architecture]{.italic} (Pearson, 2017), p. 183.

There are only two components[]{#index_split_034.html#filepos696348}[[[[4]{.underline}]{.calibre_10}]{.calibre3}](#index_split_034.html#filepos696581) and one boundary in this partitioning so far. In larger systems, we would see many more boundaries and many more components within each.

[[[4]{.underline}]{.calibre_10}](#index_split_034.html#filepos696348). See Martin, [Clean Architecture]{.italic}, p. 93.

Let's focus on the model first.[]{#index_split_034.html#filepos696810}[[[[5]{.underline}]{.calibre_10}]{.calibre3}](#index_split_034.html#filepos696950) What kinds of classes are we going to need?

[[[5]{.underline}]{.calibre_10}](#index_split_034.html#filepos696810). [[[http://wiki.c2.com/?ModelFirst]{.underline}]{.calibre_10}](http://wiki.c2.com/?ModelFirst)

Yes, I said classes. We may be using a functional language, but if you've learned anything in this book so far, it is that functional design and OO design are two sides of the same coin.

So, at first blush, I think the object model looks something like [[[Figure 17.2]{.underline}]{.calibre_10}](#index_split_034.html#filepos697633).

![](images/00004.jpg){#filepos697633 .calibre_91}

[[Figure 17.2.]{.bold}]{.calibre3}[ Initial object model of Wa-Tor]{.calibre3}

The [` world `{.calibre4}]{.calibre_17} contains a bunch of [` cell `{.calibre4}]{.calibre_17}s. Each [` cell `{.calibre4}]{.calibre_17} can process a [` tick `{.calibre4}]{.calibre_17}[]{#index_split_034.html#filepos698127}[[[[6]{.underline}]{.calibre_10}]{.calibre3}](#index_split_034.html#filepos698403) of time. I guessed that [` cell `{.calibre4}]{.calibre_17} is abstract rather than an interface because I expect that there will be concrete functions at this level.

[[[6]{.underline}]{.calibre_10}](#index_split_034.html#filepos698127). Dewdney called these [chronons]{.italic}.

Each [` cell `{.calibre4}]{.calibre_17} can be [` water `{.calibre4}]{.calibre_17}, or an [` animal `{.calibre4}]{.calibre_17} that can [` move `{.calibre4}]{.calibre_17} and [` reproduce `{.calibre4}]{.calibre_17}. The two possible subtypes of [` animal `{.calibre4}]{.calibre_17} are [` fish `{.calibre4}]{.calibre_17} and [` sharks `{.calibre4}]{.calibre_17} that can [` eat `{.calibre4}]{.calibre_17}.

Let's see if we can code this. No tests yet, because we haven't defined any behavior:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_277.html#filepos991362)

> > [[`(ns wator.cell)`{.calibre4}\
> > \
> > `(defmulti tick ::type)`{.calibre4}\
> > \
> > `——————`{.calibre4}\
> > \
> > `(ns wator.water`{.calibre4}\
> > `  (:require [wator`{.calibre4}\
> > `             [cell :as cell]]))`{.calibre4}\
> > \
> > `(defn make [] {::cell/type ::water})`{.calibre4}\
> > \
> > `(defmethod cell/tick ::water [water]`{.calibre4}\
> > `  )`{.calibre4}\
> > \
> > `———————`{.calibre4}\
> > \
> > `(ns wator.animal)`{.calibre4}\
> > \
> > `(defmulti move ::type)`{.calibre4}\
> > `(defmulti reproduce ::type)`{.calibre4}\
> > \
> > `(defn tick [animal]`{.calibre4}\
> > `  )`{.calibre4}\
> > \
> > `—————`{.calibre4}\
> > \
> > `(ns wator.fish`{.calibre4}\
> > `  (:require [wator`{.calibre4}\
> > `             [cell :as cell]`{.calibre4}\
> > `             [animal :as animal]]))`{.calibre4}\
> > \
> > `(defn make [] {::cell/type ::fish})`{.calibre4}\
> > \
> > `(defmethod cell/tick ::fish [fish]`{.calibre4}\
> > `  (animal/tick fish)`{.calibre4}\
> > `  )`{.calibre4}\
> > \
> > `(defmethod animal/move ::fish [fish]`{.calibre4}\
> > `  )`{.calibre4}\
> > \
> > `(defmethod animal/reproduce ::fish [fish]`{.calibre4}\
> > `  )`{.calibre4}\
> > \
> > `—————`{.calibre4}\
> > \
> > `(ns wator.shark`{.calibre4}\
> > `  (:require [wator`{.calibre4}\
> > `             [cell :as cell]`{.calibre4}\
> > `             [animal :as animal]]))`{.calibre4}\
> > \
> > `(defmethod cell/tick ::shark [shark]`{.calibre4}\
> > `  (animal/tick shark)`{.calibre4}\
> > `  )`{.calibre4}\
> > \
> > `(defmethod animal/move ::shark [shark]`{.calibre4}\
> > `  )`{.calibre4}\
> > \
> > `(defmethod animal/reproduce ::shark [shark]`{.calibre4}\
> > `  )`{.calibre4}\
> > \
> > `(defn eat [shark]`{.calibre4}\
> > `  )`{.calibre4}]{.calibre_3}]{.calibre_17}
>
> []{#index_split_034.html#filepos701127}

This looks pretty standard. The [` cell `{.calibre4}]{.calibre_17} module looks like an interface so far. The [` water `{.calibre4}]{.calibre_17} module implements it trivially. The dangling parentheses are there to remind me that I want to add something to that function.

The [` animal `{.calibre4}]{.calibre_17} module [does not]{.italic} implement [` tick `{.calibre4}]{.calibre_17}, but it does have a function named [` tick `{.calibre4}]{.calibre_17} that can be called by its subtypes. I put this in as a guess. It's a bit of hubris, I suppose; but I have a feeling that it'll be necessary.[]{#index_split_034.html#filepos701899}[[[[7]{.underline}]{.calibre_10}]{.calibre3}](#index_split_034.html#filepos701995)

[[[7]{.underline}]{.calibre_10}](#index_split_034.html#filepos701899). Yeah, I know. You Aren't Gonna Need It (YAGNI). Well, we'll see.

The [` fish `{.calibre4}]{.calibre_17} trivially implements both the [` cell `{.calibre4}]{.calibre_17} and [` animal `{.calibre4}]{.calibre_17}. This actually looks more like multiple inheritance than the UML diagram. On the other hand, there's no inheritance anywhere in this code, so. . .

Finally, [` shark `{.calibre4}]{.calibre_17} also trivially implements both [` cell `{.calibre4}]{.calibre_17} and [` animal `{.calibre4}]{.calibre_17} and adds its own [` eat `{.calibre4}]{.calibre_17} function.

I didn't code the [` world `{.calibre4}]{.calibre_17} because I don't know enough to even start. However, there are a few issues that I think the [` world `{.calibre4}]{.calibre_17} will have to deal with. We don't want the [` world `{.calibre4}]{.calibre_17} to depend upon the GUI, and yet the GUI is going to put a lot of constraints on the [` world `{.calibre4}]{.calibre_17}. For example, it seems to me that the GUI is going to tell us the size of the [` world `{.calibre4}]{.calibre_17}. I also think that since the GUI is likely to repaint the screen [N]{.italic} times per second, the GUI will define [time]{.italic}.

But let's set all that aside for the time being. Enough of this up-front design. Let's see if we can code some of the behavior.

What is the behavior of [` water `{.calibre4}]{.calibre_17}? We ask our modelers, and they tell us that a [` water `{.calibre4}]{.calibre_17} cell will randomly evolve into a [` fish `{.calibre4}]{.calibre_17} cell if given enough time. Here's my implementation of that rule:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_280.html#filepos991800)

> > [[`(ns wator.core-spec`{.calibre4}\
> > `  (:require [speclj.core :refer :all]`{.calibre4}\
> > `            [wator`{.calibre4}\
> > `             [cell :as cell]`{.calibre4}\
> > `             [water :as water]`{.calibre4}\
> > `             [fish :as fish]]))`{.calibre4}\
> > \
> > `(describe "Wator"`{.calibre4}\
> > `  (with-stubs)`{.calibre4}\
> > `  (context "Water"`{.calibre4}\
> > `    (it "usually remains water"`{.calibre4}\
> > `          (with-redefs [rand (stub :rand {:return 0.0})]`{.calibre4}\
> > `            (let [water (water/make)`{.calibre4}\
> > `                  evolved (cell/tick water)]`{.calibre4}\
> > `              (should= ::water/water (::cell/type evolved)))))`{.calibre4}\
> > \
> > \
> > `    (it "occasionally evolves into a fish"`{.calibre4}\
> > `      (with-redefs [rand (stub :rand {:return 1.0})]`{.calibre4}\
> > `        (let [water (water/make)`{.calibre4}\
> > `              evolved (cell/tick water)]`{.calibre4}\
> > `          (should= ::fish/fish (::cell/type evolved)))))))`{.calibre4}\
> > \
> > `———`{.calibre4}\
> > \
> > `(ns wator.water`{.calibre4}\
> > `  (:require [wator`{.calibre4}\
> > `             [cell :as cell]`{.calibre4}\
> > `             [fish :as fish]`{.calibre4}\
> > `             [config :as config]]))`{.calibre4}\
> > \
> > `(defn make [] {::cell/type ::water})`{.calibre4}\
> > \
> > `(defmethod cell/tick ::water [water]`{.calibre4}\
> > `  `{.calibre4}]{.calibre_3}]{.calibre_17}[[`(if (> (rand) config/water-evolution-rate)`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `    `{.calibre4}]{.calibre_3}]{.calibre_17}[[`(fish/make)`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `    `{.calibre4}]{.calibre_3}]{.calibre_17}[[`water))`{.calibre4}]{.calibre_3}]{.bold}[[\
> > \
> > `——————`{.calibre4}\
> > \
> > `(ns wator.config)`{.calibre4}\
> > \
> > `(def water-evolution-rate 0.99999)`{.calibre4}]{.calibre_3}]{.calibre_17}

So, right away we see the "functional" nature of this program.[]{#index_split_034.html#filepos706571}[[[[8]{.underline}]{.calibre_10}]{.calibre3}](#index_split_034.html#filepos707067) The return value of [` tick `{.calibre4}]{.calibre_17} is a new [` cell `{.calibre4}]{.calibre_17}. I don't know if that [` water-evolution-rate `{.calibre4}]{.calibre_17} is correct. The modelers haven't told us what the rate should be. So I just guessed. I expect that they'll wait until they see how the model behaves and then tell us to change it.

[[[8]{.underline}]{.calibre_10}](#index_split_034.html#filepos706571). Almost. The [` (rand) `{.calibre4}]{.calibre_17} invocation is impure.

So far, I haven't specified any dynamic types. It seems a bit early for that. But I'm pretty sure it's coming.

Anyway, let's see if we can make a [` fish `{.calibre4}]{.calibre_17} move.

Wait. How do you move a [` fish `{.calibre4}]{.calibre_17}? Where is the [` fish `{.calibre4}]{.calibre_17}? Does the [` fish `{.calibre4}]{.calibre_17} know its location, or is that something the [` world `{.calibre4}]{.calibre_17} knows?

The [` cell `{.calibre4}]{.calibre_17}s are arranged in a two-dimensional rectangular Cartesian grid that wraps left to right and top to bottom. So the location of a [` cell `{.calibre4}]{.calibre_17} is the tuple [` [x y] `{.calibre4}]{.calibre_17}. The [` world `{.calibre4}]{.calibre_17} could hold the [` cell `{.calibre4}]{.calibre_17}s in a two-dimensioned array, or in a map keyed by the position tuple.

I like using maps for things like this, so let's make a [` world `{.calibre4}]{.calibre_17} full of [` water `{.calibre4}]{.calibre_17} cells:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_281.html#filepos991946)

> > [[`(context "world"`{.calibre4}\
> > `  (it "creates a world full of water cells"`{.calibre4}\
> > `    (let [world (world/make 2 2)`{.calibre4}\
> > `          cells (:cells world)`{.calibre4}\
> > `          positions (set (keys cells))]`{.calibre4}\
> > `      (should= #{[0 0] [0 1]`{.calibre4}\
> > `                 [1 0] [1 1]} positions)`{.calibre4}\
> > `      (should (every? #(= ::water/water (::cell/type %))`{.calibre4}\
> > `                      (vals cells))))))`{.calibre4}\
> > \
> > `————`{.calibre4}\
> > \
> > `(ns wator.world`{.calibre4}\
> > `  (:require [wator`{.calibre4}\
> > `             [water :as water]]))`{.calibre4}\
> > \
> > `(defn make [w h]`{.calibre4}\
> > `  (let [locs (for [x (range w) y (range h)] [x y])`{.calibre4}\
> > `        loc-water (interleave locs (repeat (water/make)))`{.calibre4}\
> > `        cells (apply hash-map loc-water)]`{.calibre4}\
> > `    {:cells cells}))`{.calibre4}]{.calibre_3}]{.calibre_17}
>
> []{#index_split_034.html#filepos709869}

Did you catch the use of the lazy list of [` water `{.calibre4}]{.calibre_17} cells passed into [` interleave `{.calibre4}]{.calibre_17}? Now we should be able to put a [` fish `{.calibre4}]{.calibre_17} in the world and move it around. Here's my first try at a test:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_282.html#filepos992092)

> > [[`(context "animal"`{.calibre4}\
> > `  (it "moves"`{.calibre4}\
> > `    (let [fish (fish/make)`{.calibre4}\
> > `          world (-> (world/make 3 3)`{.calibre4}\
> > `                    (world/set-cell [1 1] fish))`{.calibre4}\
> > `          [loc cell] (animal/move fish [1 1] world)]`{.calibre4}\
> > `      (should= cell fish)`{.calibre4}\
> > `      (should (#{[0 0] [0 1] [0 2]`{.calibre4}\
> > `                 [1 0] [1 2]`{.calibre4}\
> > `                 [2 0] [2 1] [2 2]}`{.calibre4}\
> > `               loc)))))`{.calibre4}]{.calibre_3}]{.calibre_17}

This is pretty straightforward. We create a 3-by-3 [` world `{.calibre4}]{.calibre_17} with a [` fish `{.calibre4}]{.calibre_17} in the center. Then we move the [` fish `{.calibre4}]{.calibre_17}. Finally, we make sure it's still a [` fish `{.calibre4}]{.calibre_17} and that its destination is one of the neighboring cells.

I made a ton of design decisions while composing this test. Those kinds of decisions are why the last [D]{.italic} in [TDD]{.italic} often stands for [design]{.italic}. I'll walk you through those decisions in a moment, but first let me show you the code that passes this test:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_283.html#filepos992238)

> > [[`(ns wator.world`{.calibre4}\
> > `  (:require [wator`{.calibre4}\
> > `             [water :as water]]))`{.calibre4}\
> > \
> > `(defn make [w h] . . .)`{.calibre4}\
> > \
> > ]{.calibre_3}]{.calibre_17}[[`(defn set-cell [world loc cell]`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `  `{.calibre4}]{.calibre_3}]{.calibre_17}[[`(assoc-in world [:cells loc] cell))`{.calibre4}]{.calibre_3}]{.bold}[[\
> > \
> > ]{.calibre_3}]{.calibre_17}[[`——————`{.calibre4}]{.calibre_3}]{.bold}[[\
> > \
> > `(ns wator.animal`{.calibre4}\
> > `  (:require [wator`{.calibre4}\
> > `             `{.calibre4}]{.calibre_3}]{.calibre_17}[[`[cell :as cell]`{.calibre4}]{.calibre_3}]{.bold}[[`]))`{.calibre4}\
> > \
> > `(defmulti move `{.calibre4}]{.calibre_3}]{.calibre_17}[[`(fn [animal & args] (::cell/type animal))`{.calibre4}]{.calibre_3}]{.bold}[[`)`{.calibre4}\
> > `(defmulti reproduce `{.calibre4}]{.calibre_3}]{.calibre_17}[[`(fn [animal & args] (::cell/type animal))`{.calibre4}]{.calibre_3}]{.bold}[[`)`{.calibre4}\
> > \
> > `(defn tick [animal]`{.calibre4}\
> > `  )`{.calibre4}\
> > \
> > ]{.calibre_3}]{.calibre_17}[[`(defn do-move [animal loc world]`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `  `{.calibre4}]{.calibre_3}]{.calibre_17}[[`[[0 0] animal])`{.calibre4}]{.calibre_3}]{.bold}[[\
> > \
> > `——————`{.calibre4}\
> > \
> > `(ns wator.fish`{.calibre4}\
> > `  (:require [wator`{.calibre4}\
> > `             [cell :as cell]`{.calibre4}\
> > `             [animal :as animal]]))`{.calibre4}\
> > \
> > `(defn make [] {::cell/type ::fish})`{.calibre4}\
> > \
> > `(defmethod cell/tick ::fish [fish]`{.calibre4}\
> > `  (animal/tick fish)`{.calibre4}\
> > `  )`{.calibre4}\
> > \
> > ]{.calibre_3}]{.calibre_17}[[`(defmethod animal/move ::fish [fish loc world]`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `  `{.calibre4}]{.calibre_3}]{.calibre_17}[[`(animal/do-move fish loc world))`{.calibre4}]{.calibre_3}]{.bold}[[\
> > \
> > `(defmethod animal/reproduce ::fish [fish]`{.calibre4}\
> > `  )`{.calibre4}]{.calibre_3}]{.calibre_17}

When you see [` . . . `{.calibre4}]{.calibre_17} in a method body, it means that there has been no change to that method since the last time I presented it.

There's nothing really astonishing here. I changed the [` defmulti `{.calibre4}]{.calibre_17} definitions in [` animal `{.calibre4}]{.calibre_17} to accept multiple arguments, and I created a default [` do-move `{.calibre4}]{.calibre_17} method in [` animal `{.calibre4}]{.calibre_17} that the subtypes can call if they like.[]{#index_split_034.html#filepos715225}[[[[9]{.underline}]{.calibre_10}]{.calibre3}](#index_split_034.html#filepos715445) The implementation of [` do-move `{.calibre4}]{.calibre_17} is degenerate and is there only to test the test.

[[[9]{.underline}]{.calibre_10}](#index_split_034.html#filepos715225). This is kind of like implementing a method in a base class and allowing subclasses to either override it or not.

So, on to the design decisions that I made while composing this test. My first problem was that an [` animal `{.calibre4}]{.calibre_17} can't [` move `{.calibre4}]{.calibre_17} if it can't see the [` world `{.calibre4}]{.calibre_17}. So either every [` animal `{.calibre4}]{.calibre_17} should hold a reference to the [` world `{.calibre4}]{.calibre_17}, or the [` world `{.calibre4}]{.calibre_17} should be a global [` atom `{.calibre4}]{.calibre_17}, or the [` world `{.calibre4}]{.calibre_17} should be passed in as an argument to the [` move `{.calibre4}]{.calibre_17} function. I chose the latter because I feel a kind of mild disdain[]{#index_split_034.html#filepos716477}[[[[10]{.underline}]{.calibre_10}]{.calibre3}](#index_split_034.html#filepos716692) for abandoning the functional paradigm and falling back on [` atom `{.calibre4}]{.calibre_17}s and STM.

[[[10]{.underline}]{.calibre_10}](#index_split_034.html#filepos716477). Perhaps that disdain is misplaced, but this IS a book about functional design, so. . .

My next problem was that the [` animal `{.calibre4}]{.calibre_17} does not know its location. So I need to pass the location of the [` animal `{.calibre4}]{.calibre_17} into the [` move `{.calibre4}]{.calibre_17} function along with the [` world `{.calibre4}]{.calibre_17}.

Finally, and most importantly, I puzzled over what the [` move `{.calibre4}]{.calibre_17} function should return. At first, I thought it should return the updated [` world `{.calibre4}]{.calibre_17}. But this creates the following inconsistency problem.

Imagine the update process for the [` world `{.calibre4}]{.calibre_17}. It begins at location [` [0 0] `{.calibre4}]{.calibre_17} and walks through the [` world `{.calibre4}]{.calibre_17} updating each [` cell `{.calibre4}]{.calibre_17} in turn. Now imagine there is a [` fish `{.calibre4}]{.calibre_17} at [` [0 0] `{.calibre4}]{.calibre_17} and that the update moves it to [` [0 1] `{.calibre4}]{.calibre_17}. But [` [0 1] `{.calibre4}]{.calibre_17} is the [` cell `{.calibre4}]{.calibre_17} that the [` world `{.calibre4}]{.calibre_17} updates next. So that same fish moves [again]{.italic}. A [` fish `{.calibre4}]{.calibre_17} should not move twice in a single turn.

So the [` move `{.calibre4}]{.calibre_17} function cannot update the [` world `{.calibre4}]{.calibre_17}. Instead, the [` world `{.calibre4}]{.calibre_17} is going to have to build up a new world from the old world, one cell at a time. I imagine we could do it something like this:[]{#index_split_034.html#filepos718824}[[[[11]{.underline}]{.calibre_10}]{.calibre3}](#index_split_034.html#filepos718921)

[[[11]{.underline}]{.calibre_10}](#index_split_034.html#filepos718824). Remember that [` :cells `{.calibre4}]{.calibre_17} holds a map, so the [` update-cell `{.calibre4}]{.calibre_17} function will take [` [key val] `{.calibre4}]{.calibre_17} pairs and return [` [key val] `{.calibre4}]{.calibre_17} pairs.

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_284.html#filepos992384)

> > [[`(let [new-world-cells (apply hash-map`{.calibre4}\
> > `                             (map update-cell old-world-cells))]. . .)`{.calibre4}]{.calibre_3}]{.calibre_17}

So now let's actually implement the degenerate [` do-move `{.calibre4}]{.calibre_17} function. What is the process for moving an [` animal `{.calibre4}]{.calibre_17}? I think it's pretty simple. We just get the neighbors of the animal's location, determine which are valid destinations (i.e., are [` water `{.calibre4}]{.calibre_17}), and then randomly choose from that list. So [` do-move `{.calibre4}]{.calibre_17} should look like this:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_285.html#filepos992529)

> > [[`(defn do-move [animal loc world]`{.calibre4}\
> > `  (let [neighbors (world/neighbors world loc)`{.calibre4}\
> > \
> > `        destinations (filter`{.calibre4}\
> > `                       #(water/is?`{.calibre4}\
> > `                         (world/get-cell world %))`{.calibre4}\
> > `                       neighbors)`{.calibre4}\
> > `        new-location (rand-nth destinations)]`{.calibre4}\
> > `    [new-location animal]))`{.calibre4}]{.calibre_3}]{.calibre_17}

Very pretty. We ask the [` world `{.calibre4}]{.calibre_17} for the [` neighbors `{.calibre4}]{.calibre_17} of the location, filter out any that aren't [` water `{.calibre4}]{.calibre_17}, and then randomly choose one. Cool.

I thought it best to make sure that all the torus math was nicely sequestered within [` world `{.calibre4}]{.calibre_17}. I didn't want it leaking out into all the [` animal `{.calibre4}]{.calibre_17}s:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_286.html#filepos992675)

> > [[`(defn wrap [world [x y]]`{.calibre4}\
> > `  (let [[w h] (::bounds world)]`{.calibre4}\
> > `    [(mod x w) (mod y h)])`{.calibre4}\
> > `  )`{.calibre4}\
> > \
> > `(defn neighbors [world loc]`{.calibre4}\
> > `  (let [[x y] loc`{.calibre4}\
> > `        neighbors (for [dx (range -1 2) dy (range -1 2)]`{.calibre4}\
> > `                    (wrap world [(+ x dx) (+ y dy)]))]`{.calibre4}\
> > `    (remove #(= loc %) neighbors))`{.calibre4}]{.calibre_3}]{.calibre_17}

Are you ready for the stuff that's not pretty? The code above refused to compile, because (are you ready for this?) [` water `{.calibre4}]{.calibre_17} depends upon [` fish `{.calibre4}]{.calibre_17} (for the evolution), [` fish `{.calibre4}]{.calibre_17} depends upon [` animal `{.calibre4}]{.calibre_17} (for [` do-move `{.calibre4}]{.calibre_17}), and [` animal `{.calibre4}]{.calibre_17} depends upon [` water `{.calibre4}]{.calibre_17}. That's a dependency cycle, and Clojure [hates]{.italic} dependency cycles. See [[[Figure 17.3]{.underline}]{.calibre_10}](#index_split_034.html#filepos723210).

![](images/00047.jpg){#filepos723210 .calibre_92}

[[Figure 17.3.]{.bold}]{.calibre3}[ A dependency cycle]{.calibre3}

OK, take a deep breath. Remember, we're playing a game here. In a simple application like Wa-Tor, I would not be partitioning these files so ruthlessly. In fact, there's a good chance I'd just write the whole program in a single file and let the devil have his way with me. But we are pretending that this is a multi-mega-line enterprise application, and so we're going to be assiduously careful with all these source code dependencies. Right?

So the way we have to solve this is by falling back on something like the old C mechanism of declarations and implementations. See [[[Figure 17.4]{.underline}]{.calibre_10}](#index_split_034.html#filepos724200).

![](images/00096.jpg){#filepos724200 .calibre_93}

[[Figure 17.4.]{.bold}]{.calibre3}[ Breaking the dependency cycle]{.calibre3}

By splitting [` water `{.calibre4}]{.calibre_17} such that its [` fish `{.calibre4}]{.calibre_17} dependency is in [` water-imp `{.calibre4}]{.calibre_17}, and by making sure that [` water-imp `{.calibre4}]{.calibre_17} depends upon [` water `{.calibre4}]{.calibre_17} instead of the other way around (the DIP), the cycle is broken. I also split up [` fish `{.calibre4}]{.calibre_17} and [` shark `{.calibre4}]{.calibre_17}[]{#index_split_034.html#filepos724973}[[[[12]{.underline}]{.calibre_10}]{.calibre3}](#index_split_034.html#filepos725281) for consistency. I'll probably have to split up [` animal `{.calibre4}]{.calibre_17} pretty soon too.[]{#index_split_034.html#filepos725184}[[[[13]{.underline}]{.calibre_10}]{.calibre3}](#index_split_034.html#filepos725572)

[[[12]{.underline}]{.calibre_10}](#index_split_034.html#filepos724973). Actually, just [` fish `{.calibre4}]{.calibre_17}. I split [` shark `{.calibre4}]{.calibre_17} on the diagram but not in the code. YAGNI, YAGNI, YAGNI.

[[[13]{.underline}]{.calibre_10}](#index_split_034.html#filepos725184). Future Uncle Bob: . . .nope.

So now the code looks like this:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_287.html#filepos992821)

> > [[`(ns wator.world`{.calibre4}\
> > `  (:require [wator`{.calibre4}\
> > `             [water :as water]]))`{.calibre4}\
> > \
> > `(defn make [w h]`{.calibre4}\
> > `  (let [locs (for [x (range w) y (range h)] [x y])`{.calibre4}\
> > `        loc-water (interleave locs (repeat (water/make)))`{.calibre4}\
> > `        cells (apply hash-map loc-water)]`{.calibre4}\
> > `    {::cells cells`{.calibre4}\
> > `     ::bounds [w h]}))`{.calibre4}\
> > \
> > `(defn set-cell [world loc cell]`{.calibre4}\
> > `  (assoc-in world [::cells loc] cell))`{.calibre4}\
> > \
> > `(defn get-cell [world loc]`{.calibre4}\
> > `  (get-in world [::cells loc]))`{.calibre4}\
> > \
> > `; . . .`{.calibre4}\
> > \
> > `—————`{.calibre4}\
> > \
> > `(ns wator.cell)`{.calibre4}\
> > \
> > `(defmulti tick ::type)`{.calibre4}\
> > \
> > `—————`{.calibre4}\
> > \
> > `(ns wator.water`{.calibre4}\
> > `  (:require [wator`{.calibre4}\
> > `             [cell :as cell]]))`{.calibre4}\
> > \
> > `(defn make [] {::cell/type ::water})`{.calibre4}\
> > \
> > `(defn is? [cell]`{.calibre4}\
> > `  (= ::water (::cell/type cell)))`{.calibre4}\
> > \
> > `——————————`{.calibre4}\
> > \
> > `(ns wator.water-imp`{.calibre4}\
> > `  (:require [wator`{.calibre4}\
> > `             [cell :as cell]`{.calibre4}\
> > `             [water :as water]`{.calibre4}\
> > `             [fish :as fish]`{.calibre4}\
> > `             [config :as config]]))`{.calibre4}\
> > \
> > `(defmethod cell/tick ::water/water [water]`{.calibre4}\
> > `  (if (> (rand) config/water-evolution-rate)`{.calibre4}\
> > `    (fish/make)`{.calibre4}\
> > `    water))`{.calibre4}\
> > \
> > `———————`{.calibre4}\
> > \
> > `(ns wator.animal`{.calibre4}\
> > `  (:require [wator`{.calibre4}\
> > `             [world :as world]`{.calibre4}\
> > `             [cell :as cell]`{.calibre4}\
> > `             [water :as water]]))`{.calibre4}\
> > \
> > `(defmulti move (fn [animal & args] (::cell/type animal)))`{.calibre4}\
> > `(defmulti reproduce (fn [animal & args] (::cell/type animal)))`{.calibre4}\
> > \
> > `(defn tick [animal]`{.calibre4}\
> > `  )`{.calibre4}\
> > \
> > `(defn do-move [animal loc world]`{.calibre4}\
> > `  (let [neighbors (world/neighbors world loc)`{.calibre4}\
> > `        destinations (filter #(water/is?`{.calibre4}\
> > `                               (world/get-cell world %))`{.calibre4}\
> > `                             neighbors)`{.calibre4}\
> > `        new-location (rand-nth destinations)]`{.calibre4}\
> > `    [new-location animal]))`{.calibre4}\
> > \
> > `————`{.calibre4}\
> > \
> > `(ns wator.fish`{.calibre4}\
> > `  (:require [wator`{.calibre4}\
> > `             [cell :as cell]]))`{.calibre4}\
> > `(defn make [] {::cell/type ::fish})`{.calibre4}\
> > \
> > `——————`{.calibre4}\
> > \
> > `(ns wator.fish-imp`{.calibre4}\
> > `  (:require [wator`{.calibre4}\
> > `             [cell :as cell]`{.calibre4}\
> > `             [animal :as animal]`{.calibre4}\
> > `             [fish :as fish]]))`{.calibre4}\
> > \
> > `(defmethod cell/tick ::fish/fish [fish]`{.calibre4}\
> > `  (animal/tick fish)`{.calibre4}\
> > `  )`{.calibre4}\
> > \
> > `(defmethod animal/move ::fish/fish [fish loc world]`{.calibre4}\
> > `  (animal/do-move fish loc world))`{.calibre4}\
> > \
> > `(defmethod animal/reproduce ::fish/fish [fish]`{.calibre4}\
> > `  )`{.calibre4}]{.calibre_3}]{.calibre_17}

The [` shark `{.calibre4}]{.calibre_17} isn't relevant yet, so I didn't show it.

The criterion for splitting [` water `{.calibre4}]{.calibre_17} and [` fish `{.calibre4}]{.calibre_17} is pretty easy to see. Any function that references a file outside of the direct type hierarchy gets put into the [` imp `{.calibre4}]{.calibre_17} file. Pay special attention to the namespaces and the namespaced keywords. For example, notice that the [` defmethod `{.calibre4}]{.calibre_17}s in [` fish-imp `{.calibre4}]{.calibre_17} will still be dispatched on [` ::fish/fish `{.calibre4}]{.calibre_17}.

And just in case you thought I'd forgotten, here are the current tests:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_290.html#filepos993259)

> > [[`(ns wator.core-spec`{.calibre4}\
> > `  (:require [speclj.core :refer :all]`{.calibre4}\
> > `            [wator`{.calibre4}\
> > `             [cell :as cell]`{.calibre4}\
> > `             [water :as water]`{.calibre4}\
> > `             [water-imp]`{.calibre4}\
> > `             [animal :as animal]`{.calibre4}\
> > `             [fish :as fish]`{.calibre4}\
> > `             [fish-imp]`{.calibre4}\
> > `             [world :as world]]))`{.calibre4}\
> > `(describe "Wator"`{.calibre4}\
> > `  (with-stubs)`{.calibre4}\
> > `  (context "Water"`{.calibre4}\
> > `    (it "usually remains water"`{.calibre4}\
> > `      (with-redefs [rand (stub :rand {:return 0.0})]`{.calibre4}\
> > `        (let [water (water/make)`{.calibre4}\
> > `              evolved (cell/tick water)]`{.calibre4}\
> > `          (should= ::water/water (::cell/type evolved)))))`{.calibre4}\
> > \
> > `    (it "occasionally evolves into a fish"`{.calibre4}\
> > `      (with-redefs [rand (stub :rand {:return 1.0})]`{.calibre4}\
> > `        (let [water (water/make)`{.calibre4}\
> > `              evolved (cell/tick water)]`{.calibre4}\
> > `          (should= ::fish/fish (::cell/type evolved))))))`{.calibre4}\
> > \
> > `  (context "world"`{.calibre4}\
> > `    (it "creates a world full of water cells"`{.calibre4}\
> > `      (let [world (world/make 2 2)`{.calibre4}\
> > `            cells (::world/cells world)`{.calibre4}\
> > `            positions (set (keys cells))]`{.calibre4}\
> > `        (should= #{[0 0] [0 1]`{.calibre4}\
> > `                   [1 0] [1 1]} positions)`{.calibre4}\
> > `        (should (every? #(= ::water/water (::cell/type %))`{.calibre4}\
> > `                        (vals cells)))))`{.calibre4}\
> > \
> > `    (it "makes neighbors"`{.calibre4}\
> > `      (let [world (world/make 5 5)]`{.calibre4}\
> > `        (should= [[0 0] [0 1] [0 2]`{.calibre4}\
> > `                  [1 0] [1 2]`{.calibre4}\
> > `                  [2 0] [2 1] [2 2]]`{.calibre4}\
> > `                 (world/neighbors world [1 1]))`{.calibre4}\
> > `        (should= [[4 4] [4 0] [4 1]`{.calibre4}\
> > `                  [0 4] [0 1]`{.calibre4}\
> > `                  [1 4] [1 0] [1 1]]`{.calibre4}\
> > `                 (world/neighbors world [0 0]))`{.calibre4}\
> > `        (should= [[3 3] [3 4] [3 0]`{.calibre4}\
> > `                  [4 3] [4 0]`{.calibre4}\
> > `                  [0 3] [0 4] [0 0]]`{.calibre4}\
> > `                 (world/neighbors world [4 4])))))`{.calibre4}\
> > \
> > `  (context "animal"`{.calibre4}\
> > `    (it "moves"`{.calibre4}\
> > `      (let [fish (fish/make)`{.calibre4}\
> > `            world (-> (world/make 3 3)`{.calibre4}\
> > `                      (world/set-cell [1 1] fish))`{.calibre4}\
> > `            [loc cell] (animal/move fish [1 1] world)]`{.calibre4}\
> > `        (should= cell fish)`{.calibre4}\
> > `        (should (#{[0 0] [0 1] [0 2]`{.calibre4}\
> > `                   [1 0] [1 2]`{.calibre4}\
> > `                   [2 0] [2 1] [2 2]}`{.calibre4}\
> > `                 loc))))))`{.calibre4}]{.calibre_3}]{.calibre_17}
>
> []{#index_split_034.html#filepos733849}

Look at the [` :require `{.calibre4}]{.calibre_17} up in the [` ns `{.calibre4}]{.calibre_17} statement. Notice that we are requiring the [` imp `{.calibre4}]{.calibre_17}s but not explicitly using them. Requiring them registers the [` defmethod `{.calibre4}]{.calibre_17}s that they contain.

OK, now that we can move the [` fish `{.calibre4}]{.calibre_17}, I'm pretty sure the [` shark `{.calibre4}]{.calibre_17}s will move too. So next we should try some reproduction. But before we do that, I'm getting (pretend) concerned about the type system for the [` world `{.calibre4}]{.calibre_17}. Let's get that set up first:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_292.html#filepos993551)

> > [[`(ns wator.world`{.calibre4}\
> > `  (:require [clojure.spec.alpha :as s]`{.calibre4}\
> > `            [wator`{.calibre4}\
> > `             [cell :as cell]`{.calibre4}\
> > `             [water :as water]]))`{.calibre4}\
> > \
> > `(s/def ::location (s/tuple int? int?))`{.calibre4}\
> > `(s/def ::cell #(contains? % ::cell/type))`{.calibre4}\
> > `(s/def ::cells (s/map-of ::location ::cell))`{.calibre4}\
> > `(s/def ::bounds ::location)`{.calibre4}\
> > `(s/def ::world (s/keys :req [::cells ::bounds]))`{.calibre4}\
> > \
> > `(defn make [w h]`{.calibre4}\
> > `  {:post [(s/valid? ::world %)]}`{.calibre4}\
> > `  …)`{.calibre4}]{.calibre_3}]{.calibre_17}

OK, that's better. Now, what do we need for reproduction? The modelers said that a [` fish `{.calibre4}]{.calibre_17} will reproduce if it is next to a [` water `{.calibre4}]{.calibre_17} cell and is above a certain age. The two daughter [` fish `{.calibre4}]{.calibre_17} have their ages reset to zero. Otherwise, the [` ::age `{.calibre4}]{.calibre_17} of a [` fish `{.calibre4}]{.calibre_17} increases with time.

Here are the tests:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_293.html#filepos993697)

> > [[`(it "reproduces"`{.calibre4}\
> > `  (let [fish (-> (fish/make)`{.calibre4}\
> > `                 (animal/set-age config/fish-reproduction-age))`{.calibre4}\
> > `        world (-> (world/make 3 3)`{.calibre4}\
> > `                  (world/set-cell [1 1] fish))`{.calibre4}\
> > `        [loc1 cell1 loc2 cell2] (animal/reproduce`{.calibre4}\
> > `                                  fish [1 1] world)]`{.calibre4}\
> > `    (should= loc1 [1 1])`{.calibre4}\
> > `    (should (fish/is? cell1))`{.calibre4}\
> > `    (should= 0 (animal/age cell1))`{.calibre4}\
> > `    (should (#{[0 0] [0 1] [0 2]`{.calibre4}\
> > `               [1 0] [1 2]`{.calibre4}\
> > `               [2 0] [2 1] [2 2]}`{.calibre4}\
> > `             loc2))`{.calibre4}\
> > `    (should (fish/is? cell2))`{.calibre4}\
> > `    (should= 0 (animal/age cell2))))`{.calibre4}\
> > \
> > `(it "doesn't reproduce if there is no room"`{.calibre4}\
> > `  (let [fish (-> (fish/make)`{.calibre4}\
> > `                 (animal/set-age config/fish-reproduction-age))`{.calibre4}\
> > `        world (-> (world/make 1 1)`{.calibre4}\
> > `                  (world/set-cell [0 0] fish))`{.calibre4}\
> > `        failed (animal/reproduce fish [0 0] world)]`{.calibre4}\
> > `    (should-be-nil failed)))`{.calibre4}\
> > \
> > `(it "doesn't reproduce if too young"`{.calibre4}\
> > `      (let [fish (-> (fish/make)`{.calibre4}\
> > `                     (animal/set-age`{.calibre4}\
> > `                       (dec config/fish-reproduction-age)))`{.calibre4}\
> > `            world (-> (world/make 3 3)`{.calibre4}\
> > `                      (world/set-cell [1 1] fish))`{.calibre4}\
> > `            failed (animal/reproduce fish [1 1] world)]`{.calibre4}\
> > `        (should-be-nil failed)))`{.calibre4}]{.calibre_3}]{.calibre_17}

Notice that if the [` fish `{.calibre4}]{.calibre_17} reproduces, the return value contains both daughters. But if something goes wrong, we return [` nil `{.calibre4}]{.calibre_17}. This is because I reckon that the high-level policy of a [` fish `{.calibre4}]{.calibre_17} includes something like this:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_294.html#filepos993843)

> > [[`(if-let [result (animal/reproduce …)]`{.calibre4}\
> > `  result`{.calibre4}\
> > `  (animal/move …))`{.calibre4}]{.calibre_3}]{.calibre_17}

Anyway, here's the abbreviated code that passes that test:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_295.html#filepos993988)

> > [[`(ns wator.animal`{.calibre4}\
> > `  (:require [clojure.spec.alpha :as s]`{.calibre4}\
> > `            [wator`{.calibre4}\
> > `             [world :as world]`{.calibre4}\
> > `             [cell :as cell]`{.calibre4}\
> > `             [water :as water]`{.calibre4}\
> > `             [config :as config]]))`{.calibre4}\
> > \
> > `(s/def ::age int?)`{.calibre4}\
> > `(s/def ::animal (s/keys :req [::age]))`{.calibre4}\
> > \
> > `(defmulti move (fn [animal & args] (::cell/type animal)))`{.calibre4}\
> > `(defmulti reproduce (fn [animal & args] (::cell/type animal)))`{.calibre4}\
> > ]{.calibre_3}]{.calibre_17}[[`(defmulti make-child ::cell/type)`{.calibre4}]{.calibre_3}]{.bold}[[\
> > \
> > ]{.calibre_3}]{.calibre_17}[[`(defn make []`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `  `{.calibre4}]{.calibre_3}]{.calibre_17}[[`{::age 0})`{.calibre4}]{.calibre_3}]{.bold}[[\
> > \
> > ]{.calibre_3}]{.calibre_17}[[`(defn age [animal]`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `  `{.calibre4}]{.calibre_3}]{.calibre_17}[[`(::age animal))`{.calibre4}]{.calibre_3}]{.bold}[[\
> > \
> > ]{.calibre_3}]{.calibre_17}[[`(defn set-age [animal age]`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `  `{.calibre4}]{.calibre_3}]{.calibre_17}[[`(assoc animal ::age age))`{.calibre4}]{.calibre_3}]{.bold}[[\
> > \
> > ]{.calibre_3}]{.calibre_17}[[`;. . .`{.calibre4}]{.calibre_3}]{.bold}[[\
> > \
> > ]{.calibre_3}]{.calibre_17}[[`(defn do-reproduce [animal loc world]`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `  `{.calibre4}]{.calibre_3}]{.calibre_17}[[`(if (>= (age animal) config/fish-reproduction-age)`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `    `{.calibre4}]{.calibre_3}]{.calibre_17}[[`(let [neighbors (world/neighbors world loc)`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `          `{.calibre4}]{.calibre_3}]{.calibre_17}[[`birth-places (filter #(water/is? (world/get-cell world %))`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `                               `{.calibre4}]{.calibre_3}]{.calibre_17}[[`neighbors)]`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `      `{.calibre4}]{.calibre_3}]{.calibre_17}[[`(if (empty? birth-places)`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `        `{.calibre4}]{.calibre_3}]{.calibre_17}[[`nil`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `        `{.calibre4}]{.calibre_3}]{.calibre_17}[[`[loc (set-age animal 0)`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `         `{.calibre4}]{.calibre_3}]{.calibre_17}[[`(rand-nth birth-places) (make-child animal)]))`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `    `{.calibre4}]{.calibre_3}]{.calibre_17}[[`nil))`{.calibre4}]{.calibre_3}]{.bold}[[\
> > \
> > ]{.calibre_3}]{.calibre_17}[[`————`{.calibre4}]{.calibre_3}]{.bold}[[\
> > \
> > `(ns wator.fish`{.calibre4}\
> > `  (:require [clojure.spec.alpha :as s]`{.calibre4}\
> > `            [wator`{.calibre4}\
> > `             [cell :as cell]`{.calibre4}\
> > `             [animal :as animal]]))`{.calibre4}\
> > \
> > ]{.calibre_3}]{.calibre_17}[[`(s/def ::fish (s/and #(= ::fish (::cell/type %))`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `                     `{.calibre4}]{.calibre_3}]{.calibre_17}[[`::animal/animal))`{.calibre4}]{.calibre_3}]{.bold}[[\
> > ]{.calibre_3}]{.calibre_17}[[`(defn is? [cell]`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `  `{.calibre4}]{.calibre_3}]{.calibre_17}[[`(= ::fish (::cell/type cell)))`{.calibre4}]{.calibre_3}]{.bold}[[\
> > \
> > ]{.calibre_3}]{.calibre_17}[[`(defn make []`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `  `{.calibre4}]{.calibre_3}]{.calibre_17}[[`{:post [(s/valid? ::fish %)]}`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `  `{.calibre4}]{.calibre_3}]{.calibre_17}[[`(merge {::cell/type ::fish}`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `         `{.calibre4}]{.calibre_3}]{.calibre_17}[[`(animal/make)))`{.calibre4}]{.calibre_3}]{.bold}[[\
> > \
> > ]{.calibre_3}]{.calibre_17}[[`(defmethod animal/make-child ::fish [fish]`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `  `{.calibre4}]{.calibre_3}]{.calibre_17}[[`(make))`{.calibre4}]{.calibre_3}]{.bold}[[\
> > \
> > `——————`{.calibre4}\
> > \
> > `(ns wator.fish-imp`{.calibre4}\
> > `  (:require [wator`{.calibre4}\
> > `             [cell :as cell]`{.calibre4}\
> > `             [animal :as animal]`{.calibre4}\
> > `             [fish :as fish]]))`{.calibre4}\
> > \
> > `;. . .`{.calibre4}\
> > \
> > `(defmethod animal/reproduce ::fish/fish [fish loc world]`{.calibre4}\
> > `  (animal/do-reproduce fish loc world))`{.calibre4}]{.calibre_3}]{.calibre_17}
>
> []{#index_split_034.html#filepos745467}

Again, notice that I am deferring the [` fish/reproduce `{.calibre4}]{.calibre_17} function to [` animal/do-reproduce `{.calibre4}]{.calibre_17}. This allows me to specify the common behavior of [` reproduce `{.calibre4}]{.calibre_17} in [` animal `{.calibre4}]{.calibre_17} while allowing [` fish `{.calibre4}]{.calibre_17} to override or augment it. I don't know if this will be necessary,[]{#index_split_034.html#filepos745991}[[[[14]{.underline}]{.calibre_10}]{.calibre3}](#index_split_034.html#filepos746260) but it's pretty cheap to add and it eliminates the duplication in [` shark `{.calibre4}]{.calibre_17} and [` fish `{.calibre4}]{.calibre_17}.

[[[14]{.underline}]{.calibre_10}](#index_split_034.html#filepos745991). Yeah, I know, YAGNI and all that. But rules are meant to be broken.

[[[Scratch That Itch]{.calibre_3}]{.bold}]{.calibre1}

I'm getting an itchy feeling that I should have implemented [` world/tick `{.calibre4}]{.calibre_17} first. I've made a lot of decisions about the return values of [` move `{.calibre4}]{.calibre_17} and [` reproduce `{.calibre4}]{.calibre_17} based upon what I think [` world/tick `{.calibre4}]{.calibre_17} is going to need. So let's switch gears and focus on that before we continue to add more, possibly errant, goop to the [` animal `{.calibre4}]{.calibre_17}s.

Here's the first test:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_297.html#filepos994280)

> > [[`(it "moves a fish around each tick"`{.calibre4}\
> > `  (let [fish (fish/make)`{.calibre4}\
> > `        small-world (-> (world/make 1 2)`{.calibre4}\
> > `                        (world/set-cell [0 0] fish)`{.calibre4}\
> > `                        (world/tick))`{.calibre4}\
> > `        vacated-cell (world/get-cell small-world [0 0])`{.calibre4}\
> > `        occupied-cell (world/get-cell small-world [0 1])]`{.calibre4}\
> > `    (should (water/is? vacated-cell))`{.calibre4}\
> > `    (should (fish/is? occupied-cell))`{.calibre4}\
> > `    (should= 1 (animal/age occupied-cell))))`{.calibre4}]{.calibre_3}]{.calibre_17}

It's pretty simple. We make a [` small-world `{.calibre4}]{.calibre_17} with two cells, one of which is a [` fish `{.calibre4}]{.calibre_17}. We call [` tick `{.calibre4}]{.calibre_17} on that [` world `{.calibre4}]{.calibre_17}, and then we make sure that the [` fish `{.calibre4}]{.calibre_17} moves to the vacant cell and that it leaves [` water `{.calibre4}]{.calibre_17} behind.

Next, I wrote a dummy implementation for [` tick `{.calibre4}]{.calibre_17}, just to see the test pass:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_298.html#filepos994426)

> > [[`(defn tick [world]`{.calibre4}\
> > `  (-> (make 2 1)`{.calibre4}\
> > `        (set-cell [0 0] (water/make))`{.calibre4}\
> > `        (set-cell [0 1] (animal/set-age (fish/make) 1))))`{.calibre4}]{.calibre_3}]{.calibre_17}

Lo and behold, this won't compile because [` world `{.calibre4}]{.calibre_17} now depends upon [` fish `{.calibre4}]{.calibre_17}, which depends upon [` animal `{.calibre4}]{.calibre_17}, which depends back upon [` world `{.calibre4}]{.calibre_17}. Sigh. Cyclic dependencies are the bane of source code structures that are thought through poorly.

But we know how to solve this. We simply have to invert a dependency (the DIP) by splitting [` world-imp `{.calibre4}]{.calibre_17} out of [` world `{.calibre4}]{.calibre_17}. The UML looks like [[[Figure 17.5]{.underline}]{.calibre_10}](#index_split_034.html#filepos750141).

![](images/00135.jpg){#filepos750141 .calibre_94}

[[Figure 17.5.]{.bold}]{.calibre3}[ Breaking another dependency cycle]{.calibre3}

The [` =0 `{.calibre4}]{.calibre_17} next to [` tick `{.calibre4}]{.calibre_17} in the [` World `{.calibre4}]{.calibre_17} class is my way of indicating that it is an abstract method. So here's the code:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_299.html#filepos994571)

> > [[`(ns wator.world`{.calibre4}\
> > `  (:require [clojure.spec.alpha :as s]`{.calibre4}\
> > `            [wator`{.calibre4}\
> > `             [cell :as cell]`{.calibre4}\
> > `             [water :as water]]))`{.calibre4}\
> > \
> > `(s/def ::location (s/tuple int? int?))`{.calibre4}\
> > `(s/def ::cell #(contains? % ::cell/type))`{.calibre4}\
> > `(s/def ::cells (s/map-of ::location ::cell))`{.calibre4}\
> > `(s/def ::bounds ::location)`{.calibre4}\
> > `(s/def ::world `{.calibre4}]{.calibre_3}]{.calibre_17}[[`(s/and`{.calibre4}]{.calibre_3}]{.bold}[[` (s/keys :req [::cells ::bounds])`{.calibre4}\
> > `                      `{.calibre4}]{.calibre_3}]{.calibre_17}[[`#(= (::type %) ::world)))`{.calibre4}]{.calibre_3}]{.bold}[[\
> > \
> > ]{.calibre_3}]{.calibre_17}[[`(defmulti tick ::type)`{.calibre4}]{.calibre_3}]{.bold}[[\
> > \
> > `(defn make [w h]`{.calibre4}\
> > `  {:post [(s/valid? ::world %)]}`{.calibre4}\
> > `  (let [locs (for [x (range w) y (range h)] [x y])`{.calibre4}\
> > `        loc-water (interleave locs (repeat (water/make)))`{.calibre4}\
> > `        cells (apply hash-map loc-water)]`{.calibre4}\
> > `    `{.calibre4}]{.calibre_3}]{.calibre_17}[[`{::type ::world`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `     ::cells cells`{.calibre4}\
> > `     ::bounds [w h]}))`{.calibre4}\
> > \
> > `; . . .`{.calibre4}\
> > `—————`{.calibre4}\
> > `(ns wator.world-imp`{.calibre4}\
> > `  (:require [wator`{.calibre4}\
> > `             [world :as world :refer :all]`{.calibre4}\
> > `             [animal :as animal]`{.calibre4}\
> > `             [fish :as fish]`{.calibre4}\
> > `             [water :as water]]))`{.calibre4}\
> > `(defmethod world/tick ::world/world [world]`{.calibre4}\
> > `  (-> (make 2 1)`{.calibre4}\
> > `        (set-cell [0 0] (water/make))`{.calibre4}\
> > `        (set-cell [0 1] (animal/set-age (fish/make) 1))))`{.calibre4}]{.calibre_3}]{.calibre_17}
>
> []{#index_split_034.html#filepos752976}

This passed the test once I added [` [world-imp] `{.calibre4}]{.calibre_17} to the [` :require `{.calibre4}]{.calibre_17} list in the test. Take note that [` tick `{.calibre4}]{.calibre_17} is now a multi-method with only one implementation. That's the dependency inversion that we needed.

But now I'm bothered by that [` water `{.calibre4}]{.calibre_17} dependency in [` world `{.calibre4}]{.calibre_17}. There's a technical term for how I feel about it. That term is [icky]{.italic}. That dependency is [wrong]{.italic} somehow.

I need a shower. I resolve lots of issues while in the shower.

[[[Showers Solve Problems]{.calibre_3}]{.bold}]{.calibre1}

OK, I'm back from my shower, and this is the conversation I had with myself while under the spray.

"Creating [` water `{.calibre4}]{.calibre_17} in [` world `{.calibre4}]{.calibre_17} is icky. I mean, I just split [` world `{.calibre4}]{.calibre_17} in two because creating a [` fish `{.calibre4}]{.calibre_17} led to a cycle. So creating [` water `{.calibre4}]{.calibre_17} could lead to a cycle too. But wait, this is all about creation. Maybe what I need is a factory! Yeah, an Abstract Factory named [` cell-factory `{.calibre4}]{.calibre_17}, and it will take opaque tokens like [` :fish `{.calibre4}]{.calibre_17} and [` :water `{.calibre4}]{.calibre_17}, and. . . (OH!). . . and [` :default-cell `{.calibre4}]{.calibre_17}. Yeah, and. . . Wait, why do I need a whole new factory? Why can't [` world `{.calibre4}]{.calibre_17} BE the factory? Yeah! That's the [Factory Method]{.italic} pattern. That's the ticket!"

The UML for this (in [[[Figure 17.6]{.underline}]{.calibre_10}](#index_split_034.html#filepos755538)) is revealing.

An architectural boundary just appeared. All dependencies cross it going toward the high-level side, following the Dependency Rule. I may not use this boundary in the actual architecture, but it's there if I need it.

![](images/00189.jpg){#filepos755538 .calibre_95}

[[Figure 17.6.]{.bold}]{.calibre3}[ Wa-Tor with the Factory Method pattern]{.calibre3}

So now the code looks like this:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_300.html#filepos994717)

> > [[`(ns wator.world`{.calibre4}\
> > `  (:require [clojure.spec.alpha :as s]`{.calibre4}\
> > `            [wator`{.calibre4}\
> > `             [cell :as cell]`{.calibre4}\
> > `             [water :as water]]))`{.calibre4}\
> > \
> > `(s/def ::location (s/tuple int? int?))`{.calibre4}\
> > `(s/def ::cell #(contains? % ::cell/type))`{.calibre4}\
> > `(s/def ::cells (s/map-of ::location ::cell))`{.calibre4}\
> > `(s/def ::bounds ::location)`{.calibre4}\
> > `(s/def ::world (s/and (s/keys :req [::cells ::bounds])`{.calibre4}\
> > `                      #(= (::type %) ::world)))`{.calibre4}\
> > \
> > `(defmulti tick ::type)`{.calibre4}\
> > ]{.calibre_3}]{.calibre_17}[[`(defmulti make-cell (fn [factory-type cell-type] factory-type))`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `(defn make [w h]`{.calibre4}\
> > `  {:post [(s/valid? ::world %)]}`{.calibre4}\
> > `  (let [locs (for [x (range w) y (range h)] [x y])`{.calibre4}\
> > `        `{.calibre4}]{.calibre_3}]{.calibre_17}[[`default-cell (make-cell ::world :default-cell)`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `        loc-water (interleave locs (repeat `{.calibre4}]{.calibre_3}]{.calibre_17}[[`default-cell`{.calibre4}]{.calibre_3}]{.bold}[[`))`{.calibre4}\
> > `        cells (apply hash-map loc-water)]`{.calibre4}\
> > `    {::type ::world`{.calibre4}\
> > `     ::cells cells`{.calibre4}\
> > `     ::bounds [w h]}))`{.calibre4}\
> > `;. . .`{.calibre4}\
> > \
> > `———————`{.calibre4}\
> > \
> > `(ns wator.world-imp`{.calibre4}\
> > `  (:require [wator`{.calibre4}\
> > `             [world :as world :refer :all]`{.calibre4}\
> > `             [animal :as animal]`{.calibre4}\
> > `             [fish :as fish]`{.calibre4}\
> > `                    `{.calibre4}]{.calibre_3}]{.calibre_17}[[`[shark :as shark]`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `             [water :as water]]))`{.calibre4}\
> > \
> > `(defmethod world/tick ::world/world [world]`{.calibre4}\
> > `  (-> (make 2 1)`{.calibre4}\
> > `        (set-cell [0 0] (water/make))`{.calibre4}\
> > `        (set-cell [0 1] (animal/set-age (fish/make) 1))))`{.calibre4}\
> > \
> > ]{.calibre_3}]{.calibre_17}[[`(defmethod world/make-cell ::world/world [world cell-type]`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `  `{.calibre4}]{.calibre_3}]{.calibre_17}[[`(condp = cell-type`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `    `{.calibre4}]{.calibre_3}]{.calibre_17}[[`:default-cell (water/make)`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `    `{.calibre4}]{.calibre_3}]{.calibre_17}[[`:water (water/make)`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `    `{.calibre4}]{.calibre_3}]{.calibre_17}[[`:fish (fish/make)`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `    `{.calibre4}]{.calibre_3}]{.calibre_17}[[`:shark (shark/make)))`{.calibre4}]{.calibre_3}]{.bold}

The [` factory-type `{.calibre4}]{.calibre_17} in [` make-cell `{.calibre4}]{.calibre_17} is simply passed in as [` ::world `{.calibre4}]{.calibre_17}. That allows the [` defmethod ::world/world `{.calibre4}]{.calibre_17} to resolve it.

I have high hopes for this change. And please note, this whole change was driven by one test that I made to pass using a dummy implementation in [` tick `{.calibre4}]{.calibre_17}, reminding us yet again that TDD is a design technique.

OK, now let's make that dummy implementation fail. Here's the test that fails:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_302.html#filepos995009)

> > [[`(it "moves a fish around each tick"`{.calibre4}\
> > `  (doseq [scenario`{.calibre4}\
> > `          [{:dimension [2 1] :starting [0 0] :ending [1 0]}`{.calibre4}\
> > `           {:dimension [2 1] :starting [1 0] :ending [0 0]}`{.calibre4}\
> > `           {:dimension [1 2] :starting [0 0] :ending [0 1]}`{.calibre4}\
> > `           {:dimension [1 2] :starting [0 1] :ending [0 0]}]]`{.calibre4}\
> > `    (let [fish (fish/make)`{.calibre4}\
> > `          {:keys [dimension starting ending]} scenario`{.calibre4}\
> > `          [h w] dimension`{.calibre4}\
> > `          small-world (-> (world/make h w)`{.calibre4}\
> > `                          (world/set-cell starting fish)`{.calibre4}\
> > `                          (world/tick))`{.calibre4}\
> > `          vacated-cell (world/get-cell small-world starting)`{.calibre4}\
> > `          occupied-cell (world/get-cell small-world ending)]`{.calibre4}\
> > `      (should (water/is? vacated-cell))`{.calibre4}\
> > `      (should (fish/is? occupied-cell))`{.calibre4}\
> > `      (should= 1 (animal/age occupied-cell)))))`{.calibre4}]{.calibre_3}]{.calibre_17}

I created the four possible 1-by-2 scenarios and made sure the [` world `{.calibre4}]{.calibre_17} got updated properly after a [` tick `{.calibre4}]{.calibre_17}.

Making this pass forced me to change the design yet again. The [` animal/move `{.calibre4}]{.calibre_17}, [` animal/reproduce `{.calibre4}]{.calibre_17}, and [` cell/tick `{.calibre4}]{.calibre_17} functions must return a [` [from to] `{.calibre4}]{.calibre_17} list in which each is a single-element map containing [` {loc cell} `{.calibre4}]{.calibre_17}. Look at the [` world-imp `{.calibre4}]{.calibre_17} and you'll see why:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_303.html#filepos995155)

> > [[`(ns wator.world-imp`{.calibre4}\
> > `  . . .)`{.calibre4}\
> > \
> > `(defmethod world/tick ::world/world [world]`{.calibre4}\
> > `  (let [cells (::world/cells world)]`{.calibre4}\
> > `    (loop [locs (keys cells)`{.calibre4}\
> > `           new-cells {}`{.calibre4}\
> > `           moved-into #{}]`{.calibre4}\
> > `      (cond`{.calibre4}\
> > \
> > `        (empty? locs)`{.calibre4}\
> > `        (assoc world ::world/cells new-cells)`{.calibre4}\
> > \
> > `        (contains? moved-into (first locs))`{.calibre4}\
> > `        (recur (rest locs) new-cells moved-into)`{.calibre4}\
> > \
> > `        :else`{.calibre4}\
> > `        (let [loc (first locs)`{.calibre4}\
> > `              cell (get cells loc)`{.calibre4}\
> > `              [from to] (cell/tick cell loc world)`{.calibre4}\
> > `              new-cells (-> new-cells (merge from) (merge to))`{.calibre4}\
> > `              to-loc (first (keys to))]`{.calibre4}\
> > `          (recur (rest locs)`{.calibre4}\
> > `                 new-cells`{.calibre4}\
> > `                 (conj moved-into to-loc)))))))`{.calibre4}\
> > \
> > `; . . .`{.calibre4}]{.calibre_3}]{.calibre_17}

It turns out that every operation makes changes to either one or two cells. When an [` animal `{.calibre4}]{.calibre_17} moves, reproduces, or eats, only two cells are involved. If an [` animal `{.calibre4}]{.calibre_17} fails to move, or if it starves, only one cell is involved. In the first case the operation will return [` [from to] `{.calibre4}]{.calibre_17}, and in the second case it will return [` [nil to] `{.calibre4}]{.calibre_17}. In either case, both [` from `{.calibre4}]{.calibre_17} and [` to `{.calibre4}]{.calibre_17} are [` merge `{.calibre4}]{.calibre_17}d[]{#index_split_034.html#filepos764504}[[[[15]{.underline}]{.calibre_10}]{.calibre3}](#index_split_034.html#filepos764661) into [` new-cells `{.calibre4}]{.calibre_17}.

[[[15]{.underline}]{.calibre_10}](#index_split_034.html#filepos764504). [` merge `{.calibre4}]{.calibre_17} is well behaved if you merge in a nil.

Notice the [` moved-into `{.calibre4}]{.calibre_17} argument of the loop. At first, I didn't have it there, and the tests failed because [` world/tick `{.calibre4}]{.calibre_17} moved the [` fish `{.calibre4}]{.calibre_17} to the remaining [` water `{.calibre4}]{.calibre_17} cell. But then [` world/tick `{.calibre4}]{.calibre_17} called [` cell/tick `{.calibre4}]{.calibre_17} on the [` water `{.calibre4}]{.calibre_17} cell, which replaced itself with [` water `{.calibre4}]{.calibre_17}. When the [` new-cells `{.calibre4}]{.calibre_17} were merged in, the [` water `{.calibre4}]{.calibre_17} overwrote the [` fish `{.calibre4}]{.calibre_17}.

So [` moved-into `{.calibre4}]{.calibre_17} is a set of all the [` to `{.calibre4}]{.calibre_17} cell locations. The [` cell/tick `{.calibre4}]{.calibre_17} function should not be called on them because they've been moved into by a previous [` tick `{.calibre4}]{.calibre_17}, and so the [` animal `{.calibre4}]{.calibre_17} there has already been [` tick `{.calibre4}]{.calibre_17}ed.

Quite a few changes had to be made throughout the structure to get this to work. So my "itch" from a few pages back was correct. It's a good thing I paid attention to it early enough to make the change doable:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_304.html#filepos995301)

> > [[`(ns wator.cell)`{.calibre4}\
> > \
> > `(defmulti tick (fn [cell & args] (::type cell)))`{.calibre4}\
> > \
> > `——————`{.calibre4}\
> > \
> > `(ns wator.water-imp`{.calibre4}\
> > `  (:require [wator`{.calibre4}\
> > `             [cell :as cell]`{.calibre4}\
> > `             [water :as water]`{.calibre4}\
> > `             [fish :as fish]`{.calibre4}\
> > `             [config :as config]]))`{.calibre4}\
> > \
> > `(defmethod cell/tick ::water/water [water `{.calibre4}]{.calibre_3}]{.calibre_17}[[`loc world`{.calibre4}]{.calibre_3}]{.bold}[[`]`{.calibre4}\
> > `  (if (> (rand) config/water-evolution-rate)`{.calibre4}\
> > `    `{.calibre4}]{.calibre_3}]{.calibre_17}[[`[nil {loc (fish/make)}]`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `    `{.calibre4}]{.calibre_3}]{.calibre_17}[[`[nil {loc water}]))`{.calibre4}]{.calibre_3}]{.bold}[[\
> > \
> > `————`{.calibre4}\
> > \
> > `(ns wator.animal . . .)`{.calibre4}\
> > \
> > `;. . .`{.calibre4}\
> > \
> > ]{.calibre_3}]{.calibre_17}[[`(defn increment-age [animal]`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `  `{.calibre4}]{.calibre_3}]{.calibre_17}[[`(update animal ::age inc))`{.calibre4}]{.calibre_3}]{.bold}[[\
> > \
> > ]{.calibre_3}]{.calibre_17}[[`(defn tick [animal loc world]`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `  `{.calibre4}]{.calibre_3}]{.calibre_17}[[`(-> animal`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `      `{.calibre4}]{.calibre_3}]{.calibre_17}[[`increment-age`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `      `{.calibre4}]{.calibre_3}]{.calibre_17}[[`(move loc world)))`{.calibre4}]{.calibre_3}]{.bold}[[\
> > \
> > `(defn do-move [animal loc world]`{.calibre4}\
> > `  (let [neighbors (world/neighbors world loc)`{.calibre4}\
> > `        destinations (filter #(water/is?`{.calibre4}\
> > `                               (world/get-cell world %))`{.calibre4}\
> > `                             neighbors)`{.calibre4}\
> > `        new-location (if (empty? destinations)`{.calibre4}\
> > `                       loc`{.calibre4}\
> > `                       (rand-nth destinations))]`{.calibre4}\
> > `    `{.calibre4}]{.calibre_3}]{.calibre_17}[[`(if (= new-location loc)`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `      `{.calibre4}]{.calibre_3}]{.calibre_17}[[`[nil {loc animal}]`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `      `{.calibre4}]{.calibre_3}]{.calibre_17}[[`[{loc (water/make)} {new-location animal}])))`{.calibre4}]{.calibre_3}]{.bold}[[\
> > \
> > `;. . .`{.calibre4}\
> > \
> > `————`{.calibre4}\
> > \
> > `(ns wator.fish-imp . . .)`{.calibre4}\
> > \
> > `(defmethod cell/tick ::fish/fish [fish `{.calibre4}]{.calibre_3}]{.calibre_17}[[`loc world`{.calibre4}]{.calibre_3}]{.bold}[[`]`{.calibre4}\
> > `  (animal/tick fish `{.calibre4}]{.calibre_3}]{.calibre_17}[[`loc world`{.calibre4}]{.calibre_3}]{.bold}[[`)`{.calibre4}\
> > `  )`{.calibre4}\
> > \
> > `; . . .`{.calibre4}]{.calibre_3}]{.calibre_17}

And, of course, a few of the tests needed to change:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_306.html#filepos995593)

> > [[`(ns wator.core-spec . . .)`{.calibre4}\
> > \
> > `(describe "Wator"`{.calibre4}\
> > `  (with-stubs)`{.calibre4}\
> > `  (context "Water"`{.calibre4}\
> > `    (it "usually remains water"`{.calibre4}\
> > `      (with-redefs [rand (stub :rand {:return 0.0})]`{.calibre4}\
> > `        (let [water (water/make)`{.calibre4}\
> > `              `{.calibre4}]{.calibre_3}]{.calibre_17}[[`world (world/make 1 1)`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `              `{.calibre4}]{.calibre_3}]{.calibre_17}[[`[from to] (cell/tick water [0 0] world)]`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `          `{.calibre4}]{.calibre_3}]{.calibre_17}[[`(should-be-nil from)`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `          `{.calibre4}]{.calibre_3}]{.calibre_17}[[`(should (water/is? (get to [0 0])))`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `          `{.calibre4}]{.calibre_3}]{.calibre_17}[[`)))`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `    (it "occasionally evolves into a fish"`{.calibre4}\
> > `      (with-redefs [rand (stub :rand {:return 1.0})]`{.calibre4}\
> > `        (let [water (water/make)`{.calibre4}\
> > `              `{.calibre4}]{.calibre_3}]{.calibre_17}[[`world (world/make 1 1)`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `              `{.calibre4}]{.calibre_3}]{.calibre_17}[[`[from to] (cell/tick water [0 0] world)]`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `          `{.calibre4}]{.calibre_3}]{.calibre_17}[[`(should-be-nil from)`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `          `{.calibre4}]{.calibre_3}]{.calibre_17}[[`(should (fish/is? (get to [0 0])))))))`{.calibre4}]{.calibre_3}]{.bold}[[\
> > \
> > ]{.calibre_3}]{.calibre_17}[[`;. . .`{.calibre4}]{.calibre_3}]{.bold}[[\
> > \
> > `  (context "animal"`{.calibre4}\
> > `    (it "moves"`{.calibre4}\
> > `      (let [fish (fish/make)`{.calibre4}\
> > `            world (-> (world/make 3 3)`{.calibre4}\
> > `                      (world/set-cell [1 1] fish))`{.calibre4}\
> > `            `{.calibre4}]{.calibre_3}]{.calibre_17}[[`[from to] (animal/move fish [1 1] world)`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `            `{.calibre4}]{.calibre_3}]{.calibre_17}[[`loc (first (keys to))]`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `        `{.calibre4}]{.calibre_3}]{.calibre_17}[[`(should (water/is? (get from [1 1])))`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `        `{.calibre4}]{.calibre_3}]{.calibre_17}[[`(should (fish/is? (get to loc)))`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `        (should (#{[0 0] [0 1] [0 2]`{.calibre4}\
> > `                   [1 0] [1 2]`{.calibre4}\
> > `                   [2 0] [2 1] [2 2]}`{.calibre4}\
> > `                 loc))))`{.calibre4}\
> > \
> > `    (it "doesn't move if there are no spaces"`{.calibre4}\
> > `      (let [fish (fish/make)`{.calibre4}\
> > `            world (-> (world/make 1 1)`{.calibre4}\
> > `                      (world/set-cell [0 0] fish))`{.calibre4}\
> > `            `{.calibre4}]{.calibre_3}]{.calibre_17}[[`[from to] (animal/move fish [0 0] world)]`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `        `{.calibre4}]{.calibre_3}]{.calibre_17}[[`(should (fish/is? (get to [0 0])))`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `        `{.calibre4}]{.calibre_3}]{.calibre_17}[[`(should (nil? from)))`{.calibre4}]{.calibre_3}]{.bold}

There's another scenario that I think will fail---two [` fish `{.calibre4}]{.calibre_17} competing for the same spot:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_308.html#filepos995885)

> > [[`(it "move two fish who compete for the same spot"`{.calibre4}\
> > `  (let [fish (fish/make)`{.calibre4}\
> > `        competitive-world (-> (world/make 3 1)`{.calibre4}\
> > `                              (world/set-cell [0 0] fish)`{.calibre4}\
> > `                              (world/set-cell [2 0] fish)`{.calibre4}\
> > `                              (world/tick))`{.calibre4}\
> > `        start-00 (world/get-cell competitive-world [0 0])`{.calibre4}\
> > `        start-20 (world/get-cell competitive-world [2 0])`{.calibre4}\
> > `        end-10 (world/get-cell competitive-world [1 0])]`{.calibre4}\
> > `    (should (fish/is? end-10))`{.calibre4}\
> > `    (should (or (fish/is? start-00)`{.calibre4}\
> > `                (fish/is? start-20)))`{.calibre4}\
> > `    (should (or (water/is? start-00)`{.calibre4}\
> > `                (water/is? start-20)))))`{.calibre4}]{.calibre_3}]{.calibre_17}

A simple 3-by-1 [` world `{.calibre4}]{.calibre_17} with [` fish `{.calibre4}]{.calibre_17} at either end. Only one of them can move into the center slot. The other will have to remain where it was. This test fails because the [` animal/move `{.calibre4}]{.calibre_17} function does not know that a [` fish `{.calibre4}]{.calibre_17} already moved into the target slot.

Solving this means somehow sending the [` moved-into `{.calibre4}]{.calibre_17} list to [` animal/move `{.calibre4}]{.calibre_17}. I hate the idea of adding yet another argument to [` animal/move `{.calibre4}]{.calibre_17}, so perhaps we can squirrel this information away in the [` world `{.calibre4}]{.calibre_17} that we pass to [` animal/move `{.calibre4}]{.calibre_17}:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_309.html#filepos996031)

> > [[`(ns wator.world-imp . . .)`{.calibre4}\
> > \
> > `(defmethod world/tick ::world/world [world]`{.calibre4}\
> > `  (let [cells (::world/cells world)]`{.calibre4}\
> > `    (loop [locs (keys cells)`{.calibre4}\
> > `           new-cells {}`{.calibre4}\
> > `           moved-into #{}]`{.calibre4}\
> > `      (cond`{.calibre4}\
> > `        (empty? locs)`{.calibre4}\
> > `        (assoc world ::world/cells new-cells)`{.calibre4}\
> > \
> > `        (contains? moved-into (first locs))`{.calibre4}\
> > `        (recur (rest locs) new-cells moved-into)`{.calibre4}\
> > \
> > `        :else`{.calibre4}\
> > `        (let [loc (first locs)`{.calibre4}\
> > `              cell (get cells loc)`{.calibre4}\
> > `              [from to] (cell/tick`{.calibre4}\
> > `                          cell loc`{.calibre4}\
> > `                          `{.calibre4}]{.calibre_3}]{.calibre_17}[[`(assoc world :moved-into moved-into))`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `              new-cells (-> new-cells (merge from) (merge to))`{.calibre4}\
> > `              to-loc (first (keys to))`{.calibre4}\
> > `              `{.calibre4}]{.calibre_3}]{.calibre_17}[[`to-cell (get to to-loc)`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `              `{.calibre4}]{.calibre_3}]{.calibre_17}[[`moved-into (if (water/is? to-cell)`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `                            `{.calibre4}]{.calibre_3}]{.calibre_17}[[`moved-into`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `                            `{.calibre4}]{.calibre_3}]{.calibre_17}[[`(conj moved-into to-loc))]`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `          (recur (rest locs) new-cells `{.calibre4}]{.calibre_3}]{.calibre_17}[[`moved-into`{.calibre4}]{.calibre_3}]{.bold}[[`))))))`{.calibre4}\
> > \
> > `———————`{.calibre4}\
> > \
> > `(ns wator.animal . . .)`{.calibre4}\
> > \
> > `; . . .`{.calibre4}\
> > \
> > `(defn do-move [animal loc world]`{.calibre4}\
> > `  (let [neighbors (world/neighbors world loc)`{.calibre4}\
> > `        `{.calibre4}]{.calibre_3}]{.calibre_17}[[`moved-into (get world :moved-into #{})`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `        `{.calibre4}]{.calibre_3}]{.calibre_17}[[`available-neighbors (remove moved-into neighbors)`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `        destinations (filter #(water/is?`{.calibre4}\
> > `                               (world/get-cell world %))`{.calibre4}\
> > `                             `{.calibre4}]{.calibre_3}]{.calibre_17}[[`available-neighbors`{.calibre4}]{.calibre_3}]{.bold}[[`)`{.calibre4}\
> > `        new-location (if (empty? destinations)`{.calibre4}\
> > `                       loc`{.calibre4}\
> > `                       (rand-nth destinations))]`{.calibre4}\
> > `    (if (= new-location loc)`{.calibre4}\
> > `      [nil {loc animal}]`{.calibre4}\
> > `      [{loc (water/make)} {new-location animal}])))`{.calibre4}]{.calibre_3}]{.calibre_17}

Note that I did not use a namespaced keyword for [` :moved-into `{.calibre4}]{.calibre_17}. That's because I consider it to be tramp data that is not really part of the [` world `{.calibre4}]{.calibre_17} and is just kind of hitching a ride. This feels a little dirty, but it works.[]{#index_split_034.html#filepos781439}[[[[16]{.underline}]{.calibre_10}]{.calibre3}](#index_split_034.html#filepos781536)

[[[16]{.underline}]{.calibre_10}](#index_split_034.html#filepos781439). Welcome to real-world engineering trade-offs.

Note that we only put locations into [` moved-into `{.calibre4}]{.calibre_17} if the [` cell `{.calibre4}]{.calibre_17} being moved in is not [` water `{.calibre4}]{.calibre_17}.

[[[It's Time to Wildly Reproduce]{.calibre_3}]{.bold}]{.calibre1}[]{#index_split_034.html#filepos782089}[[[[17]{.underline}]{.calibre_10}]{.calibre3}](#index_split_034.html#filepos782186)

[[[17]{.underline}]{.calibre_10}](#index_split_034.html#filepos782089). Ugliness breeds ugliness.

OK, let's see if we can fill the world with fish:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_311.html#filepos996323)

> > [[`(it "fills the world with reproducing fish"`{.calibre4}\
> > `  (loop [world (-> (world/make 10 10)`{.calibre4}\
> > `                   (world/set-cell [5 5] (fish/make)))`{.calibre4}\
> > `         n 100]`{.calibre4}\
> > `    (if (zero? n)`{.calibre4}\
> > `      (let [cells (-> world ::world/cells vals)`{.calibre4}\
> > `            fishies (filter fish/is? cells)`{.calibre4}\
> > `            fish-count (count fishies)]`{.calibre4}\
> > `        (should (< 50 fish-count)))`{.calibre4}\
> > `      (recur (world/tick world) (dec n)))))`{.calibre4}]{.calibre_3}]{.calibre_17}

Nifty. Create a 10-by-10 [` world `{.calibre4}]{.calibre_17}. Load it with one [` fish `{.calibre4}]{.calibre_17}. Send it 100 [` tick `{.calibre4}]{.calibre_17}s, and make sure there are more than 50 [` fish `{.calibre4}]{.calibre_17}. I mean, the fish are moving around and reproducing like crazy in there!

Of course, this test fails; but only because we didn't call [` reproduce `{.calibre4}]{.calibre_17} in [` animal/tick `{.calibre4}]{.calibre_17}. So let's fix that:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_312.html#filepos996469)

> > [[`(defn tick [animal loc world]`{.calibre4}\
> > `  (let [aged-animal (increment-age animal)`{.calibre4}\
> > `        reproduction (reproduce aged-animal loc world)]`{.calibre4}\
> > `    (if reproduction`{.calibre4}\
> > `      reproduction`{.calibre4}\
> > `      (move aged-animal loc world))))`{.calibre4}]{.calibre_3}]{.calibre_17}

Yup. Age the animal, then see if it will reproduce. If not, then move it. Simple. Easy.

Of course, I had to fix the fact that [` reproduce `{.calibre4}]{.calibre_17} didn't use our new [` [from to] `{.calibre4}]{.calibre_17} convention:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_313.html#filepos996615)

> > [[`(defn do-reproduce [animal loc world]`{.calibre4}\
> > `  (if (>= (age animal) config/fish-reproduction-age)`{.calibre4}\
> > `    (let [neighbors (world/neighbors world loc)`{.calibre4}\
> > `          birth-places (filter #(water/is?`{.calibre4}\
> > `                                 (world/get-cell world %))`{.calibre4}\
> > `                               neighbors)]`{.calibre4}\
> > `      (if (empty? birth-places)`{.calibre4}\
> > `        nil`{.calibre4}\
> > `        `{.calibre4}]{.calibre_3}]{.calibre_17}[[`[{loc (set-age animal 0)}`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `         `{.calibre4}]{.calibre_3}]{.calibre_17}[[`{(rand-nth birth-places) (make-child animal)}]))`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `    nil))`{.calibre4}]{.calibre_3}]{.calibre_17}
>
> []{#index_split_034.html#filepos786064}

And that broke an earlier test:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_314.html#filepos996761)

> > [[`(it "reproduces"`{.calibre4}\
> > `  (let [fish (-> (fish/make)`{.calibre4}\
> > `                 (animal/set-age config/fish-reproduction-age))`{.calibre4}\
> > `        world (-> (world/make 3 3)`{.calibre4}\
> > `                  (world/set-cell [1 1] fish))`{.calibre4}\
> > `        `{.calibre4}]{.calibre_3}]{.calibre_17}[[`[from to]`{.calibre4}]{.calibre_3}]{.bold}[[` (animal/reproduce fish [1 1] world)`{.calibre4}\
> > `        `{.calibre4}]{.calibre_3}]{.calibre_17}[[`from-loc (-> from keys first)`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `        `{.calibre4}]{.calibre_3}]{.calibre_17}[[`from-cell (-> from vals first)`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `        `{.calibre4}]{.calibre_3}]{.calibre_17}[[`to-loc (-> to keys first)`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `        `{.calibre4}]{.calibre_3}]{.calibre_17}[[`to-cell (-> to vals first)]`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `    (should= from-loc [1 1])`{.calibre4}\
> > `    (should (fish/is? from-cell))`{.calibre4}\
> > `    (should= 0 (animal/age from-cell))`{.calibre4}\
> > `    (should (#{[0 0] [0 1] [0 2]`{.calibre4}\
> > `               [1 0] [1 2]`{.calibre4}\
> > `               [2 0] [2 1] [2 2]}`{.calibre4}\
> > `             to-loc))`{.calibre4}\
> > `    (should (fish/is? to-cell))`{.calibre4}\
> > `    (should= 0 (animal/age to-cell))))`{.calibre4}]{.calibre_3}]{.calibre_17}

But with that, the [` fish `{.calibre4}]{.calibre_17} reproduce like. . . fish. That was pretty easy. I think our design is coming together.

[[[What about the Sharks?]{.calibre_3}]{.bold}]{.calibre1}

I've neglected the [` shark `{.calibre4}]{.calibre_17} class so far because its behavior is almost identical to [` fish `{.calibre4}]{.calibre_17} and is mostly governed by the [` animal `{.calibre4}]{.calibre_17} abstraction. But now let's see if we can get [` shark `{.calibre4}]{.calibre_17} objects to [` move `{.calibre4}]{.calibre_17} and [` reproduce `{.calibre4}]{.calibre_17}.

This required me to flesh out the [` shark `{.calibre4}]{.calibre_17} module and also make one small design change. I used the [Template Method]{.italic} pattern to get the reproduction age of an animal. The tests hint at that change:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_315.html#filepos996907)

> > [[`(context "animal"`{.calibre4}\
> > `  (it "moves"`{.calibre4}\
> > `    `{.calibre4}]{.calibre_3}]{.calibre_17}[[`(doseq [scenario`{.calibre4}]{.calibre_3}]{.bold}[[` `{.calibre4}\
> > `             `{.calibre4}]{.calibre_3}]{.calibre_17}[[`[{:constructor fish/make :tester fish/is?}`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `              `{.calibre4}]{.calibre_3}]{.calibre_17}[[`{:constructor shark/make :tester shark/is?}]]`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `      (let [animal (`{.calibre4}]{.calibre_3}]{.calibre_17}[[`(:constructor scenario)`{.calibre4}]{.calibre_3}]{.bold}[[`)`{.calibre4}\
> > `            world (-> (world/make 3 3)`{.calibre4}\
> > `                      (world/set-cell [1 1] animal))`{.calibre4}\
> > `            [from to] (animal/move animal [1 1] world)`{.calibre4}\
> > `            loc (first (keys to))]`{.calibre4}\
> > `        (should (water/is? (get from [1 1])))`{.calibre4}\
> > `        (should (`{.calibre4}]{.calibre_3}]{.calibre_17}[[`(:tester scenario)`{.calibre4}]{.calibre_3}]{.bold}[[` (get to loc)))`{.calibre4}\
> > `        (should (#{[0 0] [0 1] [0 2]`{.calibre4}\
> > `                   [1 0] [1 2]`{.calibre4}\
> > `                   [2 0] [2 1] [2 2]}`{.calibre4}\
> > `                 loc)))))`{.calibre4}\
> > \
> > `  (it "doesn't move if there are no spaces"`{.calibre4}\
> > `    `{.calibre4}]{.calibre_3}]{.calibre_17}[[`(doseq [scenario`{.calibre4}]{.calibre_3}]{.bold}[[` `{.calibre4}\
> > `             `{.calibre4}]{.calibre_3}]{.calibre_17}[[`[{:constructor fish/make :tester fish/is?}`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `              `{.calibre4}]{.calibre_3}]{.calibre_17}[[`{:constructor shark/make :tester shark/is?}]]`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `      (let [animal (`{.calibre4}]{.calibre_3}]{.calibre_17}[[`(:constructor scenario)`{.calibre4}]{.calibre_3}]{.bold}[[`)`{.calibre4}\
> > `            world (-> (world/make 1 1)`{.calibre4}\
> > `                      (world/set-cell [0 0] animal))`{.calibre4}\
> > `            [from to] (animal/move animal [0 0] world)]`{.calibre4}\
> > `        (should (`{.calibre4}]{.calibre_3}]{.calibre_17}[[`(:tester scenario)`{.calibre4}]{.calibre_3}]{.bold}[[` (get to [0 0])))`{.calibre4}\
> > `        (should (nil? from)))))`{.calibre4}\
> > `  (it "reproduces"`{.calibre4}\
> > `    `{.calibre4}]{.calibre_3}]{.calibre_17}[[`(doseq [scenario`{.calibre4}]{.calibre_3}]{.bold}[[` `{.calibre4}\
> > `             `{.calibre4}]{.calibre_3}]{.calibre_17}[[`[{:constructor fish/make :tester fish/is?}`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `              `{.calibre4}]{.calibre_3}]{.calibre_17}[[`{:constructor shark/make :tester shark/is?}]]`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `      (let [animal (`{.calibre4}]{.calibre_3}]{.calibre_17}[[`(:constructor scenario)`{.calibre4}]{.calibre_3}]{.bold}[[`)`{.calibre4}\
> > `            `{.calibre4}]{.calibre_3}]{.calibre_17}[[`reproduction-age (animal/get-reproduction-age animal)`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `            animal (animal/set-age animal reproduction-age)`{.calibre4}\
> > `            world (-> (world/make 3 3)`{.calibre4}\
> > `                      (world/set-cell [1 1] animal))`{.calibre4}\
> > `            [from to] (animal/reproduce animal [1 1] world)`{.calibre4}\
> > `            from-loc (-> from keys first)`{.calibre4}\
> > `            from-cell (-> from vals first)`{.calibre4}\
> > `            to-loc (-> to keys first)`{.calibre4}\
> > `            to-cell (-> to vals first)]`{.calibre4}\
> > `        (should= from-loc [1 1])`{.calibre4}\
> > `        (should (`{.calibre4}]{.calibre_3}]{.calibre_17}[[`(:tester scenario)`{.calibre4}]{.calibre_3}]{.bold}[[` from-cell))`{.calibre4}\
> > `        (should= 0 (animal/age from-cell))`{.calibre4}\
> > `        (should (#{[0 0] [0 1] [0 2]`{.calibre4}\
> > `                   [1 0] [1 2]`{.calibre4}\
> > `                   [2 0] [2 1] [2 2]}`{.calibre4}\
> > `                 to-loc))`{.calibre4}\
> > `        (should (`{.calibre4}]{.calibre_3}]{.calibre_17}[[`(:tester scenario)`{.calibre4}]{.calibre_3}]{.bold}[[` to-cell))`{.calibre4}\
> > `        (should= 0 (animal/age to-cell)))))`{.calibre4}\
> > \
> > `  (it "doesn't reproduce if there is no room"`{.calibre4}\
> > `    `{.calibre4}]{.calibre_3}]{.calibre_17}[[`(doseq [scenario`{.calibre4}]{.calibre_3}]{.bold}[[` `{.calibre4}\
> > `             `{.calibre4}]{.calibre_3}]{.calibre_17}[[`[{:constructor fish/make :tester fish/is?}`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `              `{.calibre4}]{.calibre_3}]{.calibre_17}[[`{:constructor shark/make :tester shark/is?}]]`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `      (let [animal (`{.calibre4}]{.calibre_3}]{.calibre_17}[[`(:constructor scenario)`{.calibre4}]{.calibre_3}]{.bold}[[`)`{.calibre4}\
> > `            `{.calibre4}]{.calibre_3}]{.calibre_17}[[`reproduction-age (animal/get-reproduction-age animal)`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `            animal (animal/set-age animal reproduction-age)`{.calibre4}\
> > `            world (-> (world/make 1 1)`{.calibre4}\
> > `                      (world/set-cell [0 0] animal))`{.calibre4}\
> > `            failed (animal/reproduce animal [0 0] world)]`{.calibre4}\
> > `        (should-be-nil failed))))`{.calibre4}\
> > \
> > `  (it "doesn't reproduce if too young"`{.calibre4}\
> > `    `{.calibre4}]{.calibre_3}]{.calibre_17}[[`(doseq [scenario`{.calibre4}]{.calibre_3}]{.bold}[[` `{.calibre4}\
> > `             `{.calibre4}]{.calibre_3}]{.calibre_17}[[`[{:constructor fish/make :tester fish/is?}`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `              `{.calibre4}]{.calibre_3}]{.calibre_17}[[`{:constructor shark/make :tester shark/is?}]]`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `      (let [animal (`{.calibre4}]{.calibre_3}]{.calibre_17}[[`(:constructor scenario)`{.calibre4}]{.calibre_3}]{.bold}[[`)`{.calibre4}\
> > `            `{.calibre4}]{.calibre_3}]{.calibre_17}[[`reproduction-age (animal/get-reproduction-age animal)`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `            animal (animal/set-age animal (dec reproduction-age))`{.calibre4}\
> > `            world (-> (world/make 3 3)`{.calibre4}\
> > `                      (world/set-cell [1 1] animal))`{.calibre4}\
> > `            failed (animal/reproduce animal [1 1] world)]`{.calibre4}\
> > `        (should-be-nil failed)))))`{.calibre4}\
> > \
> > `————————`{.calibre4}\
> > \
> > `(ns wator.animal …)`{.calibre4}\
> > \
> > `(defmulti move (fn [animal & args] (::cell/type animal)))`{.calibre4}\
> > `(defmulti reproduce (fn [animal & args] (::cell/type animal)))`{.calibre4}\
> > `(defmulti make-child ::cell/type)`{.calibre4}\
> > ]{.calibre_3}]{.calibre_17}[[`(defmulti get-reproduction-age ::cell/type)`{.calibre4}]{.calibre_3}]{.bold}[[\
> > \
> > ]{.calibre_3}]{.calibre_17}[[`; . . .`{.calibre4}]{.calibre_3}]{.bold}[[\
> > \
> > `————————`{.calibre4}\
> > \
> > `(ns wator.fish . . .)`{.calibre4}\
> > \
> > ]{.calibre_3}]{.calibre_17}[[`(defmethod animal/get-reproduction-age ::fish [fish]`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `  `{.calibre4}]{.calibre_3}]{.calibre_17}[[`config/fish-reproduction-age)`{.calibre4}]{.calibre_3}]{.bold}[[\
> > \
> > `; . . .`{.calibre4}\
> > \
> > `——————`{.calibre4}\
> > \
> > `(ns wator.shark`{.calibre4}\
> > `  (:require [clojure.spec.alpha :as s]`{.calibre4}\
> > `            [wator`{.calibre4}\
> > `             [config :as config]`{.calibre4}\
> > `             [cell :as cell]`{.calibre4}\
> > `             [animal :as animal]]))`{.calibre4}\
> > ]{.calibre_3}]{.calibre_17}[[`(s/def ::shark (s/and #(= ::shark (::cell/type %))`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `                      `{.calibre4}]{.calibre_3}]{.calibre_17}[[`::animal/animal))`{.calibre4}]{.calibre_3}]{.bold}[[\
> > ]{.calibre_3}]{.calibre_17}[[`(defn is? [cell]`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `  `{.calibre4}]{.calibre_3}]{.calibre_17}[[`(= ::shark (::cell/type cell)))`{.calibre4}]{.calibre_3}]{.bold}[[\
> > \
> > ]{.calibre_3}]{.calibre_17}[[`(defn make []`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `  `{.calibre4}]{.calibre_3}]{.calibre_17}[[`{:post [(s/valid? ::shark %)]}`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `  `{.calibre4}]{.calibre_3}]{.calibre_17}[[`(merge {::cell/type ::shark}`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `         `{.calibre4}]{.calibre_3}]{.calibre_17}[[`(animal/make)))`{.calibre4}]{.calibre_3}]{.bold}[[\
> > \
> > ]{.calibre_3}]{.calibre_17}[[`(defmethod animal/make-child ::shark [fish]`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `  `{.calibre4}]{.calibre_3}]{.calibre_17}[[`(make))`{.calibre4}]{.calibre_3}]{.bold}[[\
> > \
> > ]{.calibre_3}]{.calibre_17}[[`(defmethod animal/get-reproduction-age ::shark [shark]`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `  `{.calibre4}]{.calibre_3}]{.calibre_17}[[`config/shark-reproduction-age)`{.calibre4}]{.calibre_3}]{.bold}[[\
> > \
> > `; . . .`{.calibre4}]{.calibre_3}]{.calibre_17}

So far, with the exception of the reproduction age, the behavior of both the [` shark `{.calibre4}]{.calibre_17} and [` fish `{.calibre4}]{.calibre_17} is "inherited" from (actually it is delegated to) [` animal `{.calibre4}]{.calibre_17}. But the [` shark `{.calibre4}]{.calibre_17} class has extra constraints that we need to implement now.

The modelers have told us that a [` shark `{.calibre4}]{.calibre_17} only reproduces if its [` :health `{.calibre4}]{.calibre_17} is above a certain threshold. The [` :health `{.calibre4}]{.calibre_17} of a [` shark `{.calibre4}]{.calibre_17} is increased by eating a [` fish `{.calibre4}]{.calibre_17}, and it decreases with time. If the [` :health `{.calibre4}]{.calibre_17} of a [` shark `{.calibre4}]{.calibre_17} reaches zero, the [` shark `{.calibre4}]{.calibre_17} starves, leaving behind [` water `{.calibre4}]{.calibre_17}. When a [` shark `{.calibre4}]{.calibre_17} reproduces, its [` :health `{.calibre4}]{.calibre_17} is split between the two daughters.

OK, so let's test that the [` :health `{.calibre4}]{.calibre_17} decreases with age:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_319.html#filepos997491)

> > [[`(context "shark"`{.calibre4}\
> > `  (it "starts with some health"`{.calibre4}\
> > `    (let [shark (shark/make)]`{.calibre4}\
> > `      (should= config/shark-starting-health`{.calibre4}\
> > `               (shark/health shark))))`{.calibre4}\
> > \
> > `  (it "loses health with time"`{.calibre4}\
> > `    (let [small-world (-> (world/make 1 1)`{.calibre4}\
> > `                          (world/set-cell [0 0] (shark/make)))`{.calibre4}\
> > `          aged-world (world/tick small-world)`{.calibre4}\
> > `          aged-shark (world/get-cell aged-world [0 0])]`{.calibre4}\
> > `      (should= (dec config/shark-starting-health)`{.calibre4}\
> > `               (shark/health aged-shark)))))`{.calibre4}\
> > \
> > `—————`{.calibre4}\
> > \
> > `(ns wator.shark . . .)`{.calibre4}\
> > \
> > ]{.calibre_3}]{.calibre_17}[[`(s/def ::health int?)`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `(s/def ::shark (s/and #(= ::shark (::cell/type %))`{.calibre4}\
> > `                      ::animal/animal`{.calibre4}\
> > `                      `{.calibre4}]{.calibre_3}]{.calibre_17}[[`(s/keys :req [::health])`{.calibre4}]{.calibre_3}]{.bold}[[`))`{.calibre4}\
> > \
> > `(defn make []`{.calibre4}\
> > `  {:post [(s/valid? ::shark %)]}`{.calibre4}\
> > `  (merge {::cell/type ::shark`{.calibre4}\
> > `          `{.calibre4}]{.calibre_3}]{.calibre_17}[[`::health config/shark-starting-health}`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `         (animal/make)))`{.calibre4}\
> > \
> > ]{.calibre_3}]{.calibre_17}[[`(defn health [shark]`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `  `{.calibre4}]{.calibre_3}]{.calibre_17}[[`(::health shark))`{.calibre4}]{.calibre_3}]{.bold}[[\
> > \
> > ]{.calibre_3}]{.calibre_17}[[`(defn decrement-health [shark]`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `  `{.calibre4}]{.calibre_3}]{.calibre_17}[[`(update shark ::health dec))`{.calibre4}]{.calibre_3}]{.bold}[[\
> > \
> > `(defmethod cell/tick ::shark [shark loc world]`{.calibre4}\
> > `  (-> shark`{.calibre4}\
> > `      `{.calibre4}]{.calibre_3}]{.calibre_17}[[`(decrement-health)`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `      (animal/tick loc world))`{.calibre4}\
> > `  )`{.calibre4}\
> > \
> > `; . . .`{.calibre4}]{.calibre_3}]{.calibre_17}

Pretty easy. We just added the [` ::health `{.calibre4}]{.calibre_17} field to the [` ::shark `{.calibre4}]{.calibre_17} spec and [` shark/make `{.calibre4}]{.calibre_17}, and then we decremented the [` ::health `{.calibre4}]{.calibre_17} in the [` tick `{.calibre4}]{.calibre_17} function just before delegating the rest of the behavior to the superclass [` animal `{.calibre4}]{.calibre_17}.

Now let's test that a [` shark `{.calibre4}]{.calibre_17} will die when its [` ::health `{.calibre4}]{.calibre_17} goes to zero:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_320.html#filepos997637)

> > [[`(it "dies when health goes to zero"`{.calibre4}\
> > `      (let [sick-shark (-> (shark/make)`{.calibre4}\
> > `                           (shark/set-health 1))`{.calibre4}\
> > `            small-world (-> (world/make 1 1)`{.calibre4}\
> > `                            (world/set-cell [0 0] sick-shark))`{.calibre4}\
> > `            aged-world (world/tick small-world)`{.calibre4}\
> > `            dead-shark (world/get-cell aged-world [0 0])]`{.calibre4}\
> > `        (should (water/is? dead-shark))))`{.calibre4}\
> > \
> > `————`{.calibre4}\
> > \
> > `(ns wator.shark . . .)`{.calibre4}\
> > \
> > `(defmethod cell/tick ::shark [shark loc world]`{.calibre4}\
> > `  (if (= 1 (health shark))`{.calibre4}\
> > `    [nil {loc (water/make)}]`{.calibre4}\
> > `    (-> shark`{.calibre4}\
> > `        (decrement-health)`{.calibre4}\
> > `        (animal/tick loc world))))`{.calibre4}\
> > \
> > `; . . .`{.calibre4}]{.calibre_3}]{.calibre_17}

Pretty easy. OK, so now let's test that sharks will eat when given the opportunity:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_321.html#filepos997783)

> > [[`(it "eats when a fish is adjacent"`{.calibre4}\
> > `  (let [world (-> (world/make 2 1)`{.calibre4}\
> > `                  (world/set-cell [0 0] (fish/make))`{.calibre4}\
> > `                  (world/set-cell [1 0] (shark/make)))`{.calibre4}\
> > `        shark-ate-world (world/tick world)`{.calibre4}\
> > `        full-shark (world/get-cell shark-ate-world [0 0])`{.calibre4}\
> > `        where-shark-was (world/get-cell shark-ate-world [1 0])`{.calibre4}\
> > `        expected-health (+ config/shark-starting-health`{.calibre4}\
> > `                           config/shark-eating-health`{.calibre4}\
> > `                           -1)]`{.calibre4}\
> > `    (should (shark/is? full-shark))`{.calibre4}\
> > `    (should (water/is? where-shark-was))`{.calibre4}\
> > `    (should= expected-health (shark/health full-shark))))`{.calibre4}]{.calibre_3}]{.calibre_17}

We create a 2-by-1 [` world `{.calibre4}]{.calibre_17} with a [` shark `{.calibre4}]{.calibre_17} next to a [` fish `{.calibre4}]{.calibre_17}. After one [` tick `{.calibre4}]{.calibre_17}, the [` shark `{.calibre4}]{.calibre_17} should be where the [` fish `{.calibre4}]{.calibre_17} was, and [` water `{.calibre4}]{.calibre_17} should be where the [` shark `{.calibre4}]{.calibre_17} was, and the [` shark `{.calibre4}]{.calibre_17}'s [` ::health `{.calibre4}]{.calibre_17} should have increased.

Getting this to pass forced me to abandon the delegation to [` animal/tick `{.calibre4}]{.calibre_17} because a [` shark `{.calibre4}]{.calibre_17} should try to [` reproduce `{.calibre4}]{.calibre_17} first, then try to [` eat `{.calibre4}]{.calibre_17} next, and then finally try to [` move `{.calibre4}]{.calibre_17}:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_322.html#filepos997929)

> > [[`(ns wator.shark . . .)`{.calibre4}\
> > \
> > `(defn eat [shark loc world]`{.calibre4}\
> > `  (let [neighbors (world/neighbors world loc)`{.calibre4}\
> > `        fishy-neighbors (filter #(fish/is?`{.calibre4}\
> > `                                  (world/get-cell world %))`{.calibre4}\
> > `                                neighbors)]`{.calibre4}\
> > `    (if (empty? fishy-neighbors)`{.calibre4}\
> > `      nil`{.calibre4}\
> > `      [{loc (water/make)}`{.calibre4}\
> > `       {(rand-nth fishy-neighbors) (feed shark)}]))`{.calibre4}\
> > `  )`{.calibre4}\
> > \
> > `(defmethod cell/tick ::shark [shark loc world]`{.calibre4}\
> > `  (if (= 1 (health shark))`{.calibre4}\
> > `    [nil {loc (water/make)}]`{.calibre4}\
> > `    (let [aged-shark (-> shark`{.calibre4}\
> > `                         (animal/increment-age)`{.calibre4}\
> > `                         (decrement-health))]`{.calibre4}\
> > `      (if-let [reproduction (animal/reproduce`{.calibre4}\
> > `                              aged-shark loc world)]`{.calibre4}\
> > `        reproduction`{.calibre4}\
> > `        (if-let [eaten (eat aged-shark loc world)]`{.calibre4}\
> > `          eaten`{.calibre4}\
> > `          (animal/move aged-shark loc world))))))`{.calibre4}]{.calibre_3}]{.calibre_17}

All this slipped in with little hassle. We've passed through the design bottleneck and are now reaping the benefits.

The modelers told us that a shark will only reproduce if its health is above a threshold. Let's test that. In fact, let's make that change first[]{#index_split_034.html#filepos811500}[[[[18]{.underline}]{.calibre_10}]{.calibre3}](#index_split_034.html#filepos811624) and see which tests break:

[[[18]{.underline}]{.calibre_10}](#index_split_034.html#filepos811500). TDD VIOLATION! ALERT! ALERT!

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_323.html#filepos998075)

> > [[`(ns wator.shark . . .)`{.calibre4}\
> > \
> > `(defmethod animal/reproduce ::shark [shark loc world]`{.calibre4}\
> > `  `{.calibre4}]{.calibre_3}]{.calibre_17}[[`(if (>= (health shark) config/shark-reproduction-health)`{.calibre4}]{.calibre_3}]{.bold}[[\
> > `    (animal/do-reproduce shark loc world)`{.calibre4}\
> > `    `{.calibre4}]{.calibre_3}]{.calibre_17}[[`nil`{.calibre4}]{.calibre_3}]{.bold}[[`))`{.calibre4}]{.calibre_3}]{.calibre_17}

As expected, the test for animal reproduction fails in the shark scenario. We can address this by putting a little hack in that test:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_324.html#filepos998221)

> > [[`(it "reproduces"`{.calibre4}\
> > `  (doseq [scenario [{:constructor fish/make :tester fish/is?}`{.calibre4}\
> > `                    {:constructor`{.calibre4}\
> > `                       #(-> (shark/make)`{.calibre4}\
> > `                            (shark/set-health`{.calibre4}\
> > `                              (inc config/shark-reproduction-`{.calibre4}\
> > `                                   health)))`{.calibre4}\
> > `                     :tester shark/is?}]]`{.calibre4}\
> > \
> > `; . . .`{.calibre4}]{.calibre_3}]{.calibre_17}

Yes, that's a bit ugly, but it does the job. I suppose I should add a test for checking the other side of that threshold:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_325.html#filepos998367)

> > [[`(it "doesn't reproduce if not healthy enough"`{.calibre4}\
> > `  (let [shark (-> (shark/make)`{.calibre4}\
> > `                  (shark/set-health`{.calibre4}\
> > `                    (dec config/shark-reproduction-health))`{.calibre4}\
> > `                  (animal/set-age config/shark-reproduction-age))`{.calibre4}\
> > `        world (-> (world/make 3 3)`{.calibre4}\
> > `                  (world/set-cell [1 1] shark))`{.calibre4}\
> > `        failed (animal/reproduce shark [1 1] world)]`{.calibre4}\
> > `    (should-be-nil failed)))`{.calibre4}]{.calibre_3}]{.calibre_17}

OK. One last thing. The health of the parent shark is split between the two daughter sharks:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_326.html#filepos998513)

> > [[`(it "shares health with both daughters after reproduction"`{.calibre4}\
> > `  (let [initial-health (inc config/shark-reproduction-health)`{.calibre4}\
> > `        pregnant-shark (-> (shark/make)`{.calibre4}\
> > `                           (animal/set-age`{.calibre4}\
> > `                             (inc config/shark-reproduction-age))`{.calibre4}\
> > `                           (shark/set-health initial-health))`{.calibre4}\
> > `        world (-> (world/make 2 1)`{.calibre4}\
> > `                  (world/set-cell [0 0] pregnant-shark))`{.calibre4}\
> > `        new-world (world/tick world)`{.calibre4}\
> > `        daughter1 (world/get-cell new-world [0 0])`{.calibre4}\
> > `        daughter2 (world/get-cell new-world [1 0])`{.calibre4}\
> > `        expected-health (quot (dec initial-health) 2)]`{.calibre4}\
> > `    (should (shark/is? daughter1))`{.calibre4}\
> > `    (should (shark/is? daughter2))`{.calibre4}\
> > `    (should= expected-health (shark/health daughter1))`{.calibre4}\
> > `    (should= expected-health (shark/health daughter2))))`{.calibre4}]{.calibre_3}]{.calibre_17}

Yup. That fails because the expected health isn't correct. That should be simple to fix:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_327.html#filepos998659)

> > [[`(ns wator.shark . . .)`{.calibre4}\
> > \
> > `(defmethod animal/reproduce ::shark [shark loc world]`{.calibre4}\
> > `  (if (< (health shark) config/shark-reproduction-health)`{.calibre4}\
> > `    nil`{.calibre4}\
> > `    (if-let [reproduction (animal/do-reproduce shark loc world)]`{.calibre4}\
> > `      (let [[from to] reproduction`{.calibre4}\
> > `            from-loc (-> from keys first)`{.calibre4}\
> > `            to-loc (-> to keys first)`{.calibre4}\
> > `            daughter-health (quot (health shark) 2)`{.calibre4}\
> > `            from-shark (-> from vals first`{.calibre4}\
> > `                           (set-health daughter-health))`{.calibre4}\
> > `            to-shark (-> to vals first`{.calibre4}\
> > `                         (set-health daughter-health))]`{.calibre4}\
> > `        [{from-loc from-shark} {to-loc to-shark}])`{.calibre4}\
> > `      nil)))`{.calibre4}]{.calibre_3}]{.calibre_17}

And with that, I think the model is complete. Let's see if we can put a GUI on top of it:

[[[[Click here to view code image]{.underline}]{.calibre_10}]{.calibre3}](#index_split_328.html#filepos998805)

> > [[`(ns wator-gui.main`{.calibre4}\
> > `  (:require [quil.core :as q]`{.calibre4}\
> > `            [quil.middleware :as m]`{.calibre4}\
> > `            [wator`{.calibre4}\
> > `             [world :as world]`{.calibre4}\
> > `             [water :as water]`{.calibre4}\
> > `             [fish :as fish]`{.calibre4}\
> > `             [shark :as shark]`{.calibre4}\
> > `             [world-imp]`{.calibre4}\
> > `             [water-imp]`{.calibre4}\
> > `             [fish-imp]]))`{.calibre4}\
> > \
> > `(defn setup []`{.calibre4}\
> > `  (q/frame-rate 60)`{.calibre4}\
> > `  (q/color-mode :rgb)`{.calibre4}\
> > `  (-> (world/make 80 80)`{.calibre4}\
> > `      (world/set-cell [40 40] (fish/make)))`{.calibre4}\
> > `  )`{.calibre4}\
> > \
> > `(defn update-state [world]`{.calibre4}\
> > `  (world/tick world))`{.calibre4}\
> > `(defn draw-state [world]`{.calibre4}\
> > `  (q/background 240)`{.calibre4}\
> > `  (let [cells (::world/cells world)]`{.calibre4}\
> > `    (doseq [loc (keys cells)]`{.calibre4}\
> > `      (let [[x y] loc`{.calibre4}\
> > `            cell (get cells loc)`{.calibre4}\
> > `            x (* 12 x)`{.calibre4}\
> > `            y (* 12 y)`{.calibre4}\
> > `            color (cond`{.calibre4}\
> > `                    (water/is? cell) [255 255 255]`{.calibre4}\
> > `                    (fish/is? cell) [0 0 255]`{.calibre4}\
> > `                    (shark/is? cell) [255 0 0])]`{.calibre4}\
> > `        (q/no-stroke)`{.calibre4}\
> > `        (apply q/fill color)`{.calibre4}\
> > `        (q/rect x y 11 11)))))`{.calibre4}\
> > \
> > `(declare wator)`{.calibre4}\
> > \
> > `(defn ^:export -main [& args]`{.calibre4}\
> > `  (q/defsketch wator`{.calibre4}\
> > `               :title "Wator"`{.calibre4}\
> > `               :size [960 960]`{.calibre4}\
> > `               :setup setup`{.calibre4}\
> > `               :update update-state`{.calibre4}\
> > `               :draw draw-state`{.calibre4}\
> > `               :features [:keep-on-top]`{.calibre4}\
> > `               :middleware [m/fun-mode])`{.calibre4}\
> > \
> > `  args)`{.calibre4}]{.calibre_3}]{.calibre_17}
>
> []{#index_split_034.html#filepos820245}

Yeah, that wasn't too hard. [[[Figure 17.7]{.underline}]{.calibre_10}](#index_split_034.html#filepos820815) is a screenshot of the game in progress.

It's not super-fast; but that's not a big surprise. There are a bunch of things we could do to speed it up. But never mind that. Look at that GUI code. It depends on the model, yet the model knows nothing of the GUI. And that satisfies our original architectural goal.

![](images/00220.jpg){#filepos820815 .calibre_96}

[[Figure 17.7.]{.bold}]{.calibre3}[ Screenshot of Wa-Tor in progress]{.calibre3}

[[[Conclusion]{.calibre_3}]{.bold}]{.calibre1}

Wa-Tor is a program that is "functional"[]{#index_split_034.html#filepos821228}[[[[19]{.underline}]{.calibre_10}]{.calibre3}](#index_split_034.html#filepos821491) and object oriented; complete with several OO design patterns right out of the GOF book. Indeed, it was the OO partitioning that helped the design congeal so nicely.

[[[19]{.underline}]{.calibre_10}](#index_split_034.html#filepos821228). Why the quotes? Because random numbers aren't referentially transparent, so this program is not purely functional.

The OO partitioning separates and isolates the various data types very nicely, and it provides pleasant locations for the related functions. Any OO programmer would be very comfortable with this.

However, at its heart, this is a data flow model. The [` world `{.calibre4}]{.calibre_17} flows through the behaviors in the various objects, without any mutation. The plumbing model of functional programming still holds.

Is this a hybrid approach? Have we created an unholy alliance. . . a Frankenstein's Monster of a program?

I think not. Indeed, I think this combination of approaches is entirely natural and very beneficial. Data is encapsulated and immutable. Behavior is associated with the data it operates on. And yet the data elements flow through the behaviors as opposed to the behaviors iterating over the data.

In the end, I think this is the way software was meant to be.

By the way, you can find all the source code at [[[https://github.com/unclebob/wator]{.underline}]{.calibre_10}](https://github.com/unclebob/wator).

::: {#index_split_034.html#calibre_pb_34 .mbp_pagebreak}
:::

[]{#index_split_035.html}

[[[Afterword]{.calibre_3}]{.bold}]{.calibre1}

In March 2022, I attended a friend's birthday party where I overheard a couple of guys bantering about code. I introduced myself---I was in the market for some coding friends. Once we'd gotten the obvious exchanges of small talk out of the way, one of them dropped a bomb of a question on me.

He asked, "So, what's your preferred stack?"

All the little bits in my brain frantically searched for an answer while I was simultaneously trying to understand what he was asking me, until finally I very unconfidently answered, "Clojure?"

With a step back and obvious surprise, he exclaimed, "Really?! Like full-stack?"

\[Confetti drops in my brain---nailed it!\]

In shock, he continued . . . "Front end and back end all in Clojure? I've never heard of that before. How does that work? Clojure is a Lisp language, right? It's functional."

Yes, it is, but [Oh no! Another question . . . "How does that work?"]{.italic}

Well, if you're reading this, then I assume you've read the preceding pages and thus have already received a much better and more elaborate explanation than I could offer you here, so let's address the elephant in the room: Why was asking me my preferred stack a bomb of a question?

Almost exactly 11 years prior to this birthday party, I began my career as a chemical engineer and a union scab in Metropolis, IL, where I was trained to operate processes and equipment in the manufacturing of uranium hexafluoride. Over the next ten years, I progressed my career into production leadership of various chemical manufacturing plants.

Across that decade, I learned a lot about procedures, state, people, corporate culture, and broken processes for which I lacked the skills to fix. Then, in March 2020, as I was balancing demands based on said broken processes with overwhelming life changes, the world as we knew it shut down. For eight weeks, I suddenly found myself in the near-constant presence of someone whom I knew not only had the skills I lacked, but had developed the rules for mastering those skills.

So I asked my dad, or as you might know him, "Uncle Bob," what it would take to learn software to the depths necessary to fix those problems I so desperately wanted to fix.

That evening he showed me one of his current projects---an automated daily chart on COVID-19 infections and deaths by county. When I didn't recognize the syntax, he took the opportunity to tell me about Clojure.

I immediately had questions because I'd only ever known the basics of languages like Java and Python. He explained the basic differences of OO procedural languages and functional languages and why he liked Clojure. In one example, he showed me why functional languages are "safer" and less complicated than those that rely heavily on mutable states by depicting a race condition for me that was almost identical to that of the phone call between Bob and Alice found in [[[Chapter 15]{.underline}]{.calibre_10}](#index_split_030.html#filepos534355).

Then we dove into the code, and he allowed me an opportunity that I do not take lightly: to work with him on his COVID chart. I mostly just wrote a few basic arithmetic functions (after we wrote tests for those, of course).

He walked me through Quil too, and how even it was mostly functional and how instead of changing a state, it simply recurred a new state at each iteration. This went a little over my head at the time, but I fell back on this conversation a lot over the next year---I even have in front of me right now the printout of the source code we'd written that night as inspiration for writing this.

A little over a year later, I "graduated" from my software apprenticeship and became a full-time developer for Clean Coders Studio.

So, back to the elephant: As of March 2022, I was still pretty new to software; due to COVID-19, there hadn't been many large-group events that had taken place yet; and because Baton Rouge, LA, has some opportunity for growth in the software sector, I had been pretty isolated as a developer and had experienced little exposure to common industry lingo.

That birthday party offered me my first live interaction with a fellow developer outside of Clean Coders, and when I was asked my preferred stack, I had only enough knowledge to translate and puzzle together the question. And it was a bomb of a question because I wasn't confident that I had all the pieces.

With that out of the way, I'll leave you with two final tidbits.

::: calibre_11
 
:::

1.  The real-life moment Clojure blew my mind was when we were working on a project that built off a Java project that used Angular for the front end. When implementing anything in Angular, we of course had to test and create almost identical methods in Angular and Java (and sometimes in Clojure, as we were migrating a legacy system). Double work everywhere!

    > Then they asked for a mobile application using all the same functionality as our Clojure features. We extracted much of the core functionality into a [` cljc `{.calibre4}]{.calibre_17} library, and from there we were able to build the mobile app with little to no code duplication or rewrites.

    > We used common functions for the [` cljs `{.calibre4}]{.calibre_17} mobile application, as we did for the back end, by utilizing Clojure common namespaces.

    > In how many languages can you say you've done that---had the back end and, potentially, multiple front ends all functioning on the same, simultaneously tested code?

2.  This got me, as I've seen it get others, and if you're used to OO it will probably get you. [` for `{.calibre4}]{.calibre_17} in Clojure is not a loop. It is a list comprehension macro, and it does not force side effects. Instead, use [` doseq `{.calibre4}]{.calibre_17}, which returns [` nil `{.calibre4}]{.calibre_17} but will accomplish what you are incorrectly trying to achieve with [` for `{.calibre4}]{.calibre_17}.

Good luck!

---Gina Martiny, Clean Coders

::: {#index_split_035.html#calibre_pb_35 .mbp_pagebreak}
:::

[]{#index_split_036.html}

[[[Index]{.calibre_3}]{.bold}]{.calibre1}

[Page numbers with "n" indicate footnotes]{.italic}.

[[[Symbols]{.calibre_3}]{.bold}]{.calibre1}

::: calibre_11
 
:::

-   [` : `{.calibre4}]{.calibre_17} (colon), [[[112]{.underline}]{.calibre_10}](#index_split_023.html#filepos303219)

-   [` #(…) `{.calibre4}]{.calibre_17} form, [[[73]{.underline}]{.calibre_10}](#index_split_020.html#filepos215186)n5

-   [` #{…} `{.calibre4}]{.calibre_17} form, [[[88]{.underline}]{.calibre_10}](#index_split_021.html#filepos245883)n

-   [` :post `{.calibre4}]{.calibre_17} feature, [[[113]{.underline}]{.calibre_10}](#index_split_023.html#filepos305961)--[[[114]{.underline}]{.calibre_10}](#index_split_023.html#filepos309309), [[[256]{.underline}]{.calibre_10}](#index_split_032.html#filepos622333)

-   [` :pre `{.calibre4}]{.calibre_17} feature, [[[113]{.underline}]{.calibre_10}](#index_split_023.html#filepos305961)--[[[114]{.underline}]{.calibre_10}](#index_split_023.html#filepos309309), [[[256]{.underline}]{.calibre_10}](#index_split_032.html#filepos622333)

-   [` […] `{.calibre4}]{.calibre_17} (square brackets), [[[29]{.underline}]{.calibre_10}](#index_split_015.html#filepos108534)n

-   [` ->> `{.calibre4}]{.calibre_17} (threading macro), [[[45]{.underline}]{.calibre_10}](#index_split_017.html#filepos145812), [[[46]{.underline}]{.calibre_10}](#index_split_017.html#filepos149963)

[[[A]{.calibre_3}]{.bold}]{.calibre1}

::: calibre_11
 
:::

-   Abstract Factory pattern

    -   shape example, [[[276]{.underline}]{.calibre_10}](#index_split_032.html#filepos670446)--[[[281]{.underline}]{.calibre_10}](#index_split_032.html#filepos684329)

    -   usage, [[[271]{.underline}]{.calibre_10}](#index_split_032.html#filepos658766), [[[276]{.underline}]{.calibre_10}](#index_split_032.html#filepos670446)

-   Abstract Server pattern

    -   in switch and light problem, [[[233]{.underline}]{.calibre_10}](#index_split_032.html#filepos568776)--[[[236]{.underline}]{.calibre_10}](#index_split_032.html#filepos575468)

    -   usage, [[[230]{.underline}]{.calibre_10}](#index_split_032.html#filepos561193)--[[[231]{.underline}]{.calibre_10}](#index_split_032.html#filepos564613)

-   access points, [[[150]{.underline}]{.calibre_10}](#index_split_026.html#filepos390014)

-   actors, [[[127]{.underline}]{.calibre_10}](#index_split_026.html#filepos331947), [[[129]{.underline}]{.calibre_10}](#index_split_026.html#filepos336595), [[[288]{.underline}]{.calibre_10}](#index_split_034.html#filepos691974)--[[[289]{.underline}]{.calibre_10}](#index_split_034.html#filepos694682)

-   Adapter pattern

    -   forms, [[[231]{.underline}]{.calibre_10}](#index_split_032.html#filepos564613)--[[[233]{.underline}]{.calibre_10}](#index_split_032.html#filepos568776), [[[240]{.underline}]{.calibre_10}](#index_split_032.html#filepos585587)--[[[242]{.underline}]{.calibre_10}](#index_split_032.html#filepos591043)

    -   in switch and light problem, [[[236]{.underline}]{.calibre_10}](#index_split_032.html#filepos575468)--[[[240]{.underline}]{.calibre_10}](#index_split_032.html#filepos585587)

-   [Advanced C++ Programming Styles and Idioms]{.italic} (Coplien), [[[250]{.underline}]{.calibre_10}](#index_split_032.html#filepos607406)n

-   Advent of Code 2022 problem

    -   Clojure solution, [[[121]{.underline}]{.calibre_10}](#index_split_025.html#filepos320339)--[[[123]{.underline}]{.calibre_10}](#index_split_025.html#filepos324257)

    -   description, [[[118]{.underline}]{.calibre_10}](#index_split_025.html#filepos312918)--[[[119]{.underline}]{.calibre_10}](#index_split_025.html#filepos316270)

    -   [` Java `{.calibre4}]{.calibre_17} solution, [[[119]{.underline}]{.calibre_10}](#index_split_025.html#filepos316270)--[[[121]{.underline}]{.calibre_10}](#index_split_025.html#filepos320339)

-   [` agent `{.calibre4}]{.calibre_17}, [[[220]{.underline}]{.calibre_10}](#index_split_030.html#filepos543931)

-   [Agile Software Development: Principles, Patterns, and Practices]{.italic} (Martin), [[[53]{.underline}]{.calibre_10}](#index_split_018.html#filepos165870), [[[96]{.underline}]{.calibre_10}](#index_split_022.html#filepos263307), [[[126]{.underline}]{.calibre_10}](#index_split_026.html#filepos329228), [[[184]{.underline}]{.calibre_10}](#index_split_028.html#filepos462905)n, [[[231]{.underline}]{.calibre_10}](#index_split_032.html#filepos564613)n4, [[[243]{.underline}]{.calibre_10}](#index_split_032.html#filepos592355)

-   architectural boundaries

    -   maintaining OCP across, [[[281]{.underline}]{.calibre_10}](#index_split_032.html#filepos684329)

    -   in Payroll example, [[[98]{.underline}]{.calibre_10}](#index_split_022.html#filepos267992), [[[100]{.underline}]{.calibre_10}](#index_split_022.html#filepos271500), [[[105]{.underline}]{.calibre_10}](#index_split_022.html#filepos286904)

    -   in shape example, [[[271]{.underline}]{.calibre_10}](#index_split_032.html#filepos658766), [[[273]{.underline}]{.calibre_10}](#index_split_032.html#filepos665792), [[[275]{.underline}]{.calibre_10}](#index_split_032.html#filepos668351)--[[[276]{.underline}]{.calibre_10}](#index_split_032.html#filepos670446)

    -   in Wa-Tor app, [[[289]{.underline}]{.calibre_10}](#index_split_034.html#filepos694682), [[[312]{.underline}]{.calibre_10}](#index_split_034.html#filepos752976)--[[[313]{.underline}]{.calibre_10}](#index_split_034.html#filepos755611)

-   architecture. [See]{.italic}
    > [[[Dependency Rule of Clean Architecture]{.underline}]{.calibre_10}](#index_split_036.html#filepos865214)

-   arrays

    -   and [n]{.italic}-ary trees, [[[23]{.underline}]{.calibre_10}](#index_split_014.html#filepos100426)--[[[25]{.underline}]{.calibre_10}](#index_split_014.html#filepos104091)

    -   in Sieve of Eratosthenes algorithm, [[[20]{.underline}]{.calibre_10}](#index_split_014.html#filepos94430)--[[[22]{.underline}]{.calibre_10}](#index_split_014.html#filepos99056)

-   assignment

    -   defined, [[[7]{.underline}]{.calibre_10}](#index_split_013.html#filepos68020)--[[[8]{.underline}]{.calibre_10}](#index_split_013.html#filepos70428)

    -   programming without, [[[4]{.underline}]{.calibre_10}](#index_split_013.html#filepos61537)--[[[6]{.underline}]{.calibre_10}](#index_split_013.html#filepos66018), [[[20]{.underline}]{.calibre_10}](#index_split_014.html#filepos94430)--[[[22]{.underline}]{.calibre_10}](#index_split_014.html#filepos99056)

-   [` assoc `{.calibre4}]{.calibre_17}, [[[90]{.underline}]{.calibre_10}](#index_split_021.html#filepos250704)n5

-   [` async/>!! `{.calibre4}]{.calibre_17} function, [[[213]{.underline}]{.calibre_10}](#index_split_029.html#filepos533449)

-   [` async/go `{.calibre4}]{.calibre_17} function, [[[205]{.underline}]{.calibre_10}](#index_split_029.html#filepos513381)

-   [` atom `{.calibre4}]{.calibre_17} (atomic value), [[[50]{.underline}]{.calibre_10}](#index_split_017.html#filepos161108)--[[[51]{.underline}]{.calibre_10}](#index_split_017.html#filepos163544)

-   atomic operations, [[[50]{.underline}]{.calibre_10}](#index_split_017.html#filepos161108)

[[[B]{.calibre_3}]{.bold}]{.calibre1}

::: calibre_11
 
:::

-   batch vs. interactive applications, [[[44]{.underline}]{.calibre_10}](#index_split_017.html#filepos143664)

-   behavioral cohesion, [[[94]{.underline}]{.calibre_10}](#index_split_021.html#filepos261948), [[[336]{.underline}]{.calibre_10}](#index_split_034.html#filepos821960)

-   binary trees. [See]{.italic}
    > [[[[n]{.underline}]{.calibre_10}]{.italic}[[-ary trees]{.underline}]{.calibre_10}](#index_split_036.html#filepos905772)

-   Bowling Game problem

    -   Clojure version, [[[71]{.underline}]{.calibre_10}](#index_split_020.html#filepos208585)--[[[75]{.underline}]{.calibre_10}](#index_split_020.html#filepos222018)

    -   comparison of solutions, [[[75]{.underline}]{.calibre_10}](#index_split_020.html#filepos222018)--[[[76]{.underline}]{.calibre_10}](#index_split_020.html#filepos224096)

    -   Java version, [[[66]{.underline}]{.calibre_10}](#index_split_020.html#filepos195655)--[[[71]{.underline}]{.calibre_10}](#index_split_020.html#filepos208585)

-   business rules

    -   and dependencies, [[[154]{.underline}]{.calibre_10}](#index_split_026.html#filepos399777)--[[[155]{.underline}]{.calibre_10}](#index_split_026.html#filepos402079)

    -   tests, [[[127]{.underline}]{.calibre_10}](#index_split_026.html#filepos331947)--[[[131]{.underline}]{.calibre_10}](#index_split_026.html#filepos342014)

[[[C]{.calibre_3}]{.bold}]{.calibre1}

::: calibre_11
 
:::

-   cathode ray tubes (CRTs), [[[118]{.underline}]{.calibre_10}](#index_split_025.html#filepos312918)

-   change requests and Single Responsibility Principle, [[[126]{.underline}]{.calibre_10}](#index_split_026.html#filepos329228)--[[[131]{.underline}]{.calibre_10}](#index_split_026.html#filepos342014)

-   Church, Alonzo, [[[xvi]{.underline}]{.calibre_10}](#index_split_009.html#filepos46603)--[[[xvii]{.underline}]{.calibre_10}](#index_split_009.html#filepos48837)

-   Church-Turing thesis, [[[xvi]{.underline}]{.calibre_10}](#index_split_009.html#filepos46603)--[[[xvii]{.underline}]{.calibre_10}](#index_split_009.html#filepos48837), [[[19]{.underline}]{.calibre_10}](#index_split_014.html#filepos92254)

-   classes

    -   closed, [[[267]{.underline}]{.calibre_10}](#index_split_032.html#filepos649292), [[[273]{.underline}]{.calibre_10}](#index_split_032.html#filepos665792)

    -   and interfaces, [[[132]{.underline}]{.calibre_10}](#index_split_026.html#filepos344090), [[[283]{.underline}]{.calibre_10}](#index_split_032.html#filepos688480)--[[[284]{.underline}]{.calibre_10}](#index_split_032.html#filepos690920)

    -   vs. namespaces, [[[107]{.underline}]{.calibre_10}](#index_split_022.html#filepos292047)

-   [Clean Architecture]{.italic} (Martin), [[[96]{.underline}]{.calibre_10}](#index_split_022.html#filepos263307), [[[126]{.underline}]{.calibre_10}](#index_split_026.html#filepos329228)

-   Cleancoders, [[[126]{.underline}]{.calibre_10}](#index_split_026.html#filepos329228), [[[213]{.underline}]{.calibre_10}](#index_split_029.html#filepos533449)

-   [Clean Craftsmanship]{.italic} (Martin), [[[53]{.underline}]{.calibre_10}](#index_split_018.html#filepos165870), [[[79]{.underline}]{.calibre_10}](#index_split_021.html#filepos229830)n

-   Clojure

    -   and classes, [[[267]{.underline}]{.calibre_10}](#index_split_032.html#filepos649292)

    -   compiling, [[[137]{.underline}]{.calibre_10}](#index_split_026.html#filepos357661), [[[150]{.underline}]{.calibre_10}](#index_split_026.html#filepos390014), [[[256]{.underline}]{.calibre_10}](#index_split_032.html#filepos622333)n, [[[300]{.underline}]{.calibre_10}](#index_split_034.html#filepos723410)

    -   features and constraints, [[[41]{.underline}]{.calibre_10}](#index_split_016.html#filepos138979), [[[281]{.underline}]{.calibre_10}](#index_split_032.html#filepos684329), [[[282]{.underline}]{.calibre_10}](#index_split_032.html#filepos687147)--[[[284]{.underline}]{.calibre_10}](#index_split_032.html#filepos690920)

    -   interface segregation, [[[149]{.underline}]{.calibre_10}](#index_split_026.html#filepos388474)--[[[150]{.underline}]{.calibre_10}](#index_split_026.html#filepos390014)

    -   keyword syntax, [[[45]{.underline}]{.calibre_10}](#index_split_017.html#filepos145812)n

    -   on learning, [[[xvii]{.underline}]{.calibre_10}](#index_split_009.html#filepos48837)--[[[xviii]{.underline}]{.calibre_10}](#index_split_009.html#filepos51769)

    -   namespaces and source files, [[[107]{.underline}]{.calibre_10}](#index_split_022.html#filepos292047)--[[[108]{.underline}]{.calibre_10}](#index_split_022.html#filepos294299)

    -   source code dependency, [[[104]{.underline}]{.calibre_10}](#index_split_022.html#filepos284663)--[[[105]{.underline}]{.calibre_10}](#index_split_022.html#filepos286904)

    -   syntax overview, [[[29]{.underline}]{.calibre_10}](#index_split_015.html#filepos108534)--[[[32]{.underline}]{.calibre_10}](#index_split_015.html#filepos118882)

-   [` clojure.spec `{.calibre4}]{.calibre_17} library, [[[47]{.underline}]{.calibre_10}](#index_split_017.html#filepos153273), [[[110]{.underline}]{.calibre_10}](#index_split_023.html#filepos296903)

-   cogency, [[[151]{.underline}]{.calibre_10}](#index_split_026.html#filepos392701)

-   cohesion, [[[94]{.underline}]{.calibre_10}](#index_split_021.html#filepos261948)

-   Command pattern

    -   Undo variation, [[[245]{.underline}]{.calibre_10}](#index_split_032.html#filepos596823)--[[[249]{.underline}]{.calibre_10}](#index_split_032.html#filepos605382)

    -   usage, [[[242]{.underline}]{.calibre_10}](#index_split_032.html#filepos591043)--[[[245]{.underline}]{.calibre_10}](#index_split_032.html#filepos596823)

-   compare-and-swap protocol, [[[48]{.underline}]{.calibre_10}](#index_split_017.html#filepos155572)--[[[51]{.underline}]{.calibre_10}](#index_split_017.html#filepos163544)

-   comp.object (social network), [[[230]{.underline}]{.calibre_10}](#index_split_032.html#filepos561193)

-   Composite pattern

    -   shape example, [[[254]{.underline}]{.calibre_10}](#index_split_032.html#filepos616793)--[[[259]{.underline}]{.calibre_10}](#index_split_032.html#filepos629815)

    -   in switch and light problem, [[[249]{.underline}]{.calibre_10}](#index_split_032.html#filepos605382)--[[[254]{.underline}]{.calibre_10}](#index_split_032.html#filepos616793)

-   [` concat `{.calibre4}]{.calibre_17} function, [[[73]{.underline}]{.calibre_10}](#index_split_020.html#filepos215186)

-   constants, and functional programs, [[[16]{.underline}]{.calibre_10}](#index_split_013.html#filepos89440)

-   Coplien, Jim, [Advanced C++ Programming Styles and Idioms]{.italic}, [[[250]{.underline}]{.calibre_10}](#index_split_032.html#filepos607406)

-   copy example

    -   in C, [[[131]{.underline}]{.calibre_10}](#index_split_026.html#filepos342014)--[[[132]{.underline}]{.calibre_10}](#index_split_026.html#filepos344090)

    -   in Clojure, [[[133]{.underline}]{.calibre_10}](#index_split_026.html#filepos346402)--[[[136]{.underline}]{.calibre_10}](#index_split_026.html#filepos355413)

-   copy-making, [[[20]{.underline}]{.calibre_10}](#index_split_014.html#filepos94430)--[[[22]{.underline}]{.calibre_10}](#index_split_014.html#filepos99056)

-   coupling

    -   avoidance with laziness, [[[41]{.underline}]{.calibre_10}](#index_split_016.html#filepos138979)--[[[42]{.underline}]{.calibre_10}](#index_split_016.html#filepos141075)

    -   in Bowling Game, [[[76]{.underline}]{.calibre_10}](#index_split_020.html#filepos224096)

    -   temporal, [[[8]{.underline}]{.calibre_10}](#index_split_013.html#filepos70428)--[[[10]{.underline}]{.calibre_10}](#index_split_013.html#filepos76132)

    -   and testing, [[[166]{.underline}]{.calibre_10}](#index_split_026.html#filepos426907)

-   CRT. [See]{.italic}
    > [[[cathode ray tubes (CRTs)]{.underline}]{.calibre_10}](#index_split_036.html#filepos846513)

-   [` cycle `{.calibre4}]{.calibre_17}, [[[90]{.underline}]{.calibre_10}](#index_split_021.html#filepos250704)n6

[[[D]{.calibre_3}]{.bold}]{.calibre1}

::: calibre_11
 
:::

-   Dahl, Ole-Johan, [[[78]{.underline}]{.calibre_10}](#index_split_021.html#filepos226973), [[[153]{.underline}]{.calibre_10}](#index_split_026.html#filepos396387)

-   data cohesion, [[[94]{.underline}]{.calibre_10}](#index_split_021.html#filepos261948), [[[96]{.underline}]{.calibre_10}](#index_split_022.html#filepos263307), [[[336]{.underline}]{.calibre_10}](#index_split_034.html#filepos821960)

-   data flow. [See also]{.italic}
    > [[[Advent of Code 2022 problem]{.underline}]{.calibre_10}](#index_split_036.html#filepos837699)

    -   in command line shells, [[[123]{.underline}]{.calibre_10}](#index_split_025.html#filepos324257)

    -   as programming style, [[[118]{.underline}]{.calibre_10}](#index_split_025.html#filepos312918), [[[124]{.underline}]{.calibre_10}](#index_split_025.html#filepos327739)

-   data flow diagrams (DFDs), examples, [[[99]{.underline}]{.calibre_10}](#index_split_022.html#filepos270077)

-   data structures. [See also]{.italic}
    > [[[[n]{.underline}]{.calibre_10}]{.italic}[[-ary trees]{.underline}]{.calibre_10}](#index_split_036.html#filepos905772)

    -   persistent, [[[25]{.underline}]{.calibre_10}](#index_split_014.html#filepos104091)

-   deadly embrace (aka deadlock), [[[49]{.underline}]{.calibre_10}](#index_split_017.html#filepos158106)

-   [` declare `{.calibre4}]{.calibre_17} function, [[[35]{.underline}]{.calibre_10}](#index_split_015.html#filepos126924)

-   Decorator pattern

    -   shape example, [[[260]{.underline}]{.calibre_10}](#index_split_032.html#filepos630536)--[[[263]{.underline}]{.calibre_10}](#index_split_032.html#filepos638276)

    -   usage, [[[260]{.underline}]{.calibre_10}](#index_split_032.html#filepos630536), [[[264]{.underline}]{.calibre_10}](#index_split_032.html#filepos641681)

-   [` def `{.calibre4}]{.calibre_17} form, [[[39]{.underline}]{.calibre_10}](#index_split_016.html#filepos132376)

-   [` defmulti `{.calibre4}]{.calibre_17}, [[[103]{.underline}]{.calibre_10}](#index_split_022.html#filepos280090)

-   dependencies

    -   source code and runtime, [[[152]{.underline}]{.calibre_10}](#index_split_026.html#filepos395094)--[[[155]{.underline}]{.calibre_10}](#index_split_026.html#filepos402079)

    -   source code inversion, [[[104]{.underline}]{.calibre_10}](#index_split_022.html#filepos284663)--[[[105]{.underline}]{.calibre_10}](#index_split_022.html#filepos286904)

-   Dependency Inversion Principle (DIP)

    -   and shape example, [[[274]{.underline}]{.calibre_10}](#index_split_032.html#filepos666748)

    -   source code and run time dependency, [[[152]{.underline}]{.calibre_10}](#index_split_026.html#filepos395094)--[[[155]{.underline}]{.calibre_10}](#index_split_026.html#filepos402079)

    -   in Video Store problem, [[[165]{.underline}]{.calibre_10}](#index_split_026.html#filepos425856)--[[[174]{.underline}]{.calibre_10}](#index_split_026.html#filepos447489)

    -   in Wa-Tor, [[[300]{.underline}]{.calibre_10}](#index_split_034.html#filepos723410), [[[310]{.underline}]{.calibre_10}](#index_split_034.html#filepos748137)

-   Dependency Rule of Clean Architecture, [[[271]{.underline}]{.calibre_10}](#index_split_032.html#filepos658766), [[[275]{.underline}]{.calibre_10}](#index_split_032.html#filepos668351)--[[[276]{.underline}]{.calibre_10}](#index_split_032.html#filepos670446)

-   design patterns. [See also]{.italic}
    > [[[Abstract Factories]{.underline}]{.calibre_10}](#index_split_036.html#filepos834006); [[[Abstract Server pattern]{.underline}]{.calibre_10}](#index_split_036.html#filepos834795); [[[Adapter pattern]{.underline}]{.calibre_10}](#index_split_036.html#filepos836320); [[[Command pattern]{.underline}]{.calibre_10}](#index_split_036.html#filepos853851); [[[Composite pattern]{.underline}]{.calibre_10}](#index_split_036.html#filepos855152); [[[Decorator pattern]{.underline}]{.calibre_10}](#index_split_036.html#filepos862219); [[[Visitor pattern]{.underline}]{.calibre_10}](#index_split_036.html#filepos951371)

    -   about, [[[227]{.underline}]{.calibre_10}](#index_split_031.html#filepos559550), [[[230]{.underline}]{.calibre_10}](#index_split_032.html#filepos561193)--[[[231]{.underline}]{.calibre_10}](#index_split_032.html#filepos564613)

-   [Design Patterns: Elements of Reusable Object-Oriented Software]{.italic} (Gamma et al aka GOF book), [[[98]{.underline}]{.calibre_10}](#index_split_022.html#filepos267992), [[[227]{.underline}]{.calibre_10}](#index_split_031.html#filepos559550)n, [[[259]{.underline}]{.calibre_10}](#index_split_032.html#filepos629815), [[[270]{.underline}]{.calibre_10}](#index_split_032.html#filepos656543), [[[273]{.underline}]{.calibre_10}](#index_split_032.html#filepos665792)

-   Dewdney, A. K., [[[288]{.underline}]{.calibre_10}](#index_split_034.html#filepos691974)

-   DFDs. [See]{.italic}
    > [[[data flow diagrams (DFDs)]{.underline}]{.calibre_10}](#index_split_036.html#filepos860432)

-   diagnostic tests, [[[190]{.underline}]{.calibre_10}](#index_split_028.html#filepos479009)--[[[197]{.underline}]{.calibre_10}](#index_split_028.html#filepos499491)

-   discrete event simulation. [See]{.italic}
    > [[[Gossiping Bus Drivers problem]{.underline}]{.calibre_10}](#index_split_036.html#filepos883784)

-   dispatching functions, [[[135]{.underline}]{.calibre_10}](#index_split_026.html#filepos351742)

-   [` doall `{.calibre4}]{.calibre_17} function, [[[40]{.underline}]{.calibre_10}](#index_split_016.html#filepos135902)

-   [` doseq `{.calibre4}]{.calibre_17} function, [[[251]{.underline}]{.calibre_10}](#index_split_032.html#filepos610302)

-   double (or dual) dispatch, [[[266]{.underline}]{.calibre_10}](#index_split_032.html#filepos645672), [[[270]{.underline}]{.calibre_10}](#index_split_032.html#filepos656543)

-   duck typing, [[[132]{.underline}]{.calibre_10}](#index_split_026.html#filepos344090), [[[139]{.underline}]{.calibre_10}](#index_split_026.html#filepos361624), [[[149]{.underline}]{.calibre_10}](#index_split_026.html#filepos388474). [See also]{.italic}
    > [[[multi-methods]{.underline}]{.calibre_10}](#index_split_036.html#filepos903754)

[[[E]{.calibre_3}]{.bold}]{.calibre1}

::: calibre_11
 
:::

-   [Euler Project, The]{.italic}, [[[213]{.underline}]{.calibre_10}](#index_split_029.html#filepos533449)

-   extensions vs. modifications, [[[131]{.underline}]{.calibre_10}](#index_split_026.html#filepos342014)

[[[F]{.calibre_3}]{.bold}]{.calibre1}

::: calibre_11
 
:::

-   Fibonacci numbers example

    -   with iteration, [[[28]{.underline}]{.calibre_10}](#index_split_015.html#filepos106202)--[[[32]{.underline}]{.calibre_10}](#index_split_015.html#filepos118882)

    -   with lazy lists, [[[38]{.underline}]{.calibre_10}](#index_split_016.html#filepos129898)--[[[40]{.underline}]{.calibre_10}](#index_split_016.html#filepos135902)

    -   with true recursion, [[[32]{.underline}]{.calibre_10}](#index_split_015.html#filepos118882)--[[[35]{.underline}]{.calibre_10}](#index_split_015.html#filepos126924)

-   Fikes, Mike, [[[200]{.underline}]{.calibre_10}](#index_split_029.html#filepos502055)

-   [` filter `{.calibre4}]{.calibre_17}, [[[102]{.underline}]{.calibre_10}](#index_split_022.html#filepos277516)n5

-   finite state machines

    -   and programming style, [[[93]{.underline}]{.calibre_10}](#index_split_021.html#filepos259702)--[[[94]{.underline}]{.calibre_10}](#index_split_021.html#filepos261948)

    -   subway turnstile example, [[[13]{.underline}]{.calibre_10}](#index_split_013.html#filepos84184)--[[[15]{.underline}]{.calibre_10}](#index_split_013.html#filepos89440)

    -   telephone system example, [[[216]{.underline}]{.calibre_10}](#index_split_030.html#filepos534691)--[[[225]{.underline}]{.calibre_10}](#index_split_030.html#filepos556826)

-   [` flatten `{.calibre4}]{.calibre_17}, [[[91]{.underline}]{.calibre_10}](#index_split_021.html#filepos254913)n10

-   [` for `{.calibre4}]{.calibre_17} function, [[[102]{.underline}]{.calibre_10}](#index_split_022.html#filepos277516)n7

-   Fowler, Martin, [Refactoring]{.italic}, [[[155]{.underline}]{.calibre_10}](#index_split_026.html#filepos402079)

-   F# programming language, [[[41]{.underline}]{.calibre_10}](#index_split_016.html#filepos138979), [[[132]{.underline}]{.calibre_10}](#index_split_026.html#filepos344090)

-   fragility, [[[127]{.underline}]{.calibre_10}](#index_split_026.html#filepos331947)

-   functional languages. [See also]{.italic}
    > [[[Clojure]{.underline}]{.calibre_10}](#index_split_036.html#filepos852353)

    -   and design patterns, [[[233]{.underline}]{.calibre_10}](#index_split_032.html#filepos568776)

    -   features, [[[7]{.underline}]{.calibre_10}](#index_split_013.html#filepos68020), [[[34]{.underline}]{.calibre_10}](#index_split_015.html#filepos124752), [[[41]{.underline}]{.calibre_10}](#index_split_016.html#filepos138979), [[[124]{.underline}]{.calibre_10}](#index_split_025.html#filepos327739), [[[185]{.underline}]{.calibre_10}](#index_split_028.html#filepos465872), [[[245]{.underline}]{.calibre_10}](#index_split_032.html#filepos596823), [[[281]{.underline}]{.calibre_10}](#index_split_032.html#filepos684329)

    -   interface mechanisms, [[[132]{.underline}]{.calibre_10}](#index_split_026.html#filepos344090), [[[150]{.underline}]{.calibre_10}](#index_split_026.html#filepos390014)

    -   and mutation, [[[48]{.underline}]{.calibre_10}](#index_split_017.html#filepos155572)

    -   typing in, [[[110]{.underline}]{.calibre_10}](#index_split_023.html#filepos296903)

    -   usage, [[[225]{.underline}]{.calibre_10}](#index_split_030.html#filepos556826)

-   functional programming

    -   defined, [[[4]{.underline}]{.calibre_10}](#index_split_013.html#filepos61537)

    -   and lambda calculus, [[[xvii]{.underline}]{.calibre_10}](#index_split_009.html#filepos48837)

    -   and Moore's law, [[[225]{.underline}]{.calibre_10}](#index_split_030.html#filepos556826)--[[[226]{.underline}]{.calibre_10}](#index_split_030.html#filepos558905)

    -   and OOP compatibility, [[[282]{.underline}]{.calibre_10}](#index_split_032.html#filepos687147)--[[[284]{.underline}]{.calibre_10}](#index_split_032.html#filepos690920)

    -   and resource costs, [[[19]{.underline}]{.calibre_10}](#index_split_014.html#filepos92254)--[[[20]{.underline}]{.calibre_10}](#index_split_014.html#filepos94430), [[[25]{.underline}]{.calibre_10}](#index_split_014.html#filepos104091)

    -   and state change problems, [[[12]{.underline}]{.calibre_10}](#index_split_013.html#filepos81170)--[[[15]{.underline}]{.calibre_10}](#index_split_013.html#filepos89440), [[[93]{.underline}]{.calibre_10}](#index_split_021.html#filepos259702)--[[[94]{.underline}]{.calibre_10}](#index_split_021.html#filepos261948)

    -   and tests, [[[63]{.underline}]{.calibre_10}](#index_split_019.html#filepos192234), [[[184]{.underline}]{.calibre_10}](#index_split_028.html#filepos462905)

    -   and variables, [[[7]{.underline}]{.calibre_10}](#index_split_013.html#filepos68020)--[[[8]{.underline}]{.calibre_10}](#index_split_013.html#filepos70428)

-   functional programs

    -   characteristics, [[[10]{.underline}]{.calibre_10}](#index_split_013.html#filepos76132)--[[[12]{.underline}]{.calibre_10}](#index_split_013.html#filepos81170), [[[15]{.underline}]{.calibre_10}](#index_split_013.html#filepos89440)--[[[16]{.underline}]{.calibre_10}](#index_split_013.html#filepos89440), [[[18]{.underline}]{.calibre_10}](#index_split_014.html#filepos90221), [[[100]{.underline}]{.calibre_10}](#index_split_022.html#filepos271500), [[[335]{.underline}]{.calibre_10}](#index_split_034.html#filepos820888)--[[[336]{.underline}]{.calibre_10}](#index_split_034.html#filepos821960)

    -   GUI frameworks in, [[[200]{.underline}]{.calibre_10}](#index_split_029.html#filepos502055)

    -   vs. Object Oriented programs, [[[93]{.underline}]{.calibre_10}](#index_split_021.html#filepos259702), [[[108]{.underline}]{.calibre_10}](#index_split_022.html#filepos294299), [[[167]{.underline}]{.calibre_10}](#index_split_026.html#filepos429550)

    -   and race conditions, [[[216]{.underline}]{.calibre_10}](#index_split_030.html#filepos534691)

-   functions

    -   as abstraction layer, [[[133]{.underline}]{.calibre_10}](#index_split_026.html#filepos346402)

    -   in mathematics, [[[10]{.underline}]{.calibre_10}](#index_split_013.html#filepos76132)

    -   private, [[[103]{.underline}]{.calibre_10}](#index_split_022.html#filepos280090)n8, [[[283]{.underline}]{.calibre_10}](#index_split_032.html#filepos688480)

[[[G]{.calibre_3}]{.bold}]{.calibre1}

::: calibre_11
 
:::

-   garbage collection, [[[9]{.underline}]{.calibre_10}](#index_split_013.html#filepos73129), [[[42]{.underline}]{.calibre_10}](#index_split_016.html#filepos141075)

-   [` get `{.calibre4}]{.calibre_17}, [[[103]{.underline}]{.calibre_10}](#index_split_022.html#filepos280090)n9

-   GOF book. [See]{.italic}
    > [[[[Design Patterns: Elements of Reusable Object-Oriented Software]{.underline}]{.calibre_10}]{.italic}[[ (Gamma et al)]{.underline}]{.calibre_10}](#index_split_036.html#filepos866899)

-   GOF (Gang of Four), [[[242]{.underline}]{.calibre_10}](#index_split_032.html#filepos591043)n

-   Gossiping Bus Drivers problem

    -   Clojure solution, [[[88]{.underline}]{.calibre_10}](#index_split_021.html#filepos245883)--[[[92]{.underline}]{.calibre_10}](#index_split_021.html#filepos254913)

    -   comparison of solutions, [[[92]{.underline}]{.calibre_10}](#index_split_021.html#filepos254913)--[[[93]{.underline}]{.calibre_10}](#index_split_021.html#filepos259702)

    -   description, [[[78]{.underline}]{.calibre_10}](#index_split_021.html#filepos226973)

    -   Java solution, [[[78]{.underline}]{.calibre_10}](#index_split_021.html#filepos226973)--[[[88]{.underline}]{.calibre_10}](#index_split_021.html#filepos245883)

-   graphics. [See]{.italic}
    > [[[turtle graphics]{.underline}]{.calibre_10}](#index_split_036.html#filepos945149)

-   GUI

    -   architectural application example, [[[245]{.underline}]{.calibre_10}](#index_split_032.html#filepos596823)--[[[249]{.underline}]{.calibre_10}](#index_split_032.html#filepos605382)

    -   frameworks, [[[200]{.underline}]{.calibre_10}](#index_split_029.html#filepos502055)

[[[H]{.calibre_3}]{.bold}]{.calibre1}

::: calibre_11
 
:::

-   handle/body patterns. [See]{.italic}
    > [[[Composite pattern]{.underline}]{.calibre_10}](#index_split_036.html#filepos855152); [[[Decorator pattern]{.underline}]{.calibre_10}](#index_split_036.html#filepos862219)

-   Haskell programming language, [[[xiv]{.underline}]{.calibre_10}](#index_split_008.html#filepos43219), [[[41]{.underline}]{.calibre_10}](#index_split_016.html#filepos138979), [[[283]{.underline}]{.calibre_10}](#index_split_032.html#filepos688480)

-   high-level policy and low-level detail, [[[132]{.underline}]{.calibre_10}](#index_split_026.html#filepos344090), [[[136]{.underline}]{.calibre_10}](#index_split_026.html#filepos355413)--[[[138]{.underline}]{.calibre_10}](#index_split_026.html#filepos360177), [[[154]{.underline}]{.calibre_10}](#index_split_026.html#filepos399777)--[[[155]{.underline}]{.calibre_10}](#index_split_026.html#filepos402079)

-   higher-order functions, [[[133]{.underline}]{.calibre_10}](#index_split_026.html#filepos346402)n

[[[I]{.calibre_3}]{.bold}]{.calibre1}

::: calibre_11
 
:::

-   immutability, [[[15]{.underline}]{.calibre_10}](#index_split_013.html#filepos89440)-[[[16]{.underline}]{.calibre_10}](#index_split_013.html#filepos89440), [[[47]{.underline}]{.calibre_10}](#index_split_017.html#filepos153273), [[[93]{.underline}]{.calibre_10}](#index_split_021.html#filepos259702)-[[[94]{.underline}]{.calibre_10}](#index_split_021.html#filepos261948), [[[281]{.underline}]{.calibre_10}](#index_split_032.html#filepos684329). [See also]{.italic}
    > [[[mutability]{.underline}]{.calibre_10}](#index_split_036.html#filepos904920)

-   independent deployability, [[[136]{.underline}]{.calibre_10}](#index_split_026.html#filepos355413)--[[[138]{.underline}]{.calibre_10}](#index_split_026.html#filepos360177)

-   initialization, [[[6]{.underline}]{.calibre_10}](#index_split_013.html#filepos66018), [[[7]{.underline}]{.calibre_10}](#index_split_013.html#filepos68020)--[[[8]{.underline}]{.calibre_10}](#index_split_013.html#filepos70428), [[[18]{.underline}]{.calibre_10}](#index_split_014.html#filepos90221), [[[19]{.underline}]{.calibre_10}](#index_split_014.html#filepos92254)

-   integration tests, [[[165]{.underline}]{.calibre_10}](#index_split_026.html#filepos425856)--[[[166]{.underline}]{.calibre_10}](#index_split_026.html#filepos426907)

-   interactive programs, [[[44]{.underline}]{.calibre_10}](#index_split_017.html#filepos143664)

-   Interface Segregation Principle (ISP)

    -   examples, [[[147]{.underline}]{.calibre_10}](#index_split_026.html#filepos384615)--[[[150]{.underline}]{.calibre_10}](#index_split_026.html#filepos390014)

    -   usage, [[[150]{.underline}]{.calibre_10}](#index_split_026.html#filepos390014)--[[[151]{.underline}]{.calibre_10}](#index_split_026.html#filepos392701)

-   ISA rule, [[[142]{.underline}]{.calibre_10}](#index_split_026.html#filepos370974)--[[[145]{.underline}]{.calibre_10}](#index_split_026.html#filepos379124), [[[179]{.underline}]{.calibre_10}](#index_split_026.html#filepos460156)

-   iteration

    -   Fibonacci example, [[[28]{.underline}]{.calibre_10}](#index_split_015.html#filepos106202), [[[30]{.underline}]{.calibre_10}](#index_split_015.html#filepos112186)--[[[32]{.underline}]{.calibre_10}](#index_split_015.html#filepos118882)

    -   vs. recursion, [[[35]{.underline}]{.calibre_10}](#index_split_015.html#filepos126924)

-   iterators, [[[38]{.underline}]{.calibre_10}](#index_split_016.html#filepos129898), [[[40]{.underline}]{.calibre_10}](#index_split_016.html#filepos135902)

[[[J]{.calibre_3}]{.bold}]{.calibre1}

::: calibre_11
 
:::

-   [` jar `{.calibre4}]{.calibre_17} files, [[[136]{.underline}]{.calibre_10}](#index_split_026.html#filepos355413)--[[[137]{.underline}]{.calibre_10}](#index_split_026.html#filepos357661)

-   Java virtual machine (JVM), [[[7]{.underline}]{.calibre_10}](#index_split_013.html#filepos68020)n, [[[32]{.underline}]{.calibre_10}](#index_split_015.html#filepos118882), [[[138]{.underline}]{.calibre_10}](#index_split_026.html#filepos360177)

[[[L]{.calibre_3}]{.bold}]{.calibre1}

::: calibre_11
 
:::

-   lambda calculus, [[[xvi]{.underline}]{.calibre_10}](#index_split_009.html#filepos46603)--[[[xvii]{.underline}]{.calibre_10}](#index_split_009.html#filepos48837), [[[19]{.underline}]{.calibre_10}](#index_split_014.html#filepos92254)

-   languages. [See also]{.italic}
    > [[[Clojure]{.underline}]{.calibre_10}](#index_split_036.html#filepos852353); [[[functional languages]{.underline}]{.calibre_10}](#index_split_036.html#filepos875994)

    -   coupling characteristics, [[[150]{.underline}]{.calibre_10}](#index_split_026.html#filepos390014)

    -   type characteristics, [[[147]{.underline}]{.calibre_10}](#index_split_026.html#filepos384615)

-   laziness

    -   Fibonacci example, [[[38]{.underline}]{.calibre_10}](#index_split_016.html#filepos129898)--[[[40]{.underline}]{.calibre_10}](#index_split_016.html#filepos135902)

    -   list accumulation, [[[40]{.underline}]{.calibre_10}](#index_split_016.html#filepos135902)

    -   usage, [[[41]{.underline}]{.calibre_10}](#index_split_016.html#filepos138979)--[[[42]{.underline}]{.calibre_10}](#index_split_016.html#filepos141075)

-   lazy lists, [[[38]{.underline}]{.calibre_10}](#index_split_016.html#filepos129898)--[[[40]{.underline}]{.calibre_10}](#index_split_016.html#filepos135902)

-   Liskov Substitution Principle (LSP)

    -   code example and tests, [[[139]{.underline}]{.calibre_10}](#index_split_026.html#filepos361624)--[[[142]{.underline}]{.calibre_10}](#index_split_026.html#filepos370974)

    -   and ISA rule, [[[142]{.underline}]{.calibre_10}](#index_split_026.html#filepos370974)--[[[145]{.underline}]{.calibre_10}](#index_split_026.html#filepos379124)

    -   principle, [[[138]{.underline}]{.calibre_10}](#index_split_026.html#filepos360177)--[[[139]{.underline}]{.calibre_10}](#index_split_026.html#filepos361624)

    -   and representative rule, [[[146]{.underline}]{.calibre_10}](#index_split_026.html#filepos381921)--[[[147]{.underline}]{.calibre_10}](#index_split_026.html#filepos384615)

-   locking, [[[49]{.underline}]{.calibre_10}](#index_split_017.html#filepos158106)

-   low-level detail. [See]{.italic}
    > [[[high-level policy and low-level detail]{.underline}]{.calibre_10}](#index_split_036.html#filepos886048)

[[[M]{.calibre_3}]{.bold}]{.calibre1}

::: calibre_11
 
:::

-   [` map `{.calibre4}]{.calibre_17} function, [[[33]{.underline}]{.calibre_10}](#index_split_015.html#filepos121785)

-   Martin, Robert C.

    -   [Agile Software Development: Principles, Patterns, and Practices]{.italic}, [[[53]{.underline}]{.calibre_10}](#index_split_018.html#filepos165870), [[[96]{.underline}]{.calibre_10}](#index_split_022.html#filepos263307), [[[126]{.underline}]{.calibre_10}](#index_split_026.html#filepos329228), [[[184]{.underline}]{.calibre_10}](#index_split_028.html#filepos462905)n, [[[231]{.underline}]{.calibre_10}](#index_split_032.html#filepos564613)n4, [[[243]{.underline}]{.calibre_10}](#index_split_032.html#filepos592355)

    -   [Clean Architecture]{.italic}, [[[96]{.underline}]{.calibre_10}](#index_split_022.html#filepos263307), [[[126]{.underline}]{.calibre_10}](#index_split_026.html#filepos329228)

    -   [Clean Craftsmanship]{.italic}, [[[53]{.underline}]{.calibre_10}](#index_split_018.html#filepos165870), [[[79]{.underline}]{.calibre_10}](#index_split_021.html#filepos229830)n

    -   [Refactoring]{.italic}, [[[155]{.underline}]{.calibre_10}](#index_split_026.html#filepos402079)

-   memoization, [[[34]{.underline}]{.calibre_10}](#index_split_015.html#filepos124752)--[[[35]{.underline}]{.calibre_10}](#index_split_015.html#filepos126924)

-   [` memoize `{.calibre4}]{.calibre_17} function, [[[35]{.underline}]{.calibre_10}](#index_split_015.html#filepos126924)

-   memory usage

    -   garbage collection, [[[9]{.underline}]{.calibre_10}](#index_split_013.html#filepos73129), [[[42]{.underline}]{.calibre_10}](#index_split_016.html#filepos141075)

    -   and laziness, [[[39]{.underline}]{.calibre_10}](#index_split_016.html#filepos132376)--[[[41]{.underline}]{.calibre_10}](#index_split_016.html#filepos138979)

    -   with [n]{.italic}-ary trees, [[[24]{.underline}]{.calibre_10}](#index_split_014.html#filepos102483)--[[[25]{.underline}]{.calibre_10}](#index_split_014.html#filepos104091)

    -   in Sieve of Eratosthenes algorithm, [[[22]{.underline}]{.calibre_10}](#index_split_014.html#filepos99056)

-   message sequence charts, [[[216]{.underline}]{.calibre_10}](#index_split_030.html#filepos534691)--[[[217]{.underline}]{.calibre_10}](#index_split_030.html#filepos536175)

-   Meyer, Bertrand, [Object-Oriented Software Construction]{.italic}, [[[131]{.underline}]{.calibre_10}](#index_split_026.html#filepos342014)

-   mocks, [[[184]{.underline}]{.calibre_10}](#index_split_028.html#filepos462905)--[[[186]{.underline}]{.calibre_10}](#index_split_028.html#filepos468867), [[[236]{.underline}]{.calibre_10}](#index_split_032.html#filepos575468)

-   modifications vs. extensions, [[[131]{.underline}]{.calibre_10}](#index_split_026.html#filepos342014)

-   modules

    -   dependencies, [[[150]{.underline}]{.calibre_10}](#index_split_026.html#filepos390014)--[[[151]{.underline}]{.calibre_10}](#index_split_026.html#filepos392701)

    -   extensions vs. modifications, [[[131]{.underline}]{.calibre_10}](#index_split_026.html#filepos342014)--[[[132]{.underline}]{.calibre_10}](#index_split_026.html#filepos344090)

-   Moore's law, [[[225]{.underline}]{.calibre_10}](#index_split_030.html#filepos556826)

-   [` more-speech `{.calibre4}]{.calibre_17} application, [[[48]{.underline}]{.calibre_10}](#index_split_017.html#filepos155572)n, [[[185]{.underline}]{.calibre_10}](#index_split_028.html#filepos465872)

-   multi-methods

    -   in ATM interactor example, [[[149]{.underline}]{.calibre_10}](#index_split_026.html#filepos388474)--[[[150]{.underline}]{.calibre_10}](#index_split_026.html#filepos390014)

    -   in copy example, [[[135]{.underline}]{.calibre_10}](#index_split_026.html#filepos351742)--[[[136]{.underline}]{.calibre_10}](#index_split_026.html#filepos355413)

    -   in switch and light problem, [[[235]{.underline}]{.calibre_10}](#index_split_032.html#filepos573383)--[[[236]{.underline}]{.calibre_10}](#index_split_032.html#filepos575468), [[[240]{.underline}]{.calibre_10}](#index_split_032.html#filepos585587)--[[[241]{.underline}]{.calibre_10}](#index_split_032.html#filepos587478)

    -   in video statement formatting example, [[[167]{.underline}]{.calibre_10}](#index_split_026.html#filepos429550)--[[[179]{.underline}]{.calibre_10}](#index_split_026.html#filepos460156)

    -   in Wa-Tor, [[[312]{.underline}]{.calibre_10}](#index_split_034.html#filepos752976)

-   mutability. [See also]{.italic}
    > [[[immutability]{.underline}]{.calibre_10}](#index_split_036.html#filepos887039)

    -   and concurrency, [[[216]{.underline}]{.calibre_10}](#index_split_030.html#filepos534691)

    -   in languages and frameworks, [[[47]{.underline}]{.calibre_10}](#index_split_017.html#filepos153273)--[[[48]{.underline}]{.calibre_10}](#index_split_017.html#filepos155572), [[[124]{.underline}]{.calibre_10}](#index_split_025.html#filepos327739), [[[200]{.underline}]{.calibre_10}](#index_split_029.html#filepos502055)

    -   and testing, [[[197]{.underline}]{.calibre_10}](#index_split_028.html#filepos499491)

[[[N]{.calibre_3}]{.bold}]{.calibre1}

::: calibre_11
 
:::

-   namespaces and source files, [[[106]{.underline}]{.calibre_10}](#index_split_022.html#filepos289386)--[[[108]{.underline}]{.calibre_10}](#index_split_022.html#filepos294299), [[[238]{.underline}]{.calibre_10}](#index_split_032.html#filepos580042)--[[[239]{.underline}]{.calibre_10}](#index_split_032.html#filepos582448)

-   [n]{.italic}-ary trees, [[[23]{.underline}]{.calibre_10}](#index_split_014.html#filepos100426)--[[[25]{.underline}]{.calibre_10}](#index_split_014.html#filepos104091)

-   90-degree rotations, [[[265]{.underline}]{.calibre_10}](#index_split_032.html#filepos643762), [[[270]{.underline}]{.calibre_10}](#index_split_032.html#filepos656543)--[[[271]{.underline}]{.calibre_10}](#index_split_032.html#filepos658766), [[[279]{.underline}]{.calibre_10}](#index_split_032.html#filepos678316)

-   [` ns `{.calibre4}]{.calibre_17} (namespace), [[[159]{.underline}]{.calibre_10}](#index_split_026.html#filepos411531)n, [[[238]{.underline}]{.calibre_10}](#index_split_032.html#filepos580042)

-   Nygaard, Kristen, [[[78]{.underline}]{.calibre_10}](#index_split_021.html#filepos226973), [[[153]{.underline}]{.calibre_10}](#index_split_026.html#filepos396387)

[[[O]{.calibre_3}]{.bold}]{.calibre1}

::: calibre_11
 
:::

-   object orientation (OO)

    -   and functional programming, [[[53]{.underline}]{.calibre_10}](#index_split_018.html#filepos165870), [[[93]{.underline}]{.calibre_10}](#index_split_021.html#filepos259702)--[[[94]{.underline}]{.calibre_10}](#index_split_021.html#filepos261948), [[[108]{.underline}]{.calibre_10}](#index_split_022.html#filepos294299), [[[282]{.underline}]{.calibre_10}](#index_split_032.html#filepos687147)--[[[283]{.underline}]{.calibre_10}](#index_split_032.html#filepos688480)

    -   origins, [[[78]{.underline}]{.calibre_10}](#index_split_021.html#filepos226973), [[[153]{.underline}]{.calibre_10}](#index_split_026.html#filepos396387)

    -   program characteristics, [[[93]{.underline}]{.calibre_10}](#index_split_021.html#filepos259702), [[[96]{.underline}]{.calibre_10}](#index_split_022.html#filepos263307)

-   [Object-Oriented Software Construction]{.italic} (Meyer), [[[131]{.underline}]{.calibre_10}](#index_split_026.html#filepos342014)

-   OCP. [See]{.italic}
    > [[[Open-Closed Principle (OCP)]{.underline}]{.calibre_10}](#index_split_036.html#filepos910650)

-   opaque arguments, [[[279]{.underline}]{.calibre_10}](#index_split_032.html#filepos678316)--[[[281]{.underline}]{.calibre_10}](#index_split_032.html#filepos684329)

-   Open-Closed Principle (OCP)

    -   with functions, [[[133]{.underline}]{.calibre_10}](#index_split_026.html#filepos346402)--[[[134]{.underline}]{.calibre_10}](#index_split_026.html#filepos348780)

    -   independent deployability, [[[136]{.underline}]{.calibre_10}](#index_split_026.html#filepos355413)--[[[138]{.underline}]{.calibre_10}](#index_split_026.html#filepos360177)

    -   with multi-methods, [[[135]{.underline}]{.calibre_10}](#index_split_026.html#filepos351742)--[[[136]{.underline}]{.calibre_10}](#index_split_026.html#filepos355413)

    -   usage, [[[131]{.underline}]{.calibre_10}](#index_split_026.html#filepos342014)--[[[132]{.underline}]{.calibre_10}](#index_split_026.html#filepos344090)

    -   with vtables, [[[134]{.underline}]{.calibre_10}](#index_split_026.html#filepos348780)

[[[P]{.calibre_3}]{.bold}]{.calibre1}

::: calibre_11
 
:::

-   Papert, Seymour, [[[201]{.underline}]{.calibre_10}](#index_split_029.html#filepos505754)

-   [` partial `{.calibre4}]{.calibre_17} function, [[[102]{.underline}]{.calibre_10}](#index_split_022.html#filepos277516)n6

-   [` partition `{.calibre4}]{.calibre_17} function, [[[72]{.underline}]{.calibre_10}](#index_split_020.html#filepos210862)n4

-   partitioning

    -   in Gossiping Bus Drivers problem, [[[93]{.underline}]{.calibre_10}](#index_split_021.html#filepos259702)

    -   in Wa-Tor, [[[335]{.underline}]{.calibre_10}](#index_split_034.html#filepos820888)

-   Payroll problem

    -   Clojure solution, [[[98]{.underline}]{.calibre_10}](#index_split_022.html#filepos267992)--[[[107]{.underline}]{.calibre_10}](#index_split_022.html#filepos292047)

    -   Java solution, [[[97]{.underline}]{.calibre_10}](#index_split_022.html#filepos266369)--[[[98]{.underline}]{.calibre_10}](#index_split_022.html#filepos267992)

    -   requirements, [[[96]{.underline}]{.calibre_10}](#index_split_022.html#filepos263307)--[[[97]{.underline}]{.calibre_10}](#index_split_022.html#filepos266369)

    -   type specifications, [[[110]{.underline}]{.calibre_10}](#index_split_023.html#filepos296903)--[[[113]{.underline}]{.calibre_10}](#index_split_023.html#filepos305961)

-   persistent data structures, [[[25]{.underline}]{.calibre_10}](#index_split_014.html#filepos104091)

-   pointer to implementation (PIMPL) pattern, [[[140]{.underline}]{.calibre_10}](#index_split_026.html#filepos365605)

-   polymorphic interfaces, in architectural drawing application, [[[248]{.underline}]{.calibre_10}](#index_split_032.html#filepos604889)--[[[249]{.underline}]{.calibre_10}](#index_split_032.html#filepos605382)

-   polymorphism

    -   mechanisms in Clojure, [[[134]{.underline}]{.calibre_10}](#index_split_026.html#filepos348780), [[[238]{.underline}]{.calibre_10}](#index_split_032.html#filepos580042)--[[[239]{.underline}]{.calibre_10}](#index_split_032.html#filepos582448), [[[249]{.underline}]{.calibre_10}](#index_split_032.html#filepos605382), [[[282]{.underline}]{.calibre_10}](#index_split_032.html#filepos687147), [[[283]{.underline}]{.calibre_10}](#index_split_032.html#filepos688480)

    -   and mocks, [[[185]{.underline}]{.calibre_10}](#index_split_028.html#filepos465872)

    -   in OO, [[[96]{.underline}]{.calibre_10}](#index_split_022.html#filepos263307), [[[132]{.underline}]{.calibre_10}](#index_split_026.html#filepos344090)

-   prime factors example, [[[186]{.underline}]{.calibre_10}](#index_split_028.html#filepos468867)--[[[189]{.underline}]{.calibre_10}](#index_split_028.html#filepos476865)

-   Prime Factors problem

    -   Clojure version, [[[60]{.underline}]{.calibre_10}](#index_split_019.html#filepos181363)--[[[63]{.underline}]{.calibre_10}](#index_split_019.html#filepos192234)

    -   comparison of solutions, [[[63]{.underline}]{.calibre_10}](#index_split_019.html#filepos192234)--[[[64]{.underline}]{.calibre_10}](#index_split_019.html#filepos194852)

    -   Java version, [[[56]{.underline}]{.calibre_10}](#index_split_019.html#filepos168572)--[[[60]{.underline}]{.calibre_10}](#index_split_019.html#filepos181363)

-   private functions, [[[103]{.underline}]{.calibre_10}](#index_split_022.html#filepos280090)n8, [[[283]{.underline}]{.calibre_10}](#index_split_032.html#filepos688480)

-   [Processing]{.italic} framework, [[[47]{.underline}]{.calibre_10}](#index_split_017.html#filepos153273)n, [[[200]{.underline}]{.calibre_10}](#index_split_029.html#filepos502055)

-   property-based testing, [[[186]{.underline}]{.calibre_10}](#index_split_028.html#filepos468867)--[[[189]{.underline}]{.calibre_10}](#index_split_028.html#filepos476865)

-   protocol/record mechanism, [[[137]{.underline}]{.calibre_10}](#index_split_026.html#filepos357661)--[[[138]{.underline}]{.calibre_10}](#index_split_026.html#filepos360177)

[[[Q]{.calibre_3}]{.bold}]{.calibre1}

::: calibre_11
 
:::

-   [` quick-check `{.calibre4}]{.calibre_17}, [[[194]{.underline}]{.calibre_10}](#index_split_028.html#filepos491788), [[[195]{.underline}]{.calibre_10}](#index_split_028.html#filepos495138), [[[197]{.underline}]{.calibre_10}](#index_split_028.html#filepos499491)

-   QuickCheck, [[[188]{.underline}]{.calibre_10}](#index_split_028.html#filepos473859)

-   Quil framework, [[[47]{.underline}]{.calibre_10}](#index_split_017.html#filepos153273), [[[200]{.underline}]{.calibre_10}](#index_split_029.html#filepos502055)

[[[R]{.calibre_3}]{.bold}]{.calibre1}

::: calibre_11
 
:::

-   race conditions

    -   defined, [[[9]{.underline}]{.calibre_10}](#index_split_013.html#filepos73129)

    -   in finite state machines, [[[226]{.underline}]{.calibre_10}](#index_split_030.html#filepos558905)

    -   in telephone system examples, [[[223]{.underline}]{.calibre_10}](#index_split_030.html#filepos552559)--[[[225]{.underline}]{.calibre_10}](#index_split_030.html#filepos556826)

-   [` range `{.calibre4}]{.calibre_17} function, [[[33]{.underline}]{.calibre_10}](#index_split_015.html#filepos121785), [[[38]{.underline}]{.calibre_10}](#index_split_016.html#filepos129898)

-   recursion

    -   vs. assignment statements, [[[6]{.underline}]{.calibre_10}](#index_split_013.html#filepos66018)--[[[7]{.underline}]{.calibre_10}](#index_split_013.html#filepos68020)

    -   in Fibonacci example, [[[32]{.underline}]{.calibre_10}](#index_split_015.html#filepos118882)--[[[35]{.underline}]{.calibre_10}](#index_split_015.html#filepos126924)

    -   vs. iteration, [[[35]{.underline}]{.calibre_10}](#index_split_015.html#filepos126924)

    -   state changes in, [[[15]{.underline}]{.calibre_10}](#index_split_013.html#filepos89440)--[[[16]{.underline}]{.calibre_10}](#index_split_013.html#filepos89440)

-   [` reduce `{.calibre4}]{.calibre_17} function, [[[72]{.underline}]{.calibre_10}](#index_split_020.html#filepos210862)

-   [Refactoring]{.italic} (Martin), [[[155]{.underline}]{.calibre_10}](#index_split_026.html#filepos402079)

-   referential transparency, [[[11]{.underline}]{.calibre_10}](#index_split_013.html#filepos78492)--[[[12]{.underline}]{.calibre_10}](#index_split_013.html#filepos81170), [[[34]{.underline}]{.calibre_10}](#index_split_015.html#filepos124752)

-   [` repeat `{.calibre4}]{.calibre_17} function, [[[71]{.underline}]{.calibre_10}](#index_split_020.html#filepos208585)n

-   REPL, [[[184]{.underline}]{.calibre_10}](#index_split_028.html#filepos462905)

-   representatives, [[[146]{.underline}]{.calibre_10}](#index_split_026.html#filepos381921)--[[[147]{.underline}]{.calibre_10}](#index_split_026.html#filepos384615)

-   [` rest `{.calibre4}]{.calibre_17} function, [[[38]{.underline}]{.calibre_10}](#index_split_016.html#filepos129898)

-   runtime dependencies, [[[152]{.underline}]{.calibre_10}](#index_split_026.html#filepos395094)--[[[155]{.underline}]{.calibre_10}](#index_split_026.html#filepos402079)

[[[S]{.calibre_3}]{.bold}]{.calibre1}

::: calibre_11
 
:::

-   Scala programming language, [[[41]{.underline}]{.calibre_10}](#index_split_016.html#filepos138979), [[[132]{.underline}]{.calibre_10}](#index_split_026.html#filepos344090)

-   SeeSaw framework, [[[200]{.underline}]{.calibre_10}](#index_split_029.html#filepos502055)

-   semantic validation vs. business rule tests, [[[127]{.underline}]{.calibre_10}](#index_split_026.html#filepos331947)--[[[131]{.underline}]{.calibre_10}](#index_split_026.html#filepos342014)

-   sequential coupling. [See]{.italic}
    > [[[temporal coupling]{.underline}]{.calibre_10}](#index_split_036.html#filepos941036)

-   shape example

    -   Abstract Factory pattern, [[[276]{.underline}]{.calibre_10}](#index_split_032.html#filepos670446)--[[[281]{.underline}]{.calibre_10}](#index_split_032.html#filepos684329)

    -   Composite pattern, [[[254]{.underline}]{.calibre_10}](#index_split_032.html#filepos616793)--[[[259]{.underline}]{.calibre_10}](#index_split_032.html#filepos629815)

    -   Decorator pattern, [[[260]{.underline}]{.calibre_10}](#index_split_032.html#filepos630536)--[[[263]{.underline}]{.calibre_10}](#index_split_032.html#filepos638276)

    -   and instance creation, [[[274]{.underline}]{.calibre_10}](#index_split_032.html#filepos666748)--[[[276]{.underline}]{.calibre_10}](#index_split_032.html#filepos670446)

    -   Visitor pattern, [[[264]{.underline}]{.calibre_10}](#index_split_032.html#filepos641681)--[[[267]{.underline}]{.calibre_10}](#index_split_032.html#filepos649292), [[[268]{.underline}]{.calibre_10}](#index_split_032.html#filepos651668)--[[[270]{.underline}]{.calibre_10}](#index_split_032.html#filepos656543), [[[271]{.underline}]{.calibre_10}](#index_split_032.html#filepos658766)--[[[273]{.underline}]{.calibre_10}](#index_split_032.html#filepos665792)

-   side effects, [[[254]{.underline}]{.calibre_10}](#index_split_032.html#filepos616793), [[[283]{.underline}]{.calibre_10}](#index_split_032.html#filepos688480)--[[[284]{.underline}]{.calibre_10}](#index_split_032.html#filepos690920)

-   Sieve of Eratosthenes, [[[18]{.underline}]{.calibre_10}](#index_split_014.html#filepos90221)--[[[19]{.underline}]{.calibre_10}](#index_split_014.html#filepos92254), [[[20]{.underline}]{.calibre_10}](#index_split_014.html#filepos94430)--[[[22]{.underline}]{.calibre_10}](#index_split_014.html#filepos99056)

-   SIMULA-[[[67]{.underline}]{.calibre_10}](#index_split_020.html#filepos198476), [[[78]{.underline}]{.calibre_10}](#index_split_021.html#filepos226973), [[[153]{.underline}]{.calibre_10}](#index_split_026.html#filepos396387)n20

-   Single Responsibility Principle (SRP)

    -   defined, [[[126]{.underline}]{.calibre_10}](#index_split_026.html#filepos329228)--[[[127]{.underline}]{.calibre_10}](#index_split_026.html#filepos331947)

    -   usage, [[[130]{.underline}]{.calibre_10}](#index_split_026.html#filepos339613)--[[[131]{.underline}]{.calibre_10}](#index_split_026.html#filepos342014), [[[288]{.underline}]{.calibre_10}](#index_split_034.html#filepos691974)

    -   violation examples, [[[76]{.underline}]{.calibre_10}](#index_split_020.html#filepos224096), [[[127]{.underline}]{.calibre_10}](#index_split_026.html#filepos331947)--[[[130]{.underline}]{.calibre_10}](#index_split_026.html#filepos339613), [[[159]{.underline}]{.calibre_10}](#index_split_026.html#filepos411531)

-   Software Transactional Memory (STM), [[[48]{.underline}]{.calibre_10}](#index_split_017.html#filepos155572)--[[[51]{.underline}]{.calibre_10}](#index_split_017.html#filepos163544)

-   SOLID principles. [See also]{.italic}
    > [[[Dependency Inversion Principle (DIP)]{.underline}]{.calibre_10}](#index_split_036.html#filepos864847); [[[Interface Segregation Principle (ISP)]{.underline}]{.calibre_10}](#index_split_036.html#filepos889071); [[[Liskov Substitution Principle (LSP)]{.underline}]{.calibre_10}](#index_split_036.html#filepos895230); [[[Open-Closed Principle (OCP)]{.underline}]{.calibre_10}](#index_split_036.html#filepos910650); [[[Single Responsibility Principle (SRP)]{.underline}]{.calibre_10}](#index_split_036.html#filepos929401)

    -   resources, [[[126]{.underline}]{.calibre_10}](#index_split_026.html#filepos329228)

-   source code dependencies

    -   and instance creation, [[[274]{.underline}]{.calibre_10}](#index_split_032.html#filepos666748)--[[[276]{.underline}]{.calibre_10}](#index_split_032.html#filepos670446)

    -   inversion, [[[104]{.underline}]{.calibre_10}](#index_split_022.html#filepos284663)--[[[105]{.underline}]{.calibre_10}](#index_split_022.html#filepos286904)

    -   and runtime dependencies, [[[152]{.underline}]{.calibre_10}](#index_split_026.html#filepos395094)--[[[155]{.underline}]{.calibre_10}](#index_split_026.html#filepos402079)

-   source files

    -   loading from, [[[137]{.underline}]{.calibre_10}](#index_split_026.html#filepos357661)

    -   and namespaces, [[[106]{.underline}]{.calibre_10}](#index_split_022.html#filepos289386)--[[[108]{.underline}]{.calibre_10}](#index_split_022.html#filepos294299)

-   Spacewar!, [[[45]{.underline}]{.calibre_10}](#index_split_017.html#filepos145812)--[[[47]{.underline}]{.calibre_10}](#index_split_017.html#filepos153273), [[[114]{.underline}]{.calibre_10}](#index_split_023.html#filepos309309), [[[200]{.underline}]{.calibre_10}](#index_split_029.html#filepos502055)

-   [` speclj `{.calibre4}]{.calibre_17} framework, [[[184]{.underline}]{.calibre_10}](#index_split_028.html#filepos462905)

-   squares and rectangles example, [[[142]{.underline}]{.calibre_10}](#index_split_026.html#filepos370974)--[[[147]{.underline}]{.calibre_10}](#index_split_026.html#filepos384615)

-   state of the system. [See also]{.italic}
    > [[[finite state machines]{.underline}]{.calibre_10}](#index_split_036.html#filepos872690)

    -   in functional programs, [[[12]{.underline}]{.calibre_10}](#index_split_013.html#filepos81170)--[[[13]{.underline}]{.calibre_10}](#index_split_013.html#filepos84184), [[[15]{.underline}]{.calibre_10}](#index_split_013.html#filepos89440)--[[[16]{.underline}]{.calibre_10}](#index_split_013.html#filepos89440), [[[44]{.underline}]{.calibre_10}](#index_split_017.html#filepos143664)--[[[45]{.underline}]{.calibre_10}](#index_split_017.html#filepos145812)

    -   and structural sharing, [[[23]{.underline}]{.calibre_10}](#index_split_014.html#filepos100426)--[[[25]{.underline}]{.calibre_10}](#index_split_014.html#filepos104091)

    -   and temporal couplings, [[[8]{.underline}]{.calibre_10}](#index_split_013.html#filepos70428)

-   subway turnstile example, [[[13]{.underline}]{.calibre_10}](#index_split_013.html#filepos84184)--[[[15]{.underline}]{.calibre_10}](#index_split_013.html#filepos89440)

-   sum of squares example, [[[4]{.underline}]{.calibre_10}](#index_split_013.html#filepos61537)--[[[6]{.underline}]{.calibre_10}](#index_split_013.html#filepos66018), [[[9]{.underline}]{.calibre_10}](#index_split_013.html#filepos73129)--[[[10]{.underline}]{.calibre_10}](#index_split_013.html#filepos76132), [[[11]{.underline}]{.calibre_10}](#index_split_013.html#filepos78492)

-   Swing framework, [[[48]{.underline}]{.calibre_10}](#index_split_017.html#filepos155572), [[[200]{.underline}]{.calibre_10}](#index_split_029.html#filepos502055)

-   switch and light problem

    -   Abstract Server pattern, [[[234]{.underline}]{.calibre_10}](#index_split_032.html#filepos570739)--[[[236]{.underline}]{.calibre_10}](#index_split_032.html#filepos575468)

    -   Adapter pattern, [[[236]{.underline}]{.calibre_10}](#index_split_032.html#filepos575468)--[[[242]{.underline}]{.calibre_10}](#index_split_032.html#filepos591043)

    -   Composite pattern, [[[250]{.underline}]{.calibre_10}](#index_split_032.html#filepos607406)--[[[254]{.underline}]{.calibre_10}](#index_split_032.html#filepos616793)

    -   description, [[[230]{.underline}]{.calibre_10}](#index_split_032.html#filepos561193)--[[[233]{.underline}]{.calibre_10}](#index_split_032.html#filepos568776)

[[[T]{.calibre_3}]{.bold}]{.calibre1}

::: calibre_11
 
:::

-   tail call functions, [[[28]{.underline}]{.calibre_10}](#index_split_015.html#filepos106202)

-   tail call optimization (TCO)

    -   defined, [[[7]{.underline}]{.calibre_10}](#index_split_013.html#filepos68020)

    -   explicitly invoked, [[[32]{.underline}]{.calibre_10}](#index_split_015.html#filepos118882)

    -   usage, [[[19]{.underline}]{.calibre_10}](#index_split_014.html#filepos92254)--[[[20]{.underline}]{.calibre_10}](#index_split_014.html#filepos94430), [[[35]{.underline}]{.calibre_10}](#index_split_015.html#filepos126924)

-   [` take `{.calibre4}]{.calibre_17} function, [[[39]{.underline}]{.calibre_10}](#index_split_016.html#filepos132376), [[[40]{.underline}]{.calibre_10}](#index_split_016.html#filepos135902), [[[73]{.underline}]{.calibre_10}](#index_split_020.html#filepos215186)

-   TCO. [See]{.italic}
    > [[[tail call optimization (TCO)]{.underline}]{.calibre_10}](#index_split_036.html#filepos938544)

-   TDD. [See]{.italic}
    > [[[test-driven development (TDD)]{.underline}]{.calibre_10}](#index_split_036.html#filepos941373)

-   telephone system example

    -   in Clojure, [[[219]{.underline}]{.calibre_10}](#index_split_030.html#filepos540565)--[[[223]{.underline}]{.calibre_10}](#index_split_030.html#filepos552559)

    -   finite state machines, [[[216]{.underline}]{.calibre_10}](#index_split_030.html#filepos534691)--[[[217]{.underline}]{.calibre_10}](#index_split_030.html#filepos536175)

    -   race condition, [[[223]{.underline}]{.calibre_10}](#index_split_030.html#filepos552559)--[[[225]{.underline}]{.calibre_10}](#index_split_030.html#filepos556826)

-   Template Method pattern, [[[175]{.underline}]{.calibre_10}](#index_split_026.html#filepos450008), [[[324]{.underline}]{.calibre_10}](#index_split_034.html#filepos788288)

-   temporal coupling, [[[8]{.underline}]{.calibre_10}](#index_split_013.html#filepos70428)--[[[10]{.underline}]{.calibre_10}](#index_split_013.html#filepos76132)

-   test-driven development (TDD), [[[53]{.underline}]{.calibre_10}](#index_split_018.html#filepos165870), [[[184]{.underline}]{.calibre_10}](#index_split_028.html#filepos462905). [See also]{.italic} specific examples and problems

-   tests

    -   mocks, [[[184]{.underline}]{.calibre_10}](#index_split_028.html#filepos462905)--[[[186]{.underline}]{.calibre_10}](#index_split_028.html#filepos468867)

    -   property-based testing, [[[186]{.underline}]{.calibre_10}](#index_split_028.html#filepos468867)--[[[189]{.underline}]{.calibre_10}](#index_split_028.html#filepos476865)

-   threading macro ([` ->> `{.calibre4}]{.calibre_17}), [[[45]{.underline}]{.calibre_10}](#index_split_017.html#filepos145812), [[[46]{.underline}]{.calibre_10}](#index_split_017.html#filepos149963)

-   threads

    -   and race conditions, [[[216]{.underline}]{.calibre_10}](#index_split_030.html#filepos534691)

    -   usage, [[[9]{.underline}]{.calibre_10}](#index_split_013.html#filepos73129), [[[48]{.underline}]{.calibre_10}](#index_split_017.html#filepos155572)--[[[51]{.underline}]{.calibre_10}](#index_split_017.html#filepos163544)

-   TILT error message, [[[122]{.underline}]{.calibre_10}](#index_split_025.html#filepos323949)n

-   Turing, Alan, [[[xvi]{.underline}]{.calibre_10}](#index_split_009.html#filepos46603)--[[[xvii]{.underline}]{.calibre_10}](#index_split_009.html#filepos48837)

-   Turing machines, [[[xvi]{.underline}]{.calibre_10}](#index_split_009.html#filepos46603)--[[[xvii]{.underline}]{.calibre_10}](#index_split_009.html#filepos48837), [[[19]{.underline}]{.calibre_10}](#index_split_014.html#filepos92254)

-   turtle graphics

    -   command handling, [[[210]{.underline}]{.calibre_10}](#index_split_029.html#filepos525800)--[[[212]{.underline}]{.calibre_10}](#index_split_029.html#filepos531486)

    -   framework and drawing functions, [[[202]{.underline}]{.calibre_10}](#index_split_029.html#filepos507285)--[[[210]{.underline}]{.calibre_10}](#index_split_029.html#filepos525800)

    -   usage, [[[200]{.underline}]{.calibre_10}](#index_split_029.html#filepos502055)--[[[202]{.underline}]{.calibre_10}](#index_split_029.html#filepos507285)

-   turtles (printing devices), [[[200]{.underline}]{.calibre_10}](#index_split_029.html#filepos502055)--[[[201]{.underline}]{.calibre_10}](#index_split_029.html#filepos505754)

-   type integrity

    -   with [` clojure.spec `{.calibre4}]{.calibre_17} library, [[[110]{.underline}]{.calibre_10}](#index_split_023.html#filepos296903)--[[[113]{.underline}]{.calibre_10}](#index_split_023.html#filepos305961)

    -   with [` :pre `{.calibre4}]{.calibre_17} and [` :post `{.calibre4}]{.calibre_17}, [[[113]{.underline}]{.calibre_10}](#index_split_023.html#filepos305961)--[[[114]{.underline}]{.calibre_10}](#index_split_023.html#filepos309309)

-   type models, and Decorator pattern, [[[260]{.underline}]{.calibre_10}](#index_split_032.html#filepos630536)--[[[263]{.underline}]{.calibre_10}](#index_split_032.html#filepos638276)

-   type safety, [[[281]{.underline}]{.calibre_10}](#index_split_032.html#filepos684329)

-   types. [See also]{.italic}
    > [[[duck typing]{.underline}]{.calibre_10}](#index_split_036.html#filepos869317)

    -   in Liskov Substitution Principle, [[[139]{.underline}]{.calibre_10}](#index_split_026.html#filepos361624)

[[[U]{.calibre_3}]{.bold}]{.calibre1}

::: calibre_11
 
:::

-   Undo Command pattern, [[[245]{.underline}]{.calibre_10}](#index_split_032.html#filepos596823)--[[[249]{.underline}]{.calibre_10}](#index_split_032.html#filepos605382)

-   unified modeling language (UML) diagrams, [[[97]{.underline}]{.calibre_10}](#index_split_022.html#filepos266369)

-   [` union `{.calibre4}]{.calibre_17} function, [[[91]{.underline}]{.calibre_10}](#index_split_021.html#filepos254913)n8

-   [` update `{.calibre4}]{.calibre_17} function, [[[91]{.underline}]{.calibre_10}](#index_split_021.html#filepos254913)n7

[[[V]{.calibre_3}]{.bold}]{.calibre1}

::: calibre_11
 
:::

-   [` vals `{.calibre4}]{.calibre_17}, [[[91]{.underline}]{.calibre_10}](#index_split_021.html#filepos254913)n9

-   variables

    -   assignment, [[[7]{.underline}]{.calibre_10}](#index_split_013.html#filepos68020)--[[[8]{.underline}]{.calibre_10}](#index_split_013.html#filepos70428)

    -   in functional programs, [[[15]{.underline}]{.calibre_10}](#index_split_013.html#filepos89440)--[[[16]{.underline}]{.calibre_10}](#index_split_013.html#filepos89440), [[[18]{.underline}]{.calibre_10}](#index_split_014.html#filepos90221)--[[[19]{.underline}]{.calibre_10}](#index_split_014.html#filepos92254)

-   Video Store problem, [[[155]{.underline}]{.calibre_10}](#index_split_026.html#filepos402079)--[[[165]{.underline}]{.calibre_10}](#index_split_026.html#filepos425856), [[[166]{.underline}]{.calibre_10}](#index_split_026.html#filepos426907)--[[[179]{.underline}]{.calibre_10}](#index_split_026.html#filepos460156), [[[190]{.underline}]{.calibre_10}](#index_split_028.html#filepos479009)--[[[197]{.underline}]{.calibre_10}](#index_split_028.html#filepos499491)

-   Visitor pattern

    -   in shape example, [[[264]{.underline}]{.calibre_10}](#index_split_032.html#filepos641681)--[[[267]{.underline}]{.calibre_10}](#index_split_032.html#filepos649292), [[[268]{.underline}]{.calibre_10}](#index_split_032.html#filepos651668)--[[[270]{.underline}]{.calibre_10}](#index_split_032.html#filepos656543), [[[271]{.underline}]{.calibre_10}](#index_split_032.html#filepos658766)--[[[273]{.underline}]{.calibre_10}](#index_split_032.html#filepos665792)

    -   usage, [[[264]{.underline}]{.calibre_10}](#index_split_032.html#filepos641681)

-   vtables, [[[134]{.underline}]{.calibre_10}](#index_split_026.html#filepos348780), [[[139]{.underline}]{.calibre_10}](#index_split_026.html#filepos361624), [[[235]{.underline}]{.calibre_10}](#index_split_032.html#filepos573383)

[[[W]{.calibre_3}]{.bold}]{.calibre1}

::: calibre_11
 
:::

-   Wa-Tor app

    -   10x10 test, [[[322]{.underline}]{.calibre_10}](#index_split_034.html#filepos781959)--[[[323]{.underline}]{.calibre_10}](#index_split_034.html#filepos786064)

    -   actors, [[[288]{.underline}]{.calibre_10}](#index_split_034.html#filepos691974)--[[[289]{.underline}]{.calibre_10}](#index_split_034.html#filepos694682)

    -   Factory Method solution, [[[312]{.underline}]{.calibre_10}](#index_split_034.html#filepos752976)--[[[322]{.underline}]{.calibre_10}](#index_split_034.html#filepos781959)

    -   fish movement behavior, [[[295]{.underline}]{.calibre_10}](#index_split_034.html#filepos709869)--[[[305]{.underline}]{.calibre_10}](#index_split_034.html#filepos733849)

    -   fish reproduction behavior, [[[305]{.underline}]{.calibre_10}](#index_split_034.html#filepos733849)--[[[309]{.underline}]{.calibre_10}](#index_split_034.html#filepos745467)

    -   as functional and object oriented, [[[335]{.underline}]{.calibre_10}](#index_split_034.html#filepos820888)--[[[336]{.underline}]{.calibre_10}](#index_split_034.html#filepos821960)

    -   game concept, [[[288]{.underline}]{.calibre_10}](#index_split_034.html#filepos691974)

    -   objects, [[[289]{.underline}]{.calibre_10}](#index_split_034.html#filepos694682)--[[[292]{.underline}]{.calibre_10}](#index_split_034.html#filepos701127)

    -   screenshot, [[[335]{.underline}]{.calibre_10}](#index_split_034.html#filepos820888)

    -   shark class, [[[324]{.underline}]{.calibre_10}](#index_split_034.html#filepos788288)--[[[334]{.underline}]{.calibre_10}](#index_split_034.html#filepos820245)

    -   water behavior, [[[293]{.underline}]{.calibre_10}](#index_split_034.html#filepos703607)--[[[295]{.underline}]{.calibre_10}](#index_split_034.html#filepos709869)

    -   world dependency, [[[309]{.underline}]{.calibre_10}](#index_split_034.html#filepos745467)--[[[312]{.underline}]{.calibre_10}](#index_split_034.html#filepos752976)

[[[Y]{.calibre_3}]{.bold}]{.calibre1}

::: calibre_11
 
:::

-   YAGNI (You Aren't Gonna Need It), [[[292]{.underline}]{.calibre_10}](#index_split_034.html#filepos701127)n

::: {#index_split_036.html#calibre_pb_36 .mbp_pagebreak}
:::

[]{#index_split_037.html}

![](images/00140.jpg){.calibre_98}

::: {#index_split_037.html#calibre_pb_37 .mbp_pagebreak}
:::

[]{#index_split_038.html}

[[[Code Snippets]{.calibre_3}]{.bold}]{.calibre1}

Many titles include programming code or configuration examples. To optimize the presentation of these elements, view the eBook in single-column, landscape mode and adjust the font size to the smallest setting. In addition to presenting code and configurations in the reflowable text format, we have included images of the code that mimic the presentation found in the print book; therefore, where the reflowable format may compromise the presentation of the code listing, you will see a "Click here to view code image" link. Click the link to view the print-fidelity code image. To return to the previous page viewed, click the Back button on your device or app.

::: {#index_split_038.html#calibre_pb_38 .mbp_pagebreak}
:::

[]{#index_split_039.html}

![](images/00262.jpg){#filepos956896 .calibre_99}

::: {#index_split_039.html#calibre_pb_39 .mbp_pagebreak}
:::

[]{#index_split_040.html}

![](images/00337.jpg){#filepos957042 .calibre_100}

::: {#index_split_040.html#calibre_pb_40 .mbp_pagebreak}
:::

[]{#index_split_041.html}

![](images/00358.jpg){#filepos957188 .calibre_101}

::: {#index_split_041.html#calibre_pb_41 .mbp_pagebreak}
:::

[]{#index_split_042.html}

![](images/00022.jpg){#filepos957334 .calibre_102}

::: {#index_split_042.html#calibre_pb_42 .mbp_pagebreak}
:::

[]{#index_split_043.html}

![](images/00055.jpg){#filepos957479 .calibre_103}

::: {#index_split_043.html#calibre_pb_43 .mbp_pagebreak}
:::

[]{#index_split_044.html}

![](images/00366.jpg){#filepos957625 .calibre_104}

::: {#index_split_044.html#calibre_pb_44 .mbp_pagebreak}
:::

[]{#index_split_045.html}

![](images/00131.jpg){#filepos957770 .calibre_105}

::: {#index_split_045.html#calibre_pb_45 .mbp_pagebreak}
:::

[]{#index_split_046.html}

![](images/00159.jpg){#filepos957916 .calibre_106}

::: {#index_split_046.html#calibre_pb_46 .mbp_pagebreak}
:::

[]{#index_split_047.html}

![](images/00195.jpg){#filepos958061 .calibre_107}

::: {#index_split_047.html#calibre_pb_47 .mbp_pagebreak}
:::

[]{#index_split_048.html}

![](images/00227.jpg){#filepos958206 .calibre_108}

::: {#index_split_048.html#calibre_pb_48 .mbp_pagebreak}
:::

[]{#index_split_049.html}

![](images/00264.jpg){.calibre_109}

::: {#index_split_049.html#calibre_pb_49 .mbp_pagebreak}
:::

[]{#index_split_050.html}

![](images/00296.jpg){.calibre_110}

::: {#index_split_050.html#calibre_pb_50 .mbp_pagebreak}
:::

[]{#index_split_051.html}

![](images/00326.jpg){#filepos958629 .calibre_111}

::: {#index_split_051.html#calibre_pb_51 .mbp_pagebreak}
:::

[]{#index_split_052.html}

![](images/00001.jpg){#filepos958775 .calibre_112}

::: {#index_split_052.html#calibre_pb_52 .mbp_pagebreak}
:::

[]{#index_split_053.html}

![](images/00086.jpg){.calibre_113}

::: {#index_split_053.html#calibre_pb_53 .mbp_pagebreak}
:::

[]{#index_split_054.html}

![](images/00074.jpg){#filepos959052 .calibre_114}

::: {#index_split_054.html#calibre_pb_54 .mbp_pagebreak}
:::

[]{#index_split_055.html}

![](images/00104.jpg){#filepos959198 .calibre_115}

::: {#index_split_055.html#calibre_pb_55 .mbp_pagebreak}
:::

[]{#index_split_056.html}

![](images/00139.jpg){#filepos959343 .calibre_116}

::: {#index_split_056.html#calibre_pb_56 .mbp_pagebreak}
:::

[]{#index_split_057.html}

![](images/00174.jpg){#filepos959489 .calibre_117}

::: {#index_split_057.html#calibre_pb_57 .mbp_pagebreak}
:::

[]{#index_split_058.html}

![](images/00204.jpg){#filepos959634 .calibre_118}

::: {#index_split_058.html#calibre_pb_58 .mbp_pagebreak}
:::

[]{#index_split_059.html}

![](images/00237.jpg){#filepos959779 .calibre_119}

::: {#index_split_059.html#calibre_pb_59 .mbp_pagebreak}
:::

[]{#index_split_060.html}

![](images/00277.jpg){#filepos959925 .calibre_120}

::: {#index_split_060.html#calibre_pb_60 .mbp_pagebreak}
:::

[]{#index_split_061.html}

![](images/00308.jpg){#filepos960071 .calibre_121}

::: {#index_split_061.html#calibre_pb_61 .mbp_pagebreak}
:::

[]{#index_split_062.html}

![](images/00325.jpg){.calibre_122}

::: {#index_split_062.html#calibre_pb_62 .mbp_pagebreak}
:::

[]{#index_split_063.html}

![](images/00170.jpg){#filepos960363 .calibre_123}

::: {#index_split_063.html#calibre_pb_63 .mbp_pagebreak}
:::

[]{#index_split_064.html}

![](images/00057.jpg){#filepos960509 .calibre_122}

::: {#index_split_064.html#calibre_pb_64 .mbp_pagebreak}
:::

[]{#index_split_065.html}

![](images/00092.jpg){#filepos960640 .calibre_124}

::: {#index_split_065.html#calibre_pb_65 .mbp_pagebreak}
:::

[]{#index_split_066.html}

![](images/00124.jpg){#filepos960786 .calibre_125}

::: {#index_split_066.html#calibre_pb_66 .mbp_pagebreak}
:::

[]{#index_split_067.html}

![](images/00163.jpg){#filepos960931 .calibre_126}

::: {#index_split_067.html#calibre_pb_67 .mbp_pagebreak}
:::

[]{#index_split_068.html}

![](images/00196.jpg){#filepos961076 .calibre_127}

::: {#index_split_068.html#calibre_pb_68 .mbp_pagebreak}
:::

[]{#index_split_069.html}

![](images/00231.jpg){#filepos961206 .calibre_128}

::: {#index_split_069.html#calibre_pb_69 .mbp_pagebreak}
:::

[]{#index_split_070.html}

![](images/00267.jpg){#filepos961351 .calibre_129}

::: {#index_split_070.html#calibre_pb_70 .mbp_pagebreak}
:::

[]{#index_split_071.html}

![](images/00299.jpg){#filepos961497 .calibre_130}

::: {#index_split_071.html#calibre_pb_71 .mbp_pagebreak}
:::

[]{#index_split_072.html}

![](images/00329.jpg){#filepos961643 .calibre_131}

::: {#index_split_072.html#calibre_pb_72 .mbp_pagebreak}
:::

[]{#index_split_073.html}

![](images/00027.jpg){#filepos961789 .calibre_132}

::: {#index_split_073.html#calibre_pb_73 .mbp_pagebreak}
:::

[]{#index_split_074.html}

![](images/00051.jpg){#filepos961919 .calibre_133}

::: {#index_split_074.html#calibre_pb_74 .mbp_pagebreak}
:::

[]{#index_split_075.html}

![](images/00106.jpg){#filepos962065 .calibre_134}

::: {#index_split_075.html#calibre_pb_75 .mbp_pagebreak}
:::

[]{#index_split_076.html}

![](images/00156.jpg){#filepos962210 .calibre_135}

::: {#index_split_076.html#calibre_pb_76 .mbp_pagebreak}
:::

[]{#index_split_077.html}

![](images/00186.jpg){#filepos962355 .calibre_136}

::: {#index_split_077.html#calibre_pb_77 .mbp_pagebreak}
:::

[]{#index_split_078.html}

![](images/00239.jpg){#filepos962501 .calibre_137}

::: {#index_split_078.html#calibre_pb_78 .mbp_pagebreak}
:::

[]{#index_split_079.html}

![](images/00301.jpg){#filepos962646 .calibre_138}

::: {#index_split_079.html#calibre_pb_79 .mbp_pagebreak}
:::

[]{#index_split_080.html}

![](images/00321.jpg){#filepos962792 .calibre_139}

::: {#index_split_080.html#calibre_pb_80 .mbp_pagebreak}
:::

[]{#index_split_081.html}

![](images/00009.jpg){#filepos962937 .calibre_140}

::: {#index_split_081.html#calibre_pb_81 .mbp_pagebreak}
:::

[]{#index_split_082.html}

![](images/00069.jpg){#filepos963083 .calibre_141}

::: {#index_split_082.html#calibre_pb_82 .mbp_pagebreak}
:::

[]{#index_split_083.html}

![](images/00093.jpg){#filepos963228 .calibre_142}

::: {#index_split_083.html#calibre_pb_83 .mbp_pagebreak}
:::

[]{#index_split_084.html}

![](images/00148.jpg){#filepos963373 .calibre_140}

::: {#index_split_084.html#calibre_pb_84 .mbp_pagebreak}
:::

[]{#index_split_085.html}

![](images/00207.jpg){#filepos963519 .calibre_143}

::: {#index_split_085.html#calibre_pb_85 .mbp_pagebreak}
:::

[]{#index_split_086.html}

![](images/00232.jpg){#filepos963664 .calibre_144}

::: {#index_split_086.html#calibre_pb_86 .mbp_pagebreak}
:::

[]{#index_split_087.html}

![](images/00287.jpg){#filepos963810 .calibre_145}

::: {#index_split_087.html#calibre_pb_87 .mbp_pagebreak}
:::

[]{#index_split_088.html}

![](images/00342.jpg){#filepos963956 .calibre_146}

::: {#index_split_088.html#calibre_pb_88 .mbp_pagebreak}
:::

[]{#index_split_089.html}

![](images/00002.jpg){#filepos964102 .calibre_147}

::: {#index_split_089.html#calibre_pb_89 .mbp_pagebreak}
:::

[]{#index_split_090.html}

![](images/00037.jpg){#filepos964247 .calibre_148}

::: {#index_split_090.html#calibre_pb_90 .mbp_pagebreak}
:::

[]{#index_split_091.html}

![](images/00070.jpg){#filepos964392 .calibre_149}

::: {#index_split_091.html#calibre_pb_91 .mbp_pagebreak}
:::

[]{#index_split_092.html}

![](images/00128.jpg){#filepos964537 .calibre_150}

::: {#index_split_092.html#calibre_pb_92 .mbp_pagebreak}
:::

[]{#index_split_093.html}

![](images/00187.jpg){#filepos964682 .calibre_151}

::: {#index_split_093.html#calibre_pb_93 .mbp_pagebreak}
:::

[]{#index_split_094.html}

![](images/00208.jpg){#filepos964828 .calibre_152}

::: {#index_split_094.html#calibre_pb_94 .mbp_pagebreak}
:::

[]{#index_split_095.html}

![](images/00273.jpg){#filepos964973 .calibre_153}

::: {#index_split_095.html#calibre_pb_95 .mbp_pagebreak}
:::

[]{#index_split_096.html}

![](images/00317.jpg){#filepos965119 .calibre_154}

::: {#index_split_096.html#calibre_pb_96 .mbp_pagebreak}
:::

[]{#index_split_097.html}

![](images/00343.jpg){#filepos965250 .calibre_155}

::: {#index_split_097.html#calibre_pb_97 .mbp_pagebreak}
:::

[]{#index_split_098.html}

![](images/00039.jpg){#filepos965396 .calibre_156}

::: {#index_split_098.html#calibre_pb_98 .mbp_pagebreak}
:::

[]{#index_split_099.html}

![](images/00095.jpg){#filepos965541 .calibre_157}

::: {#index_split_099.html#calibre_pb_99 .mbp_pagebreak}
:::

[]{#index_split_100.html}

![](images/00117.jpg){#filepos965687 .calibre_158}

::: {#index_split_100.html#calibre_pb_100 .mbp_pagebreak}
:::

[]{#index_split_101.html}

![](images/00171.jpg){#filepos965832 .calibre_159}

::: {#index_split_101.html#calibre_pb_101 .mbp_pagebreak}
:::

[]{#index_split_102.html}

![](images/00226.jpg){#filepos965978 .calibre_160}

::: {#index_split_102.html#calibre_pb_102 .mbp_pagebreak}
:::

[]{#index_split_103.html}

![](images/00249.jpg){#filepos966124 .calibre_161}

::: {#index_split_103.html#calibre_pb_103 .mbp_pagebreak}
:::

[]{#index_split_104.html}

![](images/00314.jpg){#filepos966270 .calibre_162}

::: {#index_split_104.html#calibre_pb_104 .mbp_pagebreak}
:::

[]{#index_split_105.html}

![](images/00003.jpg){#filepos966416 .calibre_163}

::: {#index_split_105.html#calibre_pb_105 .mbp_pagebreak}
:::

[]{#index_split_106.html}

![](images/00021.jpg){#filepos966562 .calibre_164}

::: {#index_split_106.html#calibre_pb_106 .mbp_pagebreak}
:::

[]{#index_split_107.html}

![](images/00081.jpg){#filepos966708 .calibre_165}

::: {#index_split_107.html#calibre_pb_107 .mbp_pagebreak}
:::

[]{#index_split_108.html}

![](images/00136.jpg){#filepos966854 .calibre_166}

::: {#index_split_108.html#calibre_pb_108 .mbp_pagebreak}
:::

[]{#index_split_109.html}

![](images/00158.jpg){.calibre_167}

::: {#index_split_109.html#calibre_pb_109 .mbp_pagebreak}
:::

[]{#index_split_110.html}

![](images/00221.jpg){#filepos967146 .calibre_168}

::: {#index_split_110.html#calibre_pb_110 .mbp_pagebreak}
:::

[]{#index_split_111.html}

![](images/00279.jpg){#filepos967291 .calibre_150}

::: {#index_split_111.html#calibre_pb_111 .mbp_pagebreak}
:::

[]{#index_split_112.html}

![](images/00295.jpg){#filepos967436 .calibre_169}

::: {#index_split_112.html#calibre_pb_112 .mbp_pagebreak}
:::

[]{#index_split_113.html}

![](images/00356.jpg){#filepos967581 .calibre_170}

::: {#index_split_113.html#calibre_pb_113 .mbp_pagebreak}
:::

[]{#index_split_114.html}

![](images/00049.jpg){#filepos967727 .calibre_171}

::: {#index_split_114.html#calibre_pb_114 .mbp_pagebreak}
:::

[]{#index_split_115.html}

![](images/00072.jpg){#filepos967873 .calibre_172}

::: {#index_split_115.html#calibre_pb_115 .mbp_pagebreak}
:::

[]{#index_split_116.html}

![](images/00350.jpg){#filepos968019 .calibre_169}

::: {#index_split_116.html#calibre_pb_116 .mbp_pagebreak}
:::

[]{#index_split_117.html}

![](images/00190.jpg){#filepos968164 .calibre_173}

::: {#index_split_117.html#calibre_pb_117 .mbp_pagebreak}
:::

[]{#index_split_118.html}

![](images/00203.jpg){#filepos968310 .calibre_174}

::: {#index_split_118.html#calibre_pb_118 .mbp_pagebreak}
:::

[]{#index_split_119.html}

![](images/00265.jpg){#filepos968455 .calibre_175}

::: {#index_split_119.html#calibre_pb_119 .mbp_pagebreak}
:::

[]{#index_split_120.html}

![](images/00319.jpg){#filepos968585 .calibre_176}

::: {#index_split_120.html#calibre_pb_120 .mbp_pagebreak}
:::

[]{#index_split_121.html}

![](images/00345.jpg){.calibre_177}

::: {#index_split_121.html#calibre_pb_121 .mbp_pagebreak}
:::

[]{#index_split_122.html}

![](images/00270.jpg){.calibre_178}

::: {#index_split_122.html#calibre_pb_122 .mbp_pagebreak}
:::

[]{#index_split_123.html}

![](images/00091.jpg){.calibre_179}

::: {#index_split_123.html#calibre_pb_123 .mbp_pagebreak}
:::

[]{#index_split_124.html}

![](images/00115.jpg){.calibre_180}

::: {#index_split_124.html#calibre_pb_124 .mbp_pagebreak}
:::

[]{#index_split_125.html}

![](images/00175.jpg){#filepos969315 .calibre_181}

::: {#index_split_125.html#calibre_pb_125 .mbp_pagebreak}
:::

[]{#index_split_126.html}

![](images/00230.jpg){#filepos969461 .calibre_182}

::: {#index_split_126.html#calibre_pb_126 .mbp_pagebreak}
:::

[]{#index_split_127.html}

![](images/00252.jpg){#filepos969607 .calibre_183}

::: {#index_split_127.html#calibre_pb_127 .mbp_pagebreak}
:::

[]{#index_split_128.html}

![](images/00309.jpg){#filepos969754 .calibre_184}

::: {#index_split_128.html#calibre_pb_128 .mbp_pagebreak}
:::

[]{#index_split_129.html}

![](images/00353.jpg){#filepos969900 .calibre_185}

::: {#index_split_129.html#calibre_pb_129 .mbp_pagebreak}
:::

[]{#index_split_130.html}

![](images/00034.jpg){.calibre_186}

::: {#index_split_130.html#calibre_pb_130 .mbp_pagebreak}
:::

[]{#index_split_131.html}

![](images/00084.jpg){.calibre_187}

::: {#index_split_131.html#calibre_pb_131 .mbp_pagebreak}
:::

[]{#index_split_132.html}

![](images/00164.jpg){#filepos970338 .calibre_188}

::: {#index_split_132.html#calibre_pb_132 .mbp_pagebreak}
:::

[]{#index_split_133.html}

![](images/00176.jpg){#filepos970469 .calibre_189}

::: {#index_split_133.html#calibre_pb_133 .mbp_pagebreak}
:::

[]{#index_split_134.html}

![](images/00214.jpg){#filepos970615 .calibre_190}

::: {#index_split_134.html#calibre_pb_134 .mbp_pagebreak}
:::

[]{#index_split_135.html}

![](images/00300.jpg){#filepos970761 .calibre_191}

::: {#index_split_135.html#calibre_pb_135 .mbp_pagebreak}
:::

[]{#index_split_136.html}

![](images/00310.jpg){#filepos970907 .calibre_192}

::: {#index_split_136.html#calibre_pb_136 .mbp_pagebreak}
:::

[]{#index_split_137.html}

![](images/00361.jpg){#filepos971053 .calibre_193}

::: {#index_split_137.html#calibre_pb_137 .mbp_pagebreak}
:::

[]{#index_split_138.html}

![](images/00068.jpg){#filepos971199 .calibre_194}

::: {#index_split_138.html#calibre_pb_138 .mbp_pagebreak}
:::

[]{#index_split_139.html}

![](images/00085.jpg){#filepos971345 .calibre_195}

::: {#index_split_139.html#calibre_pb_139 .mbp_pagebreak}
:::

[]{#index_split_140.html}

![](images/00125.jpg){#filepos971491 .calibre_196}

::: {#index_split_140.html#calibre_pb_140 .mbp_pagebreak}
:::

[]{#index_split_141.html}

![](images/00206.jpg){#filepos971636 .calibre_197}

::: {#index_split_141.html#calibre_pb_141 .mbp_pagebreak}
:::

[]{#index_split_142.html}

![](images/00215.jpg){#filepos971767 .calibre_198}

::: {#index_split_142.html#calibre_pb_142 .mbp_pagebreak}
:::

[]{#index_split_143.html}

![](images/00268.jpg){.calibre_199}

::: {#index_split_143.html#calibre_pb_143 .mbp_pagebreak}
:::

[]{#index_split_144.html}

![](images/00340.jpg){#filepos972059 .calibre_200}

::: {#index_split_144.html#calibre_pb_144 .mbp_pagebreak}
:::

[]{#index_split_145.html}

![](images/00362.jpg){#filepos972205 .calibre_201}

::: {#index_split_145.html#calibre_pb_145 .mbp_pagebreak}
:::

[]{#index_split_146.html}

![](images/00035.jpg){#filepos972336 .calibre_202}

::: {#index_split_146.html#calibre_pb_146 .mbp_pagebreak}
:::

[]{#index_split_147.html}

![](images/00116.jpg){.calibre_203}

::: {#index_split_147.html#calibre_pb_147 .mbp_pagebreak}
:::

[]{#index_split_148.html}

![](images/00126.jpg){#filepos972628 .calibre_185}

::: {#index_split_148.html#calibre_pb_148 .mbp_pagebreak}
:::

[]{#index_split_149.html}

![](images/00177.jpg){.calibre_204}

::: {#index_split_149.html#calibre_pb_149 .mbp_pagebreak}
:::

[]{#index_split_150.html}

![](images/00248.jpg){#filepos972920 .calibre_205}

::: {#index_split_150.html#calibre_pb_150 .mbp_pagebreak}
:::

[]{#index_split_151.html}

![](images/00269.jpg){#filepos973050 .calibre_206}

::: {#index_split_151.html#calibre_pb_151 .mbp_pagebreak}
:::

[]{#index_split_152.html}

![](images/00311.jpg){.calibre_207}

::: {#index_split_152.html#calibre_pb_152 .mbp_pagebreak}
:::

[]{#index_split_153.html}

![](images/00028.jpg){#filepos973343 .calibre_208}

::: {#index_split_153.html#calibre_pb_153 .mbp_pagebreak}
:::

[]{#index_split_154.html}

![](images/00038.jpg){#filepos973489 .calibre_209}

::: {#index_split_154.html#calibre_pb_154 .mbp_pagebreak}
:::

[]{#index_split_155.html}

![](images/00271.jpg){#filepos973635 .calibre_210}

::: {#index_split_155.html#calibre_pb_155 .mbp_pagebreak}
:::

[]{#index_split_156.html}

![](images/00367.jpg){.calibre_211}

::: {#index_split_156.html#calibre_pb_156 .mbp_pagebreak}
:::

[]{#index_split_157.html}

![](images/00157.jpg){#filepos973927 .calibre_212}

::: {#index_split_157.html#calibre_pb_157 .mbp_pagebreak}
:::

[]{#index_split_158.html}

![](images/00302.jpg){.calibre_213}

::: {#index_split_158.html#calibre_pb_158 .mbp_pagebreak}
:::

[]{#index_split_159.html}

![](images/00217.jpg){#filepos974219 .calibre_214}

::: {#index_split_159.html#calibre_pb_159 .mbp_pagebreak}
:::

[]{#index_split_160.html}

![](images/00313.jpg){#filepos974365 .calibre_215}

::: {#index_split_160.html#calibre_pb_160 .mbp_pagebreak}
:::

[]{#index_split_161.html}

![](images/00355.jpg){#filepos974510 .calibre_216}

::: {#index_split_161.html#calibre_pb_161 .mbp_pagebreak}
:::

[]{#index_split_162.html}

![](images/00071.jpg){#filepos974656 .calibre_217}

::: {#index_split_162.html#calibre_pb_162 .mbp_pagebreak}
:::

[]{#index_split_163.html}

![](images/00080.jpg){#filepos974802 .calibre_218}

::: {#index_split_163.html#calibre_pb_163 .mbp_pagebreak}
:::

[]{#index_split_164.html}

![](images/00129.jpg){#filepos974948 .calibre_219}

::: {#index_split_164.html#calibre_pb_164 .mbp_pagebreak}
:::

[]{#index_split_165.html}

![](images/00209.jpg){#filepos975094 .calibre_220}

::: {#index_split_165.html#calibre_pb_165 .mbp_pagebreak}
:::

[]{#index_split_166.html}

![](images/00218.jpg){#filepos975240 .calibre_221}

::: {#index_split_166.html#calibre_pb_166 .mbp_pagebreak}
:::

[]{#index_split_167.html}

![](images/00261.jpg){#filepos975385 .calibre_222}

::: {#index_split_167.html#calibre_pb_167 .mbp_pagebreak}
:::

[]{#index_split_168.html}

![](images/00344.jpg){#filepos975531 .calibre_223}

::: {#index_split_168.html#calibre_pb_168 .mbp_pagebreak}
:::

[]{#index_split_169.html}

![](images/00357.jpg){#filepos975677 .calibre_224}

::: {#index_split_169.html#calibre_pb_169 .mbp_pagebreak}
:::

[]{#index_split_170.html}

![](images/00040.jpg){#filepos975822 .calibre_225}

::: {#index_split_170.html#calibre_pb_170 .mbp_pagebreak}
:::

[]{#index_split_171.html}

![](images/00113.jpg){#filepos975968 .calibre_226}

::: {#index_split_171.html#calibre_pb_171 .mbp_pagebreak}
:::

[]{#index_split_172.html}

![](images/00130.jpg){#filepos976114 .calibre_227}

::: {#index_split_172.html#calibre_pb_172 .mbp_pagebreak}
:::

[]{#index_split_173.html}

![](images/00172.jpg){#filepos976259 .calibre_117}

::: {#index_split_173.html#calibre_pb_173 .mbp_pagebreak}
:::

[]{#index_split_174.html}

![](images/00250.jpg){#filepos976404 .calibre_228}

::: {#index_split_174.html#calibre_pb_174 .mbp_pagebreak}
:::

[]{#index_split_175.html}

![](images/00263.jpg){#filepos976549 .calibre_229}

::: {#index_split_175.html#calibre_pb_175 .mbp_pagebreak}
:::

[]{#index_split_176.html}

![](images/00338.jpg){#filepos976695 .calibre_230}

::: {#index_split_176.html#calibre_pb_176 .mbp_pagebreak}
:::

[]{#index_split_177.html}

![](images/00023.jpg){#filepos976840 .calibre_231}

::: {#index_split_177.html#calibre_pb_177 .mbp_pagebreak}
:::

[]{#index_split_178.html}

![](images/00041.jpg){.calibre_232}

::: {#index_split_178.html#calibre_pb_178 .mbp_pagebreak}
:::

[]{#index_split_179.html}

![](images/00082.jpg){#filepos977132 .calibre_233}

::: {#index_split_179.html#calibre_pb_179 .mbp_pagebreak}
:::

[]{#index_split_180.html}

![](images/00160.jpg){.calibre_234}

::: {#index_split_180.html#calibre_pb_180 .mbp_pagebreak}
:::

[]{#index_split_181.html}

![](images/00173.jpg){#filepos977424 .calibre_235}

::: {#index_split_181.html#calibre_pb_181 .mbp_pagebreak}
:::

[]{#index_split_182.html}

![](images/00222.jpg){.calibre_236}

::: {#index_split_182.html#calibre_pb_182 .mbp_pagebreak}
:::

[]{#index_split_183.html}

![](images/00297.jpg){#filepos977716 .calibre_237}

::: {#index_split_183.html#calibre_pb_183 .mbp_pagebreak}
:::

[]{#index_split_184.html}

![](images/00352.jpg){#filepos977863 .calibre_238}

::: {#index_split_184.html#calibre_pb_184 .mbp_pagebreak}
:::

[]{#index_split_185.html}

![](images/00359.jpg){#filepos978009 .calibre_239}

::: {#index_split_185.html#calibre_pb_185 .mbp_pagebreak}
:::

[]{#index_split_186.html}

![](images/00075.jpg){#filepos978155 .calibre_240}

::: {#index_split_186.html#calibre_pb_186 .mbp_pagebreak}
:::

[]{#index_split_187.html}

![](images/00083.jpg){#filepos978301 .calibre_241}

::: {#index_split_187.html#calibre_pb_187 .mbp_pagebreak}
:::

[]{#index_split_188.html}

![](images/00180.jpg){#filepos978447 .calibre_242}

::: {#index_split_188.html#calibre_pb_188 .mbp_pagebreak}
:::

[]{#index_split_189.html}

![](images/00205.jpg){#filepos978593 .calibre_243}

::: {#index_split_189.html#calibre_pb_189 .mbp_pagebreak}
:::

[]{#index_split_190.html}

![](images/00219.jpg){#filepos978739 .calibre_244}

::: {#index_split_190.html#calibre_pb_190 .mbp_pagebreak}
:::

[]{#index_split_191.html}

![](images/00266.jpg){.calibre_245}

::: {#index_split_191.html#calibre_pb_191 .mbp_pagebreak}
:::

[]{#index_split_192.html}

![](images/00341.jpg){#filepos979032 .calibre_190}

::: {#index_split_192.html#calibre_pb_192 .mbp_pagebreak}
:::

[]{#index_split_193.html}

![](images/00360.jpg){#filepos979178 .calibre_246}

::: {#index_split_193.html#calibre_pb_193 .mbp_pagebreak}
:::

[]{#index_split_194.html}

![](images/00058.jpg){#filepos979324 .calibre_247}

::: {#index_split_194.html#calibre_pb_194 .mbp_pagebreak}
:::

[]{#index_split_195.html}

![](images/00105.jpg){#filepos979470 .calibre_248}

::: {#index_split_195.html#calibre_pb_195 .mbp_pagebreak}
:::

[]{#index_split_196.html}

![](images/00145.jpg){#filepos979616 .calibre_249}

::: {#index_split_196.html#calibre_pb_196 .mbp_pagebreak}
:::

[]{#index_split_197.html}

![](images/00197.jpg){#filepos979762 .calibre_108}

::: {#index_split_197.html#calibre_pb_197 .mbp_pagebreak}
:::

[]{#index_split_198.html}

![](images/00238.jpg){.calibre_250}

::: {#index_split_198.html#calibre_pb_198 .mbp_pagebreak}
:::

[]{#index_split_199.html}

![](images/00290.jpg){#filepos980054 .calibre_251}

::: {#index_split_199.html#calibre_pb_199 .mbp_pagebreak}
:::

[]{#index_split_200.html}

![](images/00330.jpg){#filepos980185 .calibre_252}

::: {#index_split_200.html#calibre_pb_200 .mbp_pagebreak}
:::

[]{#index_split_201.html}

![](images/00012.jpg){#filepos980331 .calibre_253}

::: {#index_split_201.html#calibre_pb_201 .mbp_pagebreak}
:::

[]{#index_split_202.html}

![](images/00059.jpg){#filepos980477 .calibre_254}

::: {#index_split_202.html#calibre_pb_202 .mbp_pagebreak}
:::

[]{#index_split_203.html}

![](images/00107.jpg){#filepos980623 .calibre_255}

::: {#index_split_203.html#calibre_pb_203 .mbp_pagebreak}
:::

[]{#index_split_204.html}

![](images/00147.jpg){#filepos980769 .calibre_252}

::: {#index_split_204.html#calibre_pb_204 .mbp_pagebreak}
:::

[]{#index_split_205.html}

![](images/00199.jpg){#filepos980915 .calibre_256}

::: {#index_split_205.html#calibre_pb_205 .mbp_pagebreak}
:::

[]{#index_split_206.html}

![](images/00240.jpg){#filepos981061 .calibre_257}

::: {#index_split_206.html#calibre_pb_206 .mbp_pagebreak}
:::

[]{#index_split_207.html}

![](images/00286.jpg){#filepos981207 .calibre_182}

::: {#index_split_207.html#calibre_pb_207 .mbp_pagebreak}
:::

[]{#index_split_208.html}

![](images/00332.jpg){#filepos981353 .calibre_258}

::: {#index_split_208.html#calibre_pb_208 .mbp_pagebreak}
:::

[]{#index_split_209.html}

![](images/00010.jpg){.calibre_259}

::: {#index_split_209.html#calibre_pb_209 .mbp_pagebreak}
:::

[]{#index_split_210.html}

![](images/00060.jpg){#filepos981645 .calibre_260}

::: {#index_split_210.html#calibre_pb_210 .mbp_pagebreak}
:::

[]{#index_split_211.html}

![](images/00101.jpg){#filepos981791 .calibre_261}

::: {#index_split_211.html#calibre_pb_211 .mbp_pagebreak}
:::

[]{#index_split_212.html}

![](images/00149.jpg){#filepos981937 .calibre_262}

::: {#index_split_212.html#calibre_pb_212 .mbp_pagebreak}
:::

[]{#index_split_213.html}

![](images/00200.jpg){#filepos982083 .calibre_263}

::: {#index_split_213.html#calibre_pb_213 .mbp_pagebreak}
:::

[]{#index_split_214.html}

![](images/00242.jpg){#filepos982214 .calibre_264}

::: {#index_split_214.html#calibre_pb_214 .mbp_pagebreak}
:::

[]{#index_split_215.html}

![](images/00008.jpg){#filepos982360 .calibre_265}

::: {#index_split_215.html#calibre_pb_215 .mbp_pagebreak}
:::

[]{#index_split_216.html}

![](images/00235.jpg){#filepos982505 .calibre_266}

::: {#index_split_216.html#calibre_pb_216 .mbp_pagebreak}
:::

[]{#index_split_217.html}

![](images/00014.jpg){#filepos982651 .calibre_267}

::: {#index_split_217.html#calibre_pb_217 .mbp_pagebreak}
:::

[]{#index_split_218.html}

![](images/00334.jpg){#filepos982798 .calibre_268}

::: {#index_split_218.html#calibre_pb_218 .mbp_pagebreak}
:::

[]{#index_split_219.html}

![](images/00108.jpg){#filepos982944 .calibre_118}

::: {#index_split_219.html#calibre_pb_219 .mbp_pagebreak}
:::

[]{#index_split_220.html}

![](images/00063.jpg){#filepos983089 .calibre_269}

::: {#index_split_220.html#calibre_pb_220 .mbp_pagebreak}
:::

[]{#index_split_221.html}

![](images/00292.jpg){.calibre_270}

::: {#index_split_221.html#calibre_pb_221 .mbp_pagebreak}
:::

[]{#index_split_222.html}

![](images/00154.jpg){#filepos983381 .calibre_271}

::: {#index_split_222.html#calibre_pb_222 .mbp_pagebreak}
:::

[]{#index_split_223.html}

![](images/00020.jpg){#filepos983527 .calibre_272}

::: {#index_split_223.html#calibre_pb_223 .mbp_pagebreak}
:::

[]{#index_split_224.html}

![](images/00246.jpg){.calibre_273}

::: {#index_split_224.html#calibre_pb_224 .mbp_pagebreak}
:::

[]{#index_split_225.html}

![](images/00015.jpg){#filepos983819 .calibre_274}

::: {#index_split_225.html#calibre_pb_225 .mbp_pagebreak}
:::

[]{#index_split_226.html}

![](images/00349.jpg){#filepos983950 .calibre_275}

::: {#index_split_226.html#calibre_pb_226 .mbp_pagebreak}
:::

[]{#index_split_227.html}

![](images/00109.jpg){#filepos984096 .calibre_239}

::: {#index_split_227.html#calibre_pb_227 .mbp_pagebreak}
:::

[]{#index_split_228.html}

![](images/00077.jpg){#filepos984242 .calibre_276}

::: {#index_split_228.html#calibre_pb_228 .mbp_pagebreak}
:::

[]{#index_split_229.html}

![](images/00305.jpg){#filepos984388 .calibre_169}

::: {#index_split_229.html#calibre_pb_229 .mbp_pagebreak}
:::

[]{#index_split_230.html}

![](images/00167.jpg){#filepos984533 .calibre_277}

::: {#index_split_230.html#calibre_pb_230 .mbp_pagebreak}
:::

[]{#index_split_231.html}

![](images/00032.jpg){#filepos984679 .calibre_278}

::: {#index_split_231.html#calibre_pb_231 .mbp_pagebreak}
:::

[]{#index_split_232.html}

![](images/00259.jpg){#filepos984825 .calibre_279}

::: {#index_split_232.html#calibre_pb_232 .mbp_pagebreak}
:::

[]{#index_split_233.html}

![](images/00016.jpg){#filepos984971 .calibre_280}

::: {#index_split_233.html#calibre_pb_233 .mbp_pagebreak}
:::

[]{#index_split_234.html}

![](images/00364.jpg){#filepos985117 .calibre_281}

::: {#index_split_234.html#calibre_pb_234 .mbp_pagebreak}
:::

[]{#index_split_235.html}

![](images/00223.jpg){#filepos985248 .calibre_230}

::: {#index_split_235.html#calibre_pb_235 .mbp_pagebreak}
:::

[]{#index_split_236.html}

![](images/00087.jpg){#filepos985393 .calibre_282}

::: {#index_split_236.html#calibre_pb_236 .mbp_pagebreak}
:::

[]{#index_split_237.html}

![](images/00315.jpg){#filepos985539 .calibre_283}

::: {#index_split_237.html#calibre_pb_237 .mbp_pagebreak}
:::

[]{#index_split_238.html}

![](images/00181.jpg){#filepos985685 .calibre_284}

::: {#index_split_238.html#calibre_pb_238 .mbp_pagebreak}
:::

[]{#index_split_239.html}

![](images/00044.jpg){#filepos985831 .calibre_285}

::: {#index_split_239.html#calibre_pb_239 .mbp_pagebreak}
:::

[]{#index_split_240.html}

![](images/00274.jpg){#filepos985977 .calibre_286}

::: {#index_split_240.html#calibre_pb_240 .mbp_pagebreak}
:::

[]{#index_split_241.html}

![](images/00141.jpg){#filepos986123 .calibre_287}

::: {#index_split_241.html#calibre_pb_241 .mbp_pagebreak}
:::

[]{#index_split_242.html}

![](images/00005.jpg){#filepos986269 .calibre_288}

::: {#index_split_242.html#calibre_pb_242 .mbp_pagebreak}
:::

[]{#index_split_243.html}

![](images/00233.jpg){#filepos986415 .calibre_289}

::: {#index_split_243.html#calibre_pb_243 .mbp_pagebreak}
:::

[]{#index_split_244.html}

![](images/00098.jpg){#filepos986561 .calibre_290}

::: {#index_split_244.html#calibre_pb_244 .mbp_pagebreak}
:::

[]{#index_split_245.html}

![](images/00323.jpg){#filepos986707 .calibre_291}

::: {#index_split_245.html#calibre_pb_245 .mbp_pagebreak}
:::

[]{#index_split_246.html}

![](images/00193.jpg){#filepos986853 .calibre_292}

::: {#index_split_246.html#calibre_pb_246 .mbp_pagebreak}
:::

[]{#index_split_247.html}

![](images/00053.jpg){#filepos986999 .calibre_289}

::: {#index_split_247.html#calibre_pb_247 .mbp_pagebreak}
:::

[]{#index_split_248.html}

![](images/00283.jpg){#filepos987145 .calibre_293}

::: {#index_split_248.html#calibre_pb_248 .mbp_pagebreak}
:::

[]{#index_split_249.html}

![](images/00150.jpg){#filepos987290 .calibre_294}

::: {#index_split_249.html#calibre_pb_249 .mbp_pagebreak}
:::

[]{#index_split_250.html}

![](images/00017.jpg){#filepos987436 .calibre_295}

::: {#index_split_250.html#calibre_pb_250 .mbp_pagebreak}
:::

[]{#index_split_251.html}

![](images/00243.jpg){.calibre_296}

::: {#index_split_251.html#calibre_pb_251 .mbp_pagebreak}
:::

[]{#index_split_252.html}

![](images/00110.jpg){#filepos987728 .calibre_297}

::: {#index_split_252.html#calibre_pb_252 .mbp_pagebreak}
:::

[]{#index_split_253.html}

![](images/00335.jpg){#filepos987874 .calibre_298}

::: {#index_split_253.html#calibre_pb_253 .mbp_pagebreak}
:::

[]{#index_split_254.html}

![](images/00202.jpg){.calibre_299}

::: {#index_split_254.html#calibre_pb_254 .mbp_pagebreak}
:::

[]{#index_split_255.html}

![](images/00064.jpg){#filepos988166 .calibre_300}

::: {#index_split_255.html#calibre_pb_255 .mbp_pagebreak}
:::

[]{#index_split_256.html}

![](images/00293.jpg){#filepos988312 .calibre_301}

::: {#index_split_256.html#calibre_pb_256 .mbp_pagebreak}
:::

[]{#index_split_257.html}

![](images/00045.jpg){#filepos988458 .calibre_302}

::: {#index_split_257.html#calibre_pb_257 .mbp_pagebreak}
:::

[]{#index_split_258.html}

![](images/00365.jpg){.calibre_303}

::: {#index_split_258.html#calibre_pb_258 .mbp_pagebreak}
:::

[]{#index_split_259.html}

![](images/00118.jpg){#filepos988750 .calibre_304}

::: {#index_split_259.html#calibre_pb_259 .mbp_pagebreak}
:::

[]{#index_split_260.html}

![](images/00088.jpg){#filepos988896 .calibre_305}

::: {#index_split_260.html#calibre_pb_260 .mbp_pagebreak}
:::

[]{#index_split_261.html}

![](images/00210.jpg){.calibre_306}

::: {#index_split_261.html#calibre_pb_261 .mbp_pagebreak}
:::

[]{#index_split_262.html}

![](images/00253.jpg){#filepos989188 .calibre_307}

::: {#index_split_262.html#calibre_pb_262 .mbp_pagebreak}
:::

[]{#index_split_263.html}

![](images/00303.jpg){#filepos989334 .calibre_308}

::: {#index_split_263.html#calibre_pb_263 .mbp_pagebreak}
:::

[]{#index_split_264.html}

![](images/00275.jpg){#filepos989480 .calibre_309}

::: {#index_split_264.html#calibre_pb_264 .mbp_pagebreak}
:::

[]{#index_split_265.html}

![](images/00029.jpg){#filepos989625 .calibre_310}

::: {#index_split_265.html#calibre_pb_265 .mbp_pagebreak}
:::

[]{#index_split_266.html}

![](images/00006.jpg){#filepos989771 .calibre_311}

::: {#index_split_266.html#calibre_pb_266 .mbp_pagebreak}
:::

[]{#index_split_267.html}

![](images/00119.jpg){#filepos989918 .calibre_312}

::: {#index_split_267.html#calibre_pb_267 .mbp_pagebreak}
:::

[]{#index_split_268.html}

![](images/00099.jpg){#filepos990064 .calibre_313}

::: {#index_split_268.html#calibre_pb_268 .mbp_pagebreak}
:::

[]{#index_split_269.html}

![](images/00211.jpg){#filepos990210 .calibre_314}

::: {#index_split_269.html#calibre_pb_269 .mbp_pagebreak}
:::

[]{#index_split_270.html}

![](images/00254.jpg){#filepos990355 .calibre_315}

::: {#index_split_270.html#calibre_pb_270 .mbp_pagebreak}
:::

[]{#index_split_271.html}

![](images/00054.jpg){#filepos990501 .calibre_316}

::: {#index_split_271.html#calibre_pb_271 .mbp_pagebreak}
:::

[]{#index_split_272.html}

![](images/00284.jpg){#filepos990647 .calibre_317}

::: {#index_split_272.html#calibre_pb_272 .mbp_pagebreak}
:::

[]{#index_split_273.html}

![](images/00152.jpg){#filepos990793 .calibre_236}

::: {#index_split_273.html#calibre_pb_273 .mbp_pagebreak}
:::

[]{#index_split_274.html}

![](images/00018.jpg){#filepos990939 .calibre_318}

::: {#index_split_274.html#calibre_pb_274 .mbp_pagebreak}
:::

[]{#index_split_275.html}

![](images/00120.jpg){#filepos991085 .calibre_319}

::: {#index_split_275.html#calibre_pb_275 .mbp_pagebreak}
:::

[]{#index_split_276.html}

![](images/00111.jpg){.calibre_320}

::: {#index_split_276.html#calibre_pb_276 .mbp_pagebreak}
:::

[]{#index_split_277.html}

![](images/00336.jpg){#filepos991362 .calibre_321}

::: {#index_split_277.html#calibre_pb_277 .mbp_pagebreak}
:::

[]{#index_split_278.html}

![](images/00255.jpg){.calibre_322}

::: {#index_split_278.html#calibre_pb_278 .mbp_pagebreak}
:::

[]{#index_split_279.html}

![](images/00065.jpg){.calibre_323}

::: {#index_split_279.html#calibre_pb_279 .mbp_pagebreak}
:::

[]{#index_split_280.html}

![](images/00294.jpg){#filepos991800 .calibre_324}

::: {#index_split_280.html#calibre_pb_280 .mbp_pagebreak}
:::

[]{#index_split_281.html}

![](images/00165.jpg){#filepos991946 .calibre_325}

::: {#index_split_281.html#calibre_pb_281 .mbp_pagebreak}
:::

[]{#index_split_282.html}

![](images/00030.jpg){#filepos992092 .calibre_326}

::: {#index_split_282.html#calibre_pb_282 .mbp_pagebreak}
:::

[]{#index_split_283.html}

![](images/00257.jpg){#filepos992238 .calibre_327}

::: {#index_split_283.html#calibre_pb_283 .mbp_pagebreak}
:::

[]{#index_split_284.html}

![](images/00122.jpg){#filepos992384 .calibre_328}

::: {#index_split_284.html#calibre_pb_284 .mbp_pagebreak}
:::

[]{#index_split_285.html}

![](images/00351.jpg){#filepos992529 .calibre_329}

::: {#index_split_285.html#calibre_pb_285 .mbp_pagebreak}
:::

[]{#index_split_286.html}

![](images/00256.jpg){#filepos992675 .calibre_330}

::: {#index_split_286.html#calibre_pb_286 .mbp_pagebreak}
:::

[]{#index_split_287.html}

![](images/00079.jpg){#filepos992821 .calibre_331}

::: {#index_split_287.html#calibre_pb_287 .mbp_pagebreak}
:::

[]{#index_split_288.html}

![](images/00307.jpg){.calibre_332}

::: {#index_split_288.html#calibre_pb_288 .mbp_pagebreak}
:::

[]{#index_split_289.html}

![](images/00179.jpg){.calibre_333}

::: {#index_split_289.html#calibre_pb_289 .mbp_pagebreak}
:::

[]{#index_split_290.html}

![](images/00042.jpg){#filepos993259 .calibre_334}

::: {#index_split_290.html#calibre_pb_290 .mbp_pagebreak}
:::

[]{#index_split_291.html}

![](images/00272.jpg){.calibre_335}

::: {#index_split_291.html#calibre_pb_291 .mbp_pagebreak}
:::

[]{#index_split_292.html}

![](images/00132.jpg){#filepos993551 .calibre_336}

::: {#index_split_292.html#calibre_pb_292 .mbp_pagebreak}
:::

[]{#index_split_293.html}

![](images/00368.jpg){#filepos993697 .calibre_337}

::: {#index_split_293.html#calibre_pb_293 .mbp_pagebreak}
:::

[]{#index_split_294.html}

![](images/00224.jpg){#filepos993843 .calibre_338}

::: {#index_split_294.html#calibre_pb_294 .mbp_pagebreak}
:::

[]{#index_split_295.html}

![](images/00089.jpg){#filepos993988 .calibre_339}

::: {#index_split_295.html#calibre_pb_295 .mbp_pagebreak}
:::

[]{#index_split_296.html}

![](images/00316.jpg){.calibre_340}

::: {#index_split_296.html#calibre_pb_296 .mbp_pagebreak}
:::

[]{#index_split_297.html}

![](images/00191.jpg){#filepos994280 .calibre_341}

::: {#index_split_297.html#calibre_pb_297 .mbp_pagebreak}
:::

[]{#index_split_298.html}

![](images/00052.jpg){#filepos994426 .calibre_221}

::: {#index_split_298.html#calibre_pb_298 .mbp_pagebreak}
:::

[]{#index_split_299.html}

![](images/00282.jpg){#filepos994571 .calibre_342}

::: {#index_split_299.html#calibre_pb_299 .mbp_pagebreak}
:::

[]{#index_split_300.html}

![](images/00142.jpg){#filepos994717 .calibre_343}

::: {#index_split_300.html#calibre_pb_300 .mbp_pagebreak}
:::

[]{#index_split_301.html}

![](images/00007.jpg){.calibre_344}

::: {#index_split_301.html#calibre_pb_301 .mbp_pagebreak}
:::

[]{#index_split_302.html}

![](images/00234.jpg){#filepos995009 .calibre_345}

::: {#index_split_302.html#calibre_pb_302 .mbp_pagebreak}
:::

[]{#index_split_303.html}

![](images/00100.jpg){#filepos995155 .calibre_346}

::: {#index_split_303.html#calibre_pb_303 .mbp_pagebreak}
:::

[]{#index_split_304.html}

![](images/00324.jpg){#filepos995301 .calibre_179}

::: {#index_split_304.html#calibre_pb_304 .mbp_pagebreak}
:::

[]{#index_split_305.html}

![](images/00201.jpg){.calibre_347}

::: {#index_split_305.html#calibre_pb_305 .mbp_pagebreak}
:::

[]{#index_split_306.html}

![](images/00062.jpg){#filepos995593 .calibre_348}

::: {#index_split_306.html#calibre_pb_306 .mbp_pagebreak}
:::

[]{#index_split_307.html}

![](images/00291.jpg){.calibre_349}

::: {#index_split_307.html#calibre_pb_307 .mbp_pagebreak}
:::

[]{#index_split_308.html}

![](images/00153.jpg){#filepos995885 .calibre_350}

::: {#index_split_308.html#calibre_pb_308 .mbp_pagebreak}
:::

[]{#index_split_309.html}

![](images/00019.jpg){#filepos996031 .calibre_351}

::: {#index_split_309.html#calibre_pb_309 .mbp_pagebreak}
:::

[]{#index_split_310.html}

![](images/00245.jpg){.calibre_352}

::: {#index_split_310.html#calibre_pb_310 .mbp_pagebreak}
:::

[]{#index_split_311.html}

![](images/00112.jpg){#filepos996323 .calibre_353}

::: {#index_split_311.html#calibre_pb_311 .mbp_pagebreak}
:::

[]{#index_split_312.html}

![](images/00339.jpg){#filepos996469 .calibre_354}

::: {#index_split_312.html#calibre_pb_312 .mbp_pagebreak}
:::

[]{#index_split_313.html}

![](images/00212.jpg){#filepos996615 .calibre_355}

::: {#index_split_313.html#calibre_pb_313 .mbp_pagebreak}
:::

[]{#index_split_314.html}

![](images/00076.jpg){#filepos996761 .calibre_356}

::: {#index_split_314.html#calibre_pb_314 .mbp_pagebreak}
:::

[]{#index_split_315.html}

![](images/00304.jpg){#filepos996907 .calibre_357}

::: {#index_split_315.html#calibre_pb_315 .mbp_pagebreak}
:::

[]{#index_split_316.html}

![](images/00166.jpg){.calibre_358}

::: {#index_split_316.html#calibre_pb_316 .mbp_pagebreak}
:::

[]{#index_split_317.html}

![](images/00031.jpg){.calibre_359}

::: {#index_split_317.html#calibre_pb_317 .mbp_pagebreak}
:::

[]{#index_split_318.html}

![](images/00258.jpg){.calibre_360}

::: {#index_split_318.html#calibre_pb_318 .mbp_pagebreak}
:::

[]{#index_split_319.html}

![](images/00123.jpg){#filepos997491 .calibre_340}

::: {#index_split_319.html#calibre_pb_319 .mbp_pagebreak}
:::

[]{#index_split_320.html}

![](images/00354.jpg){#filepos997637 .calibre_361}

::: {#index_split_320.html#calibre_pb_320 .mbp_pagebreak}
:::

[]{#index_split_321.html}

![](images/00121.jpg){#filepos997783 .calibre_176}

::: {#index_split_321.html#calibre_pb_321 .mbp_pagebreak}
:::

[]{#index_split_322.html}

![](images/00043.jpg){#filepos997929 .calibre_362}

::: {#index_split_322.html#calibre_pb_322 .mbp_pagebreak}
:::

[]{#index_split_323.html}

![](images/00213.jpg){#filepos998075 .calibre_363}

::: {#index_split_323.html#calibre_pb_323 .mbp_pagebreak}
:::

[]{#index_split_324.html}

![](images/00078.jpg){#filepos998221 .calibre_364}

::: {#index_split_324.html#calibre_pb_324 .mbp_pagebreak}
:::

[]{#index_split_325.html}

![](images/00306.jpg){#filepos998367 .calibre_365}

::: {#index_split_325.html#calibre_pb_325 .mbp_pagebreak}
:::

[]{#index_split_326.html}

![](images/00168.jpg){#filepos998513 .calibre_239}

::: {#index_split_326.html#calibre_pb_326 .mbp_pagebreak}
:::

[]{#index_split_327.html}

![](images/00033.jpg){#filepos998659 .calibre_366}

::: {#index_split_327.html#calibre_pb_327 .mbp_pagebreak}
:::

[]{#index_split_328.html}

![](images/00260.jpg){#filepos998805 .calibre_367}

::: {#index_split_328.html#calibre_pb_328 .mbp_pagebreak}
:::

[]{#index_split_329.html}

![](images/00097.jpg){.calibre_368}

::: {#index_split_329.html#calibre_pb_329 .mbp_pagebreak}
:::
