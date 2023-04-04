#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
#
Name     : R-geiger
Version  : 2.0.11
Release  : 45
URL      : https://cran.r-project.org/src/contrib/geiger_2.0.11.tar.gz
Source0  : https://cran.r-project.org/src/contrib/geiger_2.0.11.tar.gz
Summary  : Analysis of Evolutionary Diversification
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-geiger-lib = %{version}-%{release}
Requires: R-Rcpp
Requires: R-ape
Requires: R-coda
Requires: R-colorspace
Requires: R-deSolve
Requires: R-digest
Requires: R-mvtnorm
Requires: R-ncbit
Requires: R-phytools
Requires: R-subplex
BuildRequires : R-Rcpp
BuildRequires : R-ape
BuildRequires : R-coda
BuildRequires : R-colorspace
BuildRequires : R-deSolve
BuildRequires : R-digest
BuildRequires : R-mvtnorm
BuildRequires : R-ncbit
BuildRequires : R-phytools
BuildRequires : R-subplex
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Geiger
## Major features
geiger is a (growing) collection of methods developed over the years by many researchers.
Here is a a non-comprehensive list of methods:

%package lib
Summary: lib components for the R-geiger package.
Group: Libraries

%description lib
lib components for the R-geiger package.


%prep
%setup -q -n geiger

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1680620848

%install
export SOURCE_DATE_EPOCH=1680620848
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
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
