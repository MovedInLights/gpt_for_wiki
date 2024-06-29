# COMPARE_PROMPT = (
#     "As an expert in trademark comparison, you're tasked with assessing the similarity between two trademarks. "
#     "Based on the names provided, estimate the similarity percentage. "
#     "Your response should include the names of both trademarks followed by the estimated similarity percentage, formatted as follows: "
#     "'Trademark 1 - Trademark 2 - Similarity Percentage percent'. "
#     "Ensure your reply is concise and presented in Russian. Use the word 'процент' to denote percentage."
# )


COMPARE_REQUEST = (
    "Please compare the following trademarks: 1. My Trademark: '{clients_tm_app_name}' 2. Registered Trademark: '{registered_tm}'"
)
# fmt: off
RUPTO_TOOLKIT_TEXT = """1. Общие положения
Настоящие Методические рекомендации по проверке заявленных обозначений на тождество и сходство (далее - Рекомендации) направлены на обеспечение реализации положений части четвертой Гражданского кодекса Российской Федерации (далее - Кодекс), касающихся права на товарный знак и права на знак обслуживания. В Рекомендациях рассматриваются вопросы, связанные с определением тождества или сходства до степени смешения обозначений, заявленных на государственную регистрацию в качестве товарных знаков (знаков обслуживания), с товарными знаками и знаками обслуживания (далее - товарные знаки) других лиц, заявленными на государственную регистрацию или охраняемыми в Российской Федерации, в том числе в соответствии с международным договором Российской Федерации, а также признанными в установленном Кодексом порядке общеизвестными в Российской Федерации товарными знаками.
Рекомендации разработаны для экспертов и специалистов Роспатента и подведомственных ему организаций с целью их применения при экспертизе обозначения, заявленного на государственную регистрацию в качестве товарного знака, при рассмотрении возражения на решение о государственной регистрации товарного знака или об отказе в государственной регистрации товарного знака, а также при рассмотрении возражения против предоставления правовой охраны товарному знаку.
Рекомендации могут быть использованы также при решении вопросов о тождестве и сходстве товарных знаков, возникающих в ходе рассмотрения судебными, антимонопольными, правоохранительными органами дел, связанных с нарушением исключительного права на товарный знак.
Предлагаемые в Рекомендациях методические подходы, включающие признаки тождества и сходства до степени смешения товарных знаков, определены исходя из положений раздела VII части четвертой Кодекса.
При определении методических подходов были также учтены применявшиеся в предыдущие годы в системе Роспатента разработки, включая научно-исследовательские работы, по этой проблеме и опыт их практического применения.
2. Правовые основания проверки заявленных обозначений на тождество и сходство до степени смешения.
В соответствии с пунктом 6 статьи 1483 Кодекса не могут быть зарегистрированы в качестве товарных знаков обозначения, тождественные или сходные до степени смешения с:
1) товарными знаками других лиц, заявленными на регистрацию в отношении однородных товаров и имеющими более ранний приоритет, если заявка на государственную регистрацию товарного знака не отозвана или не признана отозванной;
2) товарными знаками других лиц, охраняемыми в Российской Федерации, в том числе в соответствии с международным договором Российской Федерации, в отношении однородных товаров и имеющими более ранний приоритет;
3) товарными знаками других лиц, признанными в установленном Кодексом порядке общеизвестными в Российской Федерации товарными знаками, в отношении однородных товаров.
Согласно пункту 1 статьи 1499 Кодекса одной из задач экспертизы обозначения, заявленного в качестве товарного знака (далее - экспертиза заявленного обозначения), является проверка соответствия заявленного обозначения перечисленным выше требованиям.
При проверке на тождество и сходство осуществляются следующие действия: - проводится поиск тождественных и сходных обозначений;
2 - определяется степень сходства заявленного и выявленных при проведении поиска
обозначений;
- определяется однородность товаров, в отношении которых заявлено обозначение, товарам,
для которых ранее зарегистрированы (заявлены) выявленные тождественные или сходные товарные знаки (обозначения).
В Рекомендациях изложены методические подходы, касающиеся только первых двух из перечисленных выше действий.
3. Понятие тождества и сходства до степени смешения
Административный регламент содержит определения понятий тождественного обозначения и обозначения, сходного до степени смешения, при экспертизе заявленных обозначений.
Обозначение считается тождественным с другим обозначением, если оно совпадает с ним во всех элементах.
Следовательно, сравниваемые обозначения признаются тождественными, если они полностью совпадают, т.е. являются одинаковыми.
Обозначение считается сходным до степени смешения с другим обозначением, если оно ассоциируется с ним в целом, несмотря на их отдельные отличия.
Оценка сходства обозначений производится на основе общего впечатления, формируемого, в том числе с учетом неохраняемых элементов. При этом формирование общего впечатления может происходить под воздействием любых особенностей обозначений, в том числе доминирующих словесных или графических элементов, их композиционного и цвето-графического решения и др. Исходя из разновидности обозначения (словесное, изобразительное, звуковое и т.д.) и/или способа его использования, общее впечатление может быть зрительным и/или слуховым.
Сходство обозначений связано с однородностью товаров (услуг), в отношении которых обозначения заявлены (зарегистрированы). При идентичности товаров (услуг), а также при их однородности, близкой к идентичности - больше вероятность смешения обозначений, используемых для индивидуализации товаров (услуг).
Вопросы определения сходства различных видов обозначений рассматриваются ниже.
4. Определение сходства словесных обозначений
4.1. Словесные обозначения сравниваются:
- со словесными обозначениями;
- с комбинированными обозначениями, в композиции которых входят словесные элементы. 4.2. Сходство словесных обозначений может быть звуковым (фонетическим), графическим
(визуальным) и смысловым (семантическим).
Перечисленные ниже признаки сходства словесных обозначений могут учитываться как
каждый в отдельности, так и в различных сочетаниях.
4.2.1. Звуковое (фонетическое) сходство.
4.2.1.1. Звуковое сходство определяется на основании следующих признаков:
- наличие близких и совпадающих звуков в сравниваемых обозначениях;
- близость звуков, составляющих обозначения;
- расположение близких звуков и звукосочетаний по отношению друг к другу;
- наличие совпадающих слогов и их расположение;
- число слогов в обозначениях;
- место совпадающих звукосочетаний в составе обозначений;
- близость состава гласных;
- близость состава согласных;
- характер совпадающих частей обозначений;
- вхождение одного обозначения в другое; - ударение.
4.2.1.2. наиболее распространенные случаи звукового сходства:
1) тождество звучания обозначений
DIXIE - DIXI, DIXY, ДИКСИ
2) тождество звучания начальных частей обозначений и сходство звучания конечных частей GEMO - ГЕМА
СТИЛОСЕРТ - СТИЛОЦЕРД

3 3) сходство звучания начальных частей обозначений и тождество звучания конечных частей
ZIBO - ZEBO
KENZO - ENZO
4) тождество звучания начальных и конечных частей обозначений и сходство звучания
средних частей
ДУАЛИН - ДУАЙЛЛИН
ЛОНГЕВИТ - ЛОНГОВИТ
5) тождество звучания средних частей обозначения и сходство звучания начальных и конечных частей
ARIBOLT - ORIBOLD
6) фонетическое вхождение одного обозначения в другое
ДЕТОКС - ФИТОДЕТОКС
FREESTYLE - KO’S FREESTYLE
БИОРИТМ - BIORYTHMA
4.2.1.3. В состав словесных обозначений могут входить как сильные, так и слабые элементы. Сильные элементы оригинальны, не носят описательного характера. К слабым элементам, в
частности, относятся:
- систематически повторяющиеся в товарных знаках буквосочетания (форманты) типа -мат, -
трон, -ол, -дент, карб- и т.д.;
- неохраняемые обозначения (ЭКО, ИНФО, ПЛЮС, AUTO, SOFT, FORTE).
Например, в обозначении AUTOSCRIPT слабым элементом является AUTO, а сильным
элементом - SCRIPT. В обозначении MEGASPELL слабый элемент - MEGA, а сильный элемент - SPELL.
При экспертизе словесных обозначений необходимо учитывать сходство именно сильных элементов.
Если словесное обозначение, состоящее из упомянутых выше элементов, имеет смысловое значение (например, ПЛАЗМОН, СЕЛЕНИТ), то это обозначение при экспертизе следует оценивать в целом, без деления на части.
4.2.1.4. Иногда сильный элемент кладется в основу серии знаков, образуемой путем присоединения к нему различных формантов (INDASFORM, INDASPAD, INDASLIP, INDASEC) или неохраняемых обозначений (VIZSPA, VIZPOWER, VIZCARE, VIZCLEAN).
Новое заявленное обозначение с тем же сильным элементом (например, INDASTEN и VIZSOFT соответственно) может рассматриваться как сходное до степени смешения с соответствующей серией знаков.
4.2.2. Графическое (визуальное) сходство.
4.2.2.1. Графическое сходство определяется на основании следующих признаков:
- общее зрительное впечатление;
- вид шрифта;
- графическое написание с учетом характера букв (например, печатные или письменные,
заглавные или строчные);
- расположение букв по отношению друг к другу;
- алфавит, буквами которого написано слово;
- цвет или цветовое сочетание.
4.2.2.2. Графическое сходство может усилить сходство обозначений или, наоборот, ослабить
его. Например, использование одинакового алфавита усиливает сходство обозначений SCHUMANN и SCHAUMAN, LANCOME и LONCAME.
Написание обозначения АЛЬФА в оригинальной графической манере (рис. 1) ослабляет его сходство с обозначением ALFA.
4.2.2.3. Оригинальное графическое исполнение словесного обозначения может привести к восприятию его как изобразительного обозначения, а не словесного.
Например, на рис. 2 приводится изображение словесного обозначения ГАММА, выполненного в оригинальной графической манере. На рис. 3 приводится обозначение, в котором слово СОЮЗ выполнено в виде стилизованного изображения головы кошки.
Экспертиза подобных обозначений должна проводиться в соответствии с признаками, предусмотренными для сравнения изобразительных обозначений.

4
4.2.3. Смысловое (семантическое) сходство.
4.2.3.1. Смысловое сходство определяется на основании следующих признаков:
- подобие заложенных в обозначениях понятий, идей (МУЗЫКА СНА - МЕЛОДИЯ СНА), в
частности, совпадение значения обозначений в разных языках (например, АРОМАТНАЯ МЕЛОДИЯ - AROMATIC MELODY);
- совпадение одного из элементов обозначений, на который падает логическое ударение и который имеет самостоятельное значение (CARLA FRACCI GISELLE - ЖИЗЕЛЬ), за исключением ситуации, в которой смысловое значение названного элемента меняется благодаря сочетанию с другими словесными элементами (например, ДУША - СЛАВЯНСКАЯ ДУША);
- противоположность заложенных в обозначениях понятий, идей (МОЙ МАЛЫШ - ВАШ МАЛЫШ).
4.2.3.2. Наличие у обозначения смыслового значения (или, наоборот, отсутствие такового) может способствовать признанию сравниваемых обозначений несходными. Например, КРОН (мифический герой, титан; разновидность краски) - КРОНА (часть растения; денежная единица; монета).
4.2.4. Экспертиза словесных обозначений, состоящих из двух и более слов.
4.2.4.1. Если словесное обозначение состоит из двух и более слов, экспертиза проводится как отдельно по каждому слову, так и по всему обозначению в целом (например, обозначение STELLA ALPINA). Исключение составляют устойчивые словосочетания типа ШАПКА МОНОМАХА, ELIXIR D’AMOUR, при экспертизе которых анализируется сходство всего обозначения, а не его отдельных элементов.
4.2.4.2. Если словесное обозначение состоит из охраноспособных и неохраноспособных элементов (например, ПИЦЦА СЧАСТЬЯ, ФОРМУЛА ВИН), то при экспертизе учитывается тождество и сходство именно охраноспособных элементов (FASHION COLOURS - COLORS).
В тоже время необходимо учитывать, что совпадение или сходство неохраноспособных элементов может усиливать сходство обозначений (например, KALPOL INTERNATIONAL - KOLPAL INTERNATIONAL; BEГA КОСМЕТИКА - VEGAS COSMETICS).
5. Определение сходства изобразительных и объемных обозначений
5.1. Изобразительные и объемные обозначения сравниваются:
- с изобразительными обозначениями;
- с объемными обозначениями;
- с комбинированными обозначениями, в композиции которых входят изобразительные или
объемные элементы.
5.2. Сходство изобразительных и объемных обозначений определяется на основании
следующих признаков:
- внешняя форма;
- наличие или отсутствие симметрии;
- смысловое значение;
- вид и характер изображений (натуралистическое, стилизованное, карикатурное и т.д.);
- сочетание цветов и тонов.
Перечисленные признаки могут учитываться как каждый в отдельности, так и в различных
сочетаниях.
5.2.1. При определении сходства изобразительных и объемных обозначений наиболее
важным является первое впечатление, получаемое при их сравнении. Именно оно наиболее близко к восприятию товарных знаков потребителями, которые, уже приобретали такой товар. Поэтому, если при первом впечатлении сравниваемые обозначения представляются сходными, а последующий анализ выявит отличие обозначений за счет расхождения отдельных элементов, то при оценке сходства обозначений целесообразно руководствоваться первым впечатлением. Сказанное проиллюстрировано примерами в отношении изобразительных обозначений, которые могут быть отнесены к сходным до степени смешения (рис. 4, 5).
5.2.2. Поскольку зрительное восприятие отдельного зрительного объекта начинается с его внешнего контура, то именно он запоминается в первую очередь. Поэтому оценку сходства обозначений целесообразно основывать на сходстве их внешней формы, не принимая во внимание незначительное расхождение во внутренних деталях обозначений.

5 5.2.3. На сходство изобразительных и объемных обозначений влияет их смысловое
значение. Одинаковое смысловое значение обозначений усиливает их сходство.
5.2.4. Сходство сочетаний цветов и тонов изобразительных и объемных обозначений может рассматриваться в качестве признака сходства. В некоторых случаях этот признак может быть основным, например, когда цвет (сочетание цветов) является фоном, на котором расположены
другие элементы обозначения, или когда совокупность цветов составляет основу его композиции. 5.3. При оценке сходства изобразительных и объемных обозначений, состоящих из двух и
более элементов, решающим является тождество или сходство следующих элементов:
- пространственно доминирующих элементов;
- элементов, на которых в большей степени фиксируется внимание потребителей (к таким
элементам относятся, в первую очередь, изображения людей, животных, растений и других объектов, окружающих человека, а также изображения букв, цифр);
- элементов, которые лучше запоминаются потребителями (например, симметричные элементы; элементы, представляющие собой изображения конкретных объектов, а не абстрактных).
6. Определение сходства комбинированных обозначений
6.1. Комбинированные обозначения сравниваются:
- с комбинированными обозначениями;
- с теми видами обозначений, которые входят в состав проверяемого комбинированного
обозначения как элементы.
6.2. При определении сходства комбинированных обозначений используются признаки и
положения, приведенные в разделах 4 и 5 настоящих Рекомендаций.
6.3. При оценке сходства комбинированных обозначений определяется сходство как всего
обозначения в целом, так и его составляющих элементов с учетом значимости положения, занимаемого тождественным или сходным элементом в заявленном обозначении.
При сравнении комбинированных обозначений, содержащих неохраняемые элементы, оценка их сходства также должна производиться на основе общего зрительного впечатления, формируемого, в том числе благодаря неохраняемым элементам, как, например, в приведенных на рис. 6 комбинированных обозначениях, содержащих словесные элементы «ТРИУМФАЛЬНАЯ ВОДКА» и «ТРИУМФАЛЬНАЯ ЧАША».
6.3.1. При исследовании положения словесного и изобразительного элемента в комбинированном обозначении учитывается фактор визуального доминирования одного из элементов. Такое доминирование может быть вызвано как более крупными размерами элемента, так и его более удобным для восприятия расположением в композиции (например, элемент может занимать центральное место, с которого начинается осмотр обозначения). Изображение одного из элементов в цвете может способствовать доминированию этого элемента в композиции.
Например, комбинированные обозначения, предназначенные для использования в отношении товара «пиво», приведенные на рис. 7, одно из которых содержит слово «ОХОТА», а другое содержит словосочетание «КАЗНАЧЕЙСКАЯ ОХОТА», могут рассматриваться как сходные до степени смешения благодаря доминированию в обоих обозначениях словесного элемента «ОХОТА».
Значимость положения элемента в комбинированном обозначении зависит также от того, в какой степени элемент способствует осуществлению обозначением его основной функции - индивидуализации товаров юридических лиц или индивидуальных предпринимателей.
6.3.2. При восприятии потребителем комбинированного обозначения, состоящего из изобразительного и словесного элементов, его внимание, как правило, акцентируется на словесном элементе. Словесный элемент к тому же легче запоминается, чем изобразительный.
Если при сравнении комбинированных обозначений будет установлено, что их словесные элементы тождественны или сходны до степени смешения, то такие комбинированные обозначения могут быть отнесены к сходным до степени смешения. Например, обозначения, приведенные на рис. 8, могут рассматриваться как сходные до степени смешения, поскольку они содержат словесные элементы «ДЕЛЬТА», являющиеся тождественными по звуковому и смысловому признакам.
Если при сравнении словесного элемента комбинированного обозначения будет установлена его тождественность или сходство до степени смешения со словесным товарным знаком, то комбинированное обозначение может быть признано сходным до степени смешения с этим товарным знаком. Например, комбинированное обозначение, содержащее словесный элемент

6 «ЮВенТа», (рис. 9) может рассматриваться как сходное до степени смешения со словесным
товарным знаком «ЮВЕНТА».
6.3.3. Изобразительный элемент комбинированного обозначения может играть существенную
роль в индивидуализации товара наряду со словесным элементом.
Степень важности изобразительного элемента в комбинированном обозначении зависит от
того, насколько этот элемент оригинален, каковы его размеры и пространственное положение относительно словесного элемента. Перечисленные факторы могут учитываться как каждый в отдельности, так и в совокупности.
Если при сравнении комбинированных обозначений будет установлено, что изобразительные элементы обозначений тождественны или сходны до степени смешения и важны для индивидуализации товаров, то такие комбинированные обозначения могут рассматриваться как сходные до степени смешения при различных словесных элементах (рис. 10).
Если при сравнении изобразительного элемента комбинированного обозначения с изобразительным товарным знаком будет установлена их тождественность или сходство до степени смешения, то заявленное комбинированное обозначение может быть отнесено к сходным до степени смешения с выявленным изобразительным знаком (рис. 11).
6.3.4. Следует учитывать, что имеются изобразительные элементы, часто использующиеся в товарных знаках разными лицами, утратившие в связи с этим различительную способность (например, изображение земного шара, пятиконечной звезды). Поэтому присутствие в комбинированных обозначениях подобных элементов не может служить основанием для признания данных обозначений сходными до степени смешения (рис. 12).
6.3.5. В том случае, если при экспертизе комбинированного обозначения будет установлено, что его элемент, не относящийся к общей композиции обозначения, тождественен товарному знаку другого лица, охраняемому в Российской Федерации в отношении однородных товаров, оценка охраноспособности заявленного комбинированного обозначения проводится по другому основанию для отказа в государственной регистрации товарного знака, а именно определяется способность ввести в заблуждение потребителя относительно изготовителя товара."""


COMPARE_PROMPT = f"""
    You are a trademark registration specialist. Your task is to determine if a given word can be registered as a trademark, considering that there is already an existing registered logo. To compare the word and the logo, use the officially provided guidelines below.
    "{RUPTO_TOOLKIT_TEXT}"
    YOU SHOULD STRICTLY FOLLOW THIS GUIDELINE!!!!!
    Provide detailed response with comparison of two trademarks and explanation, based on the guideline, why it could or couldn't registered. Reply in russian language.
    """


CONCLUSION_PROMPT = f"""
    You are a trademark registration specialist. Your task is to determine if a given word can be registered as a trademark, considering that there is already an existing registered list of trademarks. To compare the word and the list, use the officially provided guidelines below.
    "{RUPTO_TOOLKIT_TEXT}"
    YOU SHOULD STRICTLY FOLLOW THIS GUIDELINE!!!!!
    Provide your answer with a percentage probability calculation. The percentage should reflect how likely it is that the trademark will be registered, given the list of registered trademarks. You just have to answer with a number.

    """
