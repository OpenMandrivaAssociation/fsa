Name:		fsa
Version:	0.51
Release:	2
Summary:	Finite state automata package
Group:		Sciences/Computer science
License:	Freeware
URL:		http://www.eti.pg.gda.pl/~jandac/fsa.html
Source:		ftp://ftp.pg.gda.pl/pub/software/xtras-PG/fsa/%{name}_%{version}.tar.gz
Patch:		%{name}_0.41.fileselect-shellbang.patch.bz2

%description
This package contains several finite state automata-based utilities for:
- spellchecking
- diacritic restoration
- morphological analysis and synthesis
- acquisition of data for morphological descriptions
- perfect hashing

%package tcl
Summary:	Tcl/Tk interface for %{name}
Group:		Sciences/Computer science
Requires:	%{name} = %{version}-%{release}

%description tcl
Tcl/Tk interface for %{name}.

%prep
%setup -q -n s_fsa
%patch

%build
%make CPPFLAGS="\
  %{optflags} \
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

%files
%doc CHANGES INSTALL README TROUBLESHOOTING
%{_bindir}/*
%{_mandir}/*/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/dict
%exclude %{_bindir}/*.tcl

%files tcl
%doc CHANGES INSTALL README TROUBLESHOOTING
%{_bindir}/*.tcl
%{_datadir}/%{name}/tclmacq

%changelog
* Tue Mar 04 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.45-1mdv2008.1
+ Revision: 178403
- new version

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Dec 18 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.42-4mdv2008.1
+ Revision: 132434
- rebuild

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request
    - import fsa


* Tue Aug 29 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.42-3mdv2007.0
- Rebuild

* Wed Aug 17 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.42-2mdk
- fix description (Adam Williamson <awilliamson@mandriva.com>)
- %%mkrel  

* Wed Aug 17 2005 Guillaume Rousse <guillomovitch@zarb.org> 0.42-1mdk
- new version
- new GPL license allow inclusion in contrib
- fix conflict with anomy-sanitizer by renaming the problematic file (fix #45)

* Tue Jun 14 2005 Guillaume Rousse <guillomovitch@zarb.org> 0.41-2plf
- spec cleanup 
- less strict dependencies between packages
- fix missing shellbang

* Sun Nov 28 2004 Guillaume Rousse <guillomovitch@zarb.org> 0.41-1plf
- new version 
- fix license

* Tue Oct 05 2004 Guillaume Rousse <guillomovitch@zarb.org> 0.40-1plf 
- new version
- plf reason
- drop patch0 (merged upstream)

* Fri Jun 11 2004 Guillaume Rousse <guillomovitch@zarb.org> 0.39-1plf 
- new version
- tcl files in a subpackage
- keep default compilation options
- fix segfault for out-of-size array index
- rpmbuildupdate aware

* Fri Jun 11 2004 Guillaume Rousse <guillomovitch@zarb.org> 0.37-3plf 
- remove tcl files to avoid dependencies

* Tue Mar 02 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.37-2plf
- fix build
- Conflicts: anomy-sanitizer (%%_bindir/simplify)

* Tue Dec 16 2003 Guillaume Rousse <guillomovitch@zarb.org> 0.37-1plf
- first plf release
