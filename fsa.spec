%define name	fsa
%define version 0.45
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Finite state automata package
Group:		Sciences/Computer science
License:	Freeware
URL:		http://www.eti.pg.gda.pl/~jandac/fsa.html
Source:		ftp://ftp.pg.gda.pl/pub/software/xtras-PG/fsa/%{name}_%{version}.tar.gz
Patch:		%{name}_0.41.fileselect-shellbang.patch.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This package contains several finite state automata-based utilities for:
- spellchecking
- diacritic restoration
- morphological analysis and synthesis
- acquisition of data for morphological descriptions
- perfect hashing

%package tcl
Summary:        Tcl/Tk interface for %{name}
Group:          Sciences/Computer science
Requires:       %{name} = %{version}

%description tcl
Tcl/Tk interface for %{name}.

%prep
%setup -q -n s_fsa
%patch

%build
%make CPPFLAGS="\
  $RPM_OPT_FLAGS \
  -DFLEXIBLE  \
  -DNUMBERS \
  -DA_TERGO \
  -DGENERALIZE \
  -DSORT_ON_FREQ \
  -DSHOW_FILLERS  \
  -DSTOPBIT \
  -DNEXTBIT \
  -DMORE_COMPR \
  -DCASECONV \
  -DRUNON_WORDS \
  -DMORPH_INFIX \
  -DPOOR_MORPH \
  -DCHCLASS \
  -DGUESS_LEXEMES -DGUESS_PREFIX \
  -DGUESS_MMORPH \
  -DDUMP_ALL"

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_mandir}/{man1,man5}
install -d -m 755 %{buildroot}%{_datadir}/%{name}/{dict,tclmacq}
make PREFIXDIR=%{buildroot}%{_prefix} \
     MANDIR=%{buildroot}%{_mandir} \
     DICTDIR=%{buildroot}%{_datadir}/%{name}/dict \
     LISPDIR=%{buildroot}%{_libdir}/emacs/site-lisp \
     TCLMACQDIR=%{buildroot}%{_datadir}/%{name}/tclmacq \
     install
mv %{buildroot}%{_bindir}/simplify.pl %{buildroot}%{_bindir}/simplify-fsa.pl

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES INSTALL README TROUBLESHOOTING
%{_bindir}/*
%{_mandir}/*/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/dict
%exclude %{_bindir}/*.tcl

%files tcl
%defattr(-,root,root)
%doc CHANGES INSTALL README TROUBLESHOOTING
%{_bindir}/*.tcl
%{_datadir}/%{name}/tclmacq

