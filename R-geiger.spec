#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-geiger
Version  : 2.0.6.1
Release  : 5
URL      : https://cran.r-project.org/src/contrib/geiger_2.0.6.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/geiger_2.0.6.1.tar.gz
Summary  : Analysis of Evolutionary Diversification
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-geiger-lib = %{version}-%{release}
Requires: R-ape
Requires: R-coda
Requires: R-colorspace
Requires: R-deSolve
Requires: R-mvtnorm
Requires: R-ncbit
Requires: R-subplex
BuildRequires : R-ape
BuildRequires : R-coda
BuildRequires : R-colorspace
BuildRequires : R-deSolve
BuildRequires : R-mvtnorm
BuildRequires : R-ncbit
BuildRequires : R-subplex
BuildRequires : buildreq-R

%description
# Geiger
[![Build Status](https://travis-ci.org/mwpennell/geiger-v2.png?branch=master)](https://travis-ci.org/mwpennell/geiger-v2)

%package lib
Summary: lib components for the R-geiger package.
Group: Libraries

%description lib
lib components for the R-geiger package.


%prep
%setup -q -c -n geiger

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1547653991

%install
export SOURCE_DATE_EPOCH=1547653991
rm -rf %{buildroot}
export LANG=C
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library geiger
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library geiger
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library geiger
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/geiger/CITATION
/usr/lib64/R/library/geiger/DESCRIPTION
/usr/lib64/R/library/geiger/INDEX
/usr/lib64/R/library/geiger/Meta/Rd.rds
/usr/lib64/R/library/geiger/Meta/data.rds
/usr/lib64/R/library/geiger/Meta/features.rds
/usr/lib64/R/library/geiger/Meta/hsearch.rds
/usr/lib64/R/library/geiger/Meta/links.rds
/usr/lib64/R/library/geiger/Meta/nsInfo.rds
/usr/lib64/R/library/geiger/Meta/package.rds
/usr/lib64/R/library/geiger/NAMESPACE
/usr/lib64/R/library/geiger/R/geiger
/usr/lib64/R/library/geiger/R/geiger.rdb
/usr/lib64/R/library/geiger/R/geiger.rdx
/usr/lib64/R/library/geiger/data/amphibia.rda
/usr/lib64/R/library/geiger/data/caniformia.rda
/usr/lib64/R/library/geiger/data/carnivores.rda
/usr/lib64/R/library/geiger/data/caudata.rda
/usr/lib64/R/library/geiger/data/chelonia.rda
/usr/lib64/R/library/geiger/data/geospiza.rda
/usr/lib64/R/library/geiger/data/primates.rda
/usr/lib64/R/library/geiger/data/whales.rda
/usr/lib64/R/library/geiger/help/AnIndex
/usr/lib64/R/library/geiger/help/aliases.rds
/usr/lib64/R/library/geiger/help/geiger.rdb
/usr/lib64/R/library/geiger/help/geiger.rdx
/usr/lib64/R/library/geiger/help/paths.rds
/usr/lib64/R/library/geiger/html/00Index.html
/usr/lib64/R/library/geiger/html/R.css

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/geiger/libs/geiger.so
/usr/lib64/R/library/geiger/libs/geiger.so.avx2
/usr/lib64/R/library/geiger/libs/geiger.so.avx512
