#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-keras
Version  : 2.2.5.0
Release  : 19
URL      : https://cran.r-project.org/src/contrib/keras_2.2.5.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/keras_2.2.5.0.tar.gz
Summary  : R Interface to 'Keras'
Group    : Development/Tools
License  : MIT
Requires: R-R6
Requires: R-generics
Requires: R-magrittr
Requires: R-reticulate
Requires: R-tensorflow
Requires: R-tfruns
Requires: R-zeallot
BuildRequires : R-R6
BuildRequires : R-generics
BuildRequires : R-magrittr
BuildRequires : R-reticulate
BuildRequires : R-tensorflow
BuildRequires : R-tfruns
BuildRequires : R-zeallot
BuildRequires : buildreq-R
BuildRequires : util-linux

%description
networks 'API'. 'Keras' was developed with a focus on enabling fast experimentation,
  supports both convolution based networks and recurrent networks (as well as
  combinations of the two), and runs seamlessly on both 'CPU' and 'GPU' devices.

%prep
%setup -q -c -n keras

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1571850426

%install
export SOURCE_DATE_EPOCH=1571850426
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library keras
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library keras
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library keras
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc keras || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/keras/DESCRIPTION
/usr/lib64/R/library/keras/INDEX
/usr/lib64/R/library/keras/LICENSE
/usr/lib64/R/library/keras/Meta/Rd.rds
/usr/lib64/R/library/keras/Meta/features.rds
/usr/lib64/R/library/keras/Meta/hsearch.rds
/usr/lib64/R/library/keras/Meta/links.rds
/usr/lib64/R/library/keras/Meta/nsInfo.rds
/usr/lib64/R/library/keras/Meta/package.rds
/usr/lib64/R/library/keras/Meta/vignette.rds
/usr/lib64/R/library/keras/NAMESPACE
/usr/lib64/R/library/keras/NEWS.md
/usr/lib64/R/library/keras/R/keras
/usr/lib64/R/library/keras/R/keras.rdb
/usr/lib64/R/library/keras/R/keras.rdx
/usr/lib64/R/library/keras/doc/about_keras_layers.R
/usr/lib64/R/library/keras/doc/about_keras_layers.Rmd
/usr/lib64/R/library/keras/doc/about_keras_layers.html
/usr/lib64/R/library/keras/doc/about_keras_models.R
/usr/lib64/R/library/keras/doc/about_keras_models.Rmd
/usr/lib64/R/library/keras/doc/about_keras_models.html
/usr/lib64/R/library/keras/doc/applications.R
/usr/lib64/R/library/keras/doc/applications.Rmd
/usr/lib64/R/library/keras/doc/applications.html
/usr/lib64/R/library/keras/doc/backend.R
/usr/lib64/R/library/keras/doc/backend.Rmd
/usr/lib64/R/library/keras/doc/backend.html
/usr/lib64/R/library/keras/doc/custom_layers.R
/usr/lib64/R/library/keras/doc/custom_layers.Rmd
/usr/lib64/R/library/keras/doc/custom_layers.html
/usr/lib64/R/library/keras/doc/custom_models.R
/usr/lib64/R/library/keras/doc/custom_models.Rmd
/usr/lib64/R/library/keras/doc/custom_models.html
/usr/lib64/R/library/keras/doc/custom_wrappers.R
/usr/lib64/R/library/keras/doc/custom_wrappers.Rmd
/usr/lib64/R/library/keras/doc/custom_wrappers.html
/usr/lib64/R/library/keras/doc/eager_guide.R
/usr/lib64/R/library/keras/doc/eager_guide.Rmd
/usr/lib64/R/library/keras/doc/eager_guide.html
/usr/lib64/R/library/keras/doc/faq.R
/usr/lib64/R/library/keras/doc/faq.Rmd
/usr/lib64/R/library/keras/doc/faq.html
/usr/lib64/R/library/keras/doc/functional_api.R
/usr/lib64/R/library/keras/doc/functional_api.Rmd
/usr/lib64/R/library/keras/doc/functional_api.html
/usr/lib64/R/library/keras/doc/getting_started.R
/usr/lib64/R/library/keras/doc/getting_started.Rmd
/usr/lib64/R/library/keras/doc/getting_started.html
/usr/lib64/R/library/keras/doc/guide_keras.R
/usr/lib64/R/library/keras/doc/guide_keras.Rmd
/usr/lib64/R/library/keras/doc/guide_keras.html
/usr/lib64/R/library/keras/doc/index.html
/usr/lib64/R/library/keras/doc/saving_serializing.R
/usr/lib64/R/library/keras/doc/saving_serializing.Rmd
/usr/lib64/R/library/keras/doc/saving_serializing.html
/usr/lib64/R/library/keras/doc/sequential_model.R
/usr/lib64/R/library/keras/doc/sequential_model.Rmd
/usr/lib64/R/library/keras/doc/sequential_model.html
/usr/lib64/R/library/keras/doc/training_callbacks.R
/usr/lib64/R/library/keras/doc/training_callbacks.Rmd
/usr/lib64/R/library/keras/doc/training_callbacks.html
/usr/lib64/R/library/keras/doc/training_visualization.R
/usr/lib64/R/library/keras/doc/training_visualization.Rmd
/usr/lib64/R/library/keras/doc/training_visualization.html
/usr/lib64/R/library/keras/doc/tutorial_basic_classification.R
/usr/lib64/R/library/keras/doc/tutorial_basic_classification.Rmd
/usr/lib64/R/library/keras/doc/tutorial_basic_classification.html
/usr/lib64/R/library/keras/doc/tutorial_basic_regression.R
/usr/lib64/R/library/keras/doc/tutorial_basic_regression.Rmd
/usr/lib64/R/library/keras/doc/tutorial_basic_regression.html
/usr/lib64/R/library/keras/doc/tutorial_basic_text_classification.R
/usr/lib64/R/library/keras/doc/tutorial_basic_text_classification.Rmd
/usr/lib64/R/library/keras/doc/tutorial_basic_text_classification.html
/usr/lib64/R/library/keras/doc/tutorial_overfit_underfit.R
/usr/lib64/R/library/keras/doc/tutorial_overfit_underfit.Rmd
/usr/lib64/R/library/keras/doc/tutorial_overfit_underfit.html
/usr/lib64/R/library/keras/doc/tutorial_save_and_restore.R
/usr/lib64/R/library/keras/doc/tutorial_save_and_restore.Rmd
/usr/lib64/R/library/keras/doc/tutorial_save_and_restore.html
/usr/lib64/R/library/keras/doc/why_use_keras.R
/usr/lib64/R/library/keras/doc/why_use_keras.Rmd
/usr/lib64/R/library/keras/doc/why_use_keras.html
/usr/lib64/R/library/keras/help/AnIndex
/usr/lib64/R/library/keras/help/aliases.rds
/usr/lib64/R/library/keras/help/keras.rdb
/usr/lib64/R/library/keras/help/keras.rdx
/usr/lib64/R/library/keras/help/paths.rds
/usr/lib64/R/library/keras/html/00Index.html
/usr/lib64/R/library/keras/html/R.css
/usr/lib64/R/library/keras/python/kerastools/__init__.py
/usr/lib64/R/library/keras/python/kerastools/callback.py
/usr/lib64/R/library/keras/python/kerastools/constraint.py
/usr/lib64/R/library/keras/python/kerastools/generator.py
/usr/lib64/R/library/keras/python/kerastools/layer.py
/usr/lib64/R/library/keras/python/kerastools/model.py
/usr/lib64/R/library/keras/python/kerastools/progbar.py
/usr/lib64/R/library/keras/python/kerastools/wrapper.py
/usr/lib64/R/library/keras/tests/testthat.R
/usr/lib64/R/library/keras/tests/testthat/digit.jpeg
/usr/lib64/R/library/keras/tests/testthat/digit2.jpeg
/usr/lib64/R/library/keras/tests/testthat/digit_resized.jpeg
/usr/lib64/R/library/keras/tests/testthat/test-activations.R
/usr/lib64/R/library/keras/tests/testthat/test-applications.R
/usr/lib64/R/library/keras/tests/testthat/test-backend.R
/usr/lib64/R/library/keras/tests/testthat/test-callbacks.R
/usr/lib64/R/library/keras/tests/testthat/test-constraints.R
/usr/lib64/R/library/keras/tests/testthat/test-custom-layers.R
/usr/lib64/R/library/keras/tests/testthat/test-custom-models.R
/usr/lib64/R/library/keras/tests/testthat/test-custom_wrappers.R
/usr/lib64/R/library/keras/tests/testthat/test-datasets.R
/usr/lib64/R/library/keras/tests/testthat/test-examples.R
/usr/lib64/R/library/keras/tests/testthat/test-freeze.R
/usr/lib64/R/library/keras/tests/testthat/test-generators.R
/usr/lib64/R/library/keras/tests/testthat/test-initializers.R
/usr/lib64/R/library/keras/tests/testthat/test-layer-methods.R
/usr/lib64/R/library/keras/tests/testthat/test-layers.R
/usr/lib64/R/library/keras/tests/testthat/test-losses.R
/usr/lib64/R/library/keras/tests/testthat/test-metrics.R
/usr/lib64/R/library/keras/tests/testthat/test-model-persistence.R
/usr/lib64/R/library/keras/tests/testthat/test-model.R
/usr/lib64/R/library/keras/tests/testthat/test-optimizers.R
/usr/lib64/R/library/keras/tests/testthat/test-preprocessing.R
/usr/lib64/R/library/keras/tests/testthat/test-regularizers.R
/usr/lib64/R/library/keras/tests/testthat/test-tfdatasets.R
/usr/lib64/R/library/keras/tests/testthat/test-timeseries.R
/usr/lib64/R/library/keras/tests/testthat/test-utils.R
/usr/lib64/R/library/keras/tests/testthat/test.h5
/usr/lib64/R/library/keras/tests/testthat/train.R
/usr/lib64/R/library/keras/tests/testthat/utils.R
