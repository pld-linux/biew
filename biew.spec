Summary:	BIEW is Binary vIEWer and editor 
Summary(pl):	BIEW jest przegl�dark� plik�w binarnych z edytorem
Name:		biew
Version:	520
Release:	1
License:	GPL
Group:		Applications/Editors
Group(pl):	Aplikacje/Edytory
Source0:	ftp://biew.sourceforge.net/pub/biew/%{name}-%{version}.tar.bz2
Patch0:		biew-CURSES.patch
URL:		http://biew.sourceforge.net/
BuildRequires: ncurses-devel
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BIEW is advenced Binary vIEWer with built-in editor for binary,
hexadecimal and disassembler modes. His disassembler support many
procesors(Pentium4, K7 Athlon, Cyrix-M2) and many file formats(MZ, NE,
PE, LE, LX, DOS.SYS, NLM, arch, ELF, a.out, coff32 PharLap, rdoff)

%description -l pl
BIEW(Binary vIEWer) jest zaawansowan� przegl�dark� i edytorem plik�w
binarnych. Zawiera wbudowany disasembler z suportem dla wielu nowych
procesor�w(w tym Pentium4, Athlon i Cyrix-M2) oraz wielu format�w
plik�w wykonywalnych(MZ, NE, PE, LE, LX, DOS.SYS, NLM, arch, ELF,
a.out, coff32 PharLap, rdoff)

%prep

%setup -q 
%patch0 -p1

%build
%ifarch %{ix86}
 target=%{_target_cpu}
%else
 target=generic
%endif

%{__make} TARGET_PLATFORM=$target TARGET_OS=%{_target_os} compilation=advenced

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}/ $RPM_BUILD_ROOT%{_libdir}/biew/
install biew $RPM_BUILD_ROOT%{_bindir}
install bin_rc/biew.hlp $RPM_BUILD_ROOT%{_libdir}/biew/
install bin_rc/standard.skn $RPM_BUILD_ROOT%{_libdir}/biew/
gzip -9nf doc/*txt doc/*.en doc/*.ru

%clean 
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/biew
%dir %{_libdir}/biew
%{_libdir}/biew/*
%doc doc/biew_en.txt* doc/release.txt* doc/unix.txt*
