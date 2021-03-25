
Homework 1
1) How would you define Machine Learning?
	Makine öğrenmesi, matematiksel ve istatistiksel işlemler ile veriler üzerinden çıkarımlar yaparak tahminlerde bulunan sistemlerin bilgisayar ile modellenmesidir.

2) What are the differences between Supervised and Unsupervised Learning? Specify example 3 algorithms for each of these.
	Supervised, gözetimli öğrenme; girdi verilerinden ve ilgili label'lardan model eğitme.
	Unsupervised, gözetimsiz öğrenme; işaretlenmemiş veri üzerinden bilinmeyen bir yapıyı öğrenmek için bir algoritma kullanan makine öğrenmesi tekniği.

3) What are the test and validation set, and why would you want to use them?
	Validation set: Doğrulamada kullanılan eğitim setinden ayrı olan veri setinin bir alt kümesi
	Test set: Model, doğrulama kümesi tarafından ilk incelemeden geçtikten sonra modeli test etmek için kullanılan veri kümesinin alt kümesi.
		
4) What are the main preprocessing steps? Explain them in detail. Why we need to prepare our data?
	Bir modeli eğitmek için kullanmadan önce verileri işlemek.
	1.Veri seçme: Verilerin hepsini değil bizim için gerekli veriler seçilmeli
	2.Veri ön işleme: Biçimlendirme; veriler csv gibi bir veri formatına çevrilir.
		          Temizleme; eksik veriler istatiksel yöntemlerle düzenlenebilir.
			  Örnekleme; çok fazla veri varsa, bu veri setinden örnek olabilecek daha küçük veri seti alınır.
	3.Veri dönüştürme:Ölçekleme, Ayrıştırma, Toplama
	

5) How you can explore countionus and discrete variables?
	Discrete(ayrık); Tam sayı değerler
	Countionus(sürekli): Bir aralıktaki herhangibir değer alabilir

6) Analyse the plot given below. (What is the plot and variable type, check the distribution and make comment about how you can preproccess it.)
matplotlib, countionus
