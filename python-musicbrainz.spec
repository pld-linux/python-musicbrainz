Summary:	Python module for MusicBrainz
Summary(pl.UTF-8):	Moduł języka Python dla MusicBrainz
Name:		python-musicbrainz
Version:	1.0b1
Release:	2
License:	LGPL
Group:		Development/Languages/Python
Source0:	http://icepick.info/projects_old/python-musicbrainz/%{name}-%{version}.tar.gz
# Source0-md5:  8f07d75e67f3b2f1de89327126c0f418
URL:		http://icepick.info/projects/python-musicbrainz/
BuildRequires:	python-ctypes
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-modules
Requires:	python-ctypes
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The MusicBrainz client library is a development library geared towards
developers who wish to add MusicBrainz lookup capabilities to their
applications.

The client library includes the following features:
    * Lookup Audio CD metadata using CD Index Discids
    * Calculate Relatable TRM acoustic fingerprints
    * Search for artist/album/track titles
    * Lookup metadata by name, TRM ids or MusicBrainz Ids

%description -l pl.UTF-8
Biblioteka klienta MusicBrainz jest biblioteką rozwojową stworzoną dla
twórców oprogramowania, którzy chcą dodać mozliwości MusicBrainz do
swoich aplikacji.

Biblioteka kliencka posiada następujące możliwości:
    * Znajdowanie metadanych płyt Audio CD przy użyciu CD Index Discid
    * Obliczanie "odcisku palca" RTRM
    * Wyszukiwanie danych artysty/albumu/ścieżki
    * Wyszukiwanie metadanych po identyfikatorach TRM i MusicBrainz

%prep
%setup -q

%build
find -type f -exec sed -i -e 's|#!.*python.*|#!%{_bindir}/python|g' "{}" ";"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

python ./setup.py install --optimize=2 --root=$RPM_BUILD_ROOT
install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{py_sitescriptdir}/*.py[co]
%{_examplesdir}/%{name}-%{version}
