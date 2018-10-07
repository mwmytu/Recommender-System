A simple pytorch version Matrix Facotrization

Dataset: ml-100k


See benchmark results on some dataset on http://www.mymedialite.net/examples/datasets.html
  <p>
    Results on the <it>probe</it> dataset:
    <table border="1">
      <tr> <th>Method</th> <th><tt>--recommender-options</tt></th> <th>RMSE</th> <th>MAE</th></tr>
              <tr> <td>UserItemBaseline</td> <td><tt>reg_u=4.5 reg_i=1.137 num_iter=10</tt></td> <td>0.98261</td> <td>0.76832</td> </tr>
              <tr> <td>BiasedMatrixFactorization</td> <td><tt>num_factors=0  learn_rate=0.005 bias_reg=0.0001 reg=0.035 num_iter=80</tt></td> <td>0.9830</td> <td>0.7710</td> </tr>
              <tr> <td>BiasedMatrixFactorization</td> <td><tt>num_factors=20 learn_rate=0.005 bias_reg=0.0001 reg=0.035 num_iter=40</tt></td> <td>0.9197</td> <td>0.7157</td> </tr>
              <tr> <td>BiasedMatrixFactorization</td> <td><tt>num_factors=50 learn_rate=0.005 bias_reg=0.0001 reg=0.035 num_iter=90</tt></td> <td>0.9175</td> <td>0.7135</td> </tr>
              <tr> <td>BiasedMatrixFactorization</td> <td><tt>num_factors=80 learn_rate=0.005 reg=0.035 num_iter=26</tt></td> <td>0.9169</td> <td>0.7126</td> </tr>
          </table>
  </p>
  <p>
    Results on the <it>quiz</it> dataset:
    <table border="1">
      <tr> <th>Method</th> <th><tt>--recommender-options</tt></th> <th>RMSE</th> <th>MAE</th></tr>
              <tr> <td>GlobalAverage</td> <td><tt></tt></td> <td>1.13092</td> <td>0.95377</td> </tr>
              <tr> <td>UserAverage</td> <td><tt></tt></td> <td>1.06506</td> <td>0.84848</td> </tr>
              <tr> <td>ItemAverage</td> <td><tt></tt></td> <td>1.05326</td> <td>0.85045</td> </tr>
              <tr> <td>UserItemBaseline</td> <td><tt>reg_u=4.5 reg_i=1.137 num_iter=10</tt></td> <td>0.98013</td> <td>0.76673</td> </tr>
              <tr> <td>BiasedMatrixFactorization</td> <td><tt>num_factors=120 learn_rate=0.005 bias_reg=0.0001 reg_u=0.035 reg_i=0.035 num_iter=50 bold_driver=True</tt></td> <td>0.9086</td> <td>0.70775</td> </tr>
          </table>

  </p>

  <a href="http://kddcup.yahoo.com"><h3>KDD Cup 2011, Track 1</h3></a>
  <p>
   Results on the validation set:
    <table border="1">
      <tr> <th>Method</th> <th><tt>--recommender-options</tt></th> <th>RMSE</th> <th>MAE</th> </tr>
              <tr> <td>GlobalAverage</td> <td><tt></tt></td> <td>38.17409</td> <td>34.5378</td> </tr>
              <tr> <td>UserAverage</td> <td><tt></tt></td> <td>29.30487</td> <td>22.91169</td> </tr>
              <tr> <td>ItemAverage</td> <td><tt></tt></td> <td>34.27364</td> <td>29.41114</td> </tr>
              <tr> <td>UserItemBaseline</td> <td><tt>reg_u=4.5 reg_i=1.137 num_iter=10</tt></td> <td>27.415</td> <td>21.14358</td> </tr>
              <tr> <td>BiasedMatrixFactorization</td> <td><tt>num_factors=20 bias_reg=0.001 reg_u=1 reg_i=1 learn_rate=0.0005 num_iter=370 bold_driver=True</tt></td> <td>22.2001</td> <td>14.01087</td> </tr>
          </table>
  </p>
  
  <a href="http://webscope.sandbox.yahoo.com/catalog.php?datatype=r"><h3>Yahoo! Music (about 700 million ratings)</h3></a>
  <p>
   Results on the validation set:
    <table border="1">
      <tr> <th>Method</th> <th><tt>--recommender-options</tt></th> <th>RMSE</th> <th>MAE</th> </tr>
              <tr> <td>GlobalAverage</td> <td><tt></tt></td> <td>1.58333</td> <td>1.4266</td> </tr>
              <tr> <td>UserAverage</td> <td><tt></tt></td> <td>1.29421</td> <td>1.03074</td> </tr>
              <tr> <td>ItemAverage</td> <td><tt></tt></td> <td>1.49744</td> <td>1.31978</td> </tr>
              <tr> <td>UserItemBaseline</td> <td><tt>reg_u=4.5 reg_i=1.137 num_iter=10</tt></td> <td>1.23747</td> <td>0.97561</td> </tr>
              <tr> <td>BiasedMatrixFactorization</td> <td><tt>num_factors=10 bias_reg=0.00001 reg_u=0.01 reg_i=0.01 learn_rate=0.0005 num_iter=100 bold_driver=True</tt></td> <td>1.07446</td> <td>0.81445</td> </tr>
          </table>
  </p>

  <a href="http://www.grouplens.org/node/73"><h3>MovieLens 1M</h3></a>
  <p>
   Results for 5-fold cross-validation on the complete dataset:
    <table border="1">
      <tr> <th>Method</th> <th><tt>--recommender-options</tt></th> <th>RMSE</th> <th>MAE</th> </tr>
              <tr> <td>GlobalAverage</td> <td><tt></tt></td> <td>1.117</td> <td>0.934</td> </tr>
              <tr> <td>UserAverage</td> <td><tt></tt></td> <td>1.036</td> <td>0.827</td> </tr>
              <tr> <td>ItemAverage</td> <td><tt></tt></td> <td>0.983</td> <td>0.783</td> </tr>
              <tr> <td>SlopeOne</td> <td><tt></tt></td> <td>0.902</td> <td>0.712</td> </tr>
              <tr> <td>UserItemBaseline</td> <td><tt>reg_u=25 reg_i=10, num_iter=10</tt></td> <td>0.908</td> <td>0.719</td> </tr>
              <tr> <td>ItemKNNPearson</td> <td><tt>k=80 shrinkage=10 reg_u=25 reg_i=10</tt></td> <td>0.871</td> <td>0.683</td> </tr>
              <tr> <td>FactorWiseMatrixFactorization</td> <td><tt>num_factors=11 shrinkage=115</tt></td> <td>0.860</td> <td>0.673</td> </tr>
              <tr> <td>MatrixFactorization</td> <td><tt>num_factors=10 num_iter=75 reg=0.05 learn_rate=0.005</tt></td> <td>0.857</td> <td>0.675</td> </tr>
              <tr> <td>BiasedMatrixFactorization</td> <td><tt>num_factors=6  bias_reg=0.25 reg_u=0.4 reg_i=1.2 frequency_regularization=true learn_rate=0.03 num_iter=80 bold_driver=true</tt></td> <td>0.854</td> <td>0.674</td> </tr>
              <tr> <td>BiasedMatrixFactorization</td> <td><tt>num_factors=20 bias_reg=0.25 reg_u=0.4 reg_i=1.2 frequency_regularization=true learn_rate=0.03 num_iter=80 bold_driver=true</tt></td> <td>0.852</td> <td>0.672</td> </tr>
              <tr> <td>BiasedMatrixFactorization</td> <td><tt>num_factors=40 bias_reg=0.001 regularization=0.060 learn_rate=0.07 num_iter=110 bold_driver=true</tt></td> <td>0.855</td> <td>0.676</td> </tr>
              <tr> <td>BiasedMatrixFactorization</td> <td><tt>num_factors=60 bias_reg=0.001 regularization=0.060 learn_rate=0.07 num_iter=100 bold_driver=true</tt></td> <td>0.854</td> <td>0.676</td> </tr>
              <tr> <td>BiasedMatrixFactorization</td> <td><tt>num_factors=80 bias_reg=0.001 regularization=0.060 learn_rate=0.07 num_iter=100 bold_driver=true</tt></td> <td>0.854</td> <td>0.676</td> </tr>
              <tr> <td>BiasedMatrixFactorization</td> <td><tt>num_factors=120 bias_reg=0.001 regularization=0.055 learn_rate=0.07 num_iter=100 bold_driver=true</tt></td> <td>0.854</td> <td>0.676</td> </tr>
              <tr> <td>SVDPlusPlus</td> <td><tt>num_factors=10 num_iter=80 reg=0.05 learn_rate=0.005</tt></td> <td>0.852</td> <td>0.668</td> </tr>
              <tr> <td>SVDPlusPlus</td> <td><tt>num_factors=20 num_iter=80 reg=0.05 learn_rate=0.005</tt></td> <td>0.851</td> <td>0.668</td> </tr>
          </table>
  </p>

  <h3><a href="http://www.grouplens.org/node/73">MovieLens 100k</a></h3>
  <p>
    5-fold crossvalidation with <tt>--random-seed=1</tt>
    <table border="1">
      <tr> <th>Method</th> <th><tt>--recommender-options</tt></th> <th>RMSE</th>  <th>MAE</th> </tr>
            <tr> <td>BipolarSlopeOne</td> <td><tt></tt></td> <td>0.96754</td> <td>0.74462</td> </tr>
            <tr> <td>UserItemBaseline</td> <td><tt>reg_u=5 reg_i=2</tt></td> <td>0.94192</td> <td>0.74503</td> </tr>
            <tr> <td>SlopeOne</td> <td><tt></tt></td> <td>0.93978</td> <td>0.74038</td> </tr>
            <tr> <td>UserKNNCosine</td> <td><tt>k=40 reg_u=12 reg_i=1</tt></td> <td>0.937</td> <td>0.737</td> </tr>
            <tr> <td>UserKNNPearson</td> <td><tt>k=60 shrinkage=25 reg_u=12 reg_i=1</tt></td> <td>0.92971</td> <td>0.72805</td> </tr>
            <tr> <td>ItemKNNCosine</td> <td><tt>k=40 reg_u=12 reg_i=1</tt></td> <td>0.924</td> <td>0.727</td> </tr>
            <tr> <td>FactorWiseMatrixFactorization</td> <td><tt>num_factors=5 num_iter=5 shrinkage=150</tt></td> <td>0.9212</td> <td>0.7252</td> </tr>
            <tr> <td>BiasedMatrixFactorization</td> <td><tt>num_factors=5 bias_reg=0.1 reg_u=0.1 reg_i=0.1 learn_rate=0.07 num_iter=100 bold_driver=true</tt></td> <td>0.91678</td> <td>0.72289</td> </tr>
            <tr> <td>BiasedMatrixFactorization</td> <td><tt>num_factors=10 bias_reg=0.1 reg_u=0.1 reg_i=0.12 learn_rate=0.07 num_iter=100 bold_driver=true</tt></td> <td>0.91496</td> <td>0.72209</td> </tr>
            <tr> <td>SVDPlusPlus</td> <td><tt>num_factors=4 regularization=0.1 bias_reg=0.005 learn_rate=0.01 bias_learn_rate=0.007 num_iter=50</tt></td> <td>0.9138</td> <td>0.71836</td> </tr>
            <tr> <td>ItemKNNPearson</td> <td><tt>k=40 shrinkage=2500 reg_u=12 reg_i=1</tt></td> <td>0.91327</td> <td>0.7144</td> </tr>
            <tr> <td>BiasedMatrixFactorization</td> <td><tt>num_factors=40 bias_reg=0.1 reg_u=1.0 reg_i=1.2 learn_rate=0.07 num_iter=100 frequency_regularization=true bold_driver=true</tt></td> <td>0.90764</td> <td>0.71722</td> </tr>
            <tr> <td>BiasedMatrixFactorization</td> <td><tt>num_factors=80 bias_reg=0.003 reg_u=0.09 reg_i=0.1 learn_rate=0.07 num_iter=100 bold_driver=true</tt></td> <td>0.91153</td> <td>0.72013</td> </tr>
            <tr> <td>SVDPlusPlus</td> <td><tt>num_factors=10 regularization=0.1 bias_reg=0.005 learn_rate=0.01 bias_learn_rate=0.007 num_iter=50</tt></td> <td>0.91096</td> <td>0.7152</td> </tr>
            <tr> <td>BiasedMatrixFactorization</td> <td><tt>num_factors=320 bias_reg=0.007 reg_u=0.1 reg_i=0.1 learn_rate=0.07 num_iter=500 bold_driver=true</tt></td> <td>0.91073</td> <td>0.72053</td> </tr>
            <tr> <td>BiasedMatrixFactorization</td> <td><tt>num_factors=160 bias_reg=0.003 reg_u=0.08 reg_i=0.1 learn_rate=0.07 num_iter=100 bold_driver=true</tt></td> <td>0.91047</td> <td>0.71944</td> </tr>
            <tr> <td>SigmoidItemAsymmetricFactorModel</td> <td><tt>num_factors=5 regularization=0.005 bias_reg=0.1 learn_rate=0.006 bias_learn_rate=0.7 num_iter=65</tt></td> <td>0.91</td> <td>0.71701</td> </tr>
            <tr> <td>SVDPlusPlus</td> <td><tt>num_factors=4 regularization=1 bias_reg=0.05 learn_rate=0.01 bias_learn_rate=0.07 num_iter=50 frequency_regularization=true</tt></td> <td>0.90906</td> <td>0.71547</td> </tr>
            <tr> <td>SigmoidItemAsymmetricFactorModel</td> <td><tt>num_factors=10 regularization=0.005 bias_reg=0.1 learn_rate=0.006 bias_learn_rate=0.7 num_iter=90</tt></td> <td>0.9086</td> <td>0.71522</td> </tr>
            <tr> <td>SVDPlusPlus</td> <td><tt>num_factors=20 regularization=0.1 bias_reg=0.005 learn_rate=0.01 bias_learn_rate=0.007 num_iter=50</tt></td> <td>0.90829</td> <td>0.713</td> </tr>
            <tr> <td>SVDPlusPlus</td> <td><tt>num_factors=20 regularization=1 bias_reg=0.005 learn_rate=0.01 bias_learn_rate=0.07 num_iter=50 frequency_regularization=true</tt></td> <td>0.90783</td> <td>0.71413</td> </tr>
            <tr> <td>SVDPlusPlus</td> <td><tt>num_factors=50 regularization=1 bias_reg=0.005 learn_rate=0.01 bias_learn_rate=0.07 num_iter=50 frequency_regularization=true</tt></td> <td>0.90651</td> <td>0.71352</td> </tr>
            <tr> <td>SigmoidUserAsymmetricFactorModel</td> <td><tt>num_factors=5 regularization=0.003 bias_reg=0.01 learn_rate=0.006 bias_learn_rate=0.7 num_iter=70</tt></td> <td>0.89062</td> <td>0.69995</td> </tr>
          </table>
  </p>

  <h3><a href="">Epinions</a></h3>
  <p>
    5-fold crossvalidation with <tt>--random-seed=1</tt>
    <table border="1">
      <tr> <th>Method</th> <th><tt>--recommender-options</tt></th> <th>RMSE</th> </tr>
            <tr> <td>GlobalAverage</td> <td><tt></tt></td> <td>1.20684</td> </tr>
            <tr> <td>UserAverage</td> <td><tt></tt></td> <td>1.19884</td> </tr>
            <tr> <td>ItemAverage</td> <td><tt></tt></td> <td>1.09421</td> </tr>
            <tr> <td>UserItemBaseline</td> <td><tt></tt></td> <td>1.04722</td> </tr>
            <tr> <td>BiasedMatrixFactorization</td> <td><tt>num_iter=30 num_factors=5 learn_rate=0.01 reg=3.5</tt></td> <td>1.04265</td> </tr>
          </table>
  </p>

  <h3><a href="http://www.cs.sfu.ca/~sja25/personal/datasets/">Flixster</a></h3>
  <p>
    5-fold crossvalidation with <tt>--random-seed=1</tt>
    <table border="1">
      <tr> <th>Method</th> <th><tt>--recommender-options</tt></th> <th>RMSE</th>  <th>MAE</th> </tr>
            <tr> <td>GlobalAverage</td> <td><tt></tt></td> <td>1.092</td> <td>0.871</td> </tr>
            <tr> <td>UserAverage</td> <td><tt></tt></td> <td>1.032</td> <td>0.719</td> </tr>
            <tr> <td>ItemAverage</td> <td><tt></tt></td> <td>1.097</td> <td>0.852</td> </tr>
            <tr> <td>UserItemBaseline</td> <td><tt>reg_u=15 reg_i=10</tt></td> <td>0.904</td> <td>0.685</td> </tr>
            <tr> <td>BiasedMatrixFactorization</td> <td><tt>num_factors=5 bias_reg=0.0001 regularization=0.03 learn_rate=0.051 num_iter=50 bold_driver=True</tt></td> <td>0.851</td> <td>0.633</td> </tr>
            <tr> <td>BiasedMatrixFactorization</td> <td><tt>num_factors=10 bias_reg=0.0001 regularization=0.015 learn_rate=0.051 num_iter=50 bold_driver=True</tt></td> <td>0.845</td> <td>0.625</td> </tr>
          </table>
  </p>  

