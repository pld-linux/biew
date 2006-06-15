# NOTE:
# - slang (recommented screen lib) doesn't have mouse support
Summary:	BIEW is Binary vIEWer and editor
Summary(pl):	BIEW jest przegl╠dark╠ plikСw binarnych z edytorem
Summary(ru):	biew - редактор двоичных файлов с дизассемблером
Summary(uk):	biew - редактор дв╕йкових файл╕в з дизасемблером
Name:		biew
Version:	562
Release:	2
License:	GPL
Group:		Applications/Editors
Source0:	http://dl.sourceforge.net/biew/%{name}%{version}.tar.bz2
# Source0-md5:	622fb1f02a6d921b273f0a39407f8e7d
URL:		http://biew.sourceforge.net/
BuildRequires:	gpm-devel
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BIEW is advanced Binary vIEWer with built-in editor for binary,
hexadecimal and disassembler modes. His disassembler supports many
processors (Pentium4, K7 Athlon, Cyrix-M2) and many file formats (MZ,
NE, PE, LE, LX, DOS.SYS, NLM, arch, ELF, a.out, coff32 PharLap,
rdoff).

%description -l pl
BIEW (Binary vIEWer) jest zaawansowan╠ przegl╠dark╠ i edytorem plikСw
binarnych. Zawiera wbudowany disasembler ze wsparciem dla wielu nowych
procesorСw (w tym Pentium4, Athlon i Cyrix-M2) oraz wielu formatСw
plikСw wykonywalnych (MZ, NE, PE, LE, LX, DOS.SYS, NLM, arch, ELF,
a.out, coff32 PharLap, rdoff).

%description -l ru
biew - это просмотрщик/редактор двоичных файлов с возможностью
просмотра и редактирования в двоичном, шестнадцатиричном и
дизассемберном режимах. Поддерживается выделение ассемблерных команд
PentiumIV/K7-Athlon/Cyrix-M2, есть конвертор кириллических кодировок,
полный просмотр форматов MZ, NE, PE, LE, LX, DOS.SYS, NLM, ELF.

%description -l uk
biew - це переглядач/редактор дв╕йкових файл╕в з можлив╕стю перегляду
та редагування в дв╕йковому, ш╕стнадцятковому та дизасемблерному
режимах. П╕дтриму╓ться вид╕лення асемберних команд
PentiumIV/K7-Athlon/Cyrix-M2, ╓ конвертор кирил╕чних кодувань, повний
перегляд формат╕в MZ, NE, PE, LE, LX, DOS.SYS, NLM, ELF.

%prep
%setup -q

%build
%{__make} \
	PREFIX=%{_prefix} \
	CC="%{__cc}" \
	HOST_CFLAGS="%{rpmcflags}" \
%ifarch %{ix86}
	TARGET_PLATFORM=%{_target_cpu} \
%else
	TARGET_PLATFORM=generic \
%endif
	TARGET_SCREEN_LIB=curses \
	TARGET_OS=unix \
	USE_MOUSE=y \
	INCS="-I. -I/usr/include/ncurses" \
	compilation=%{?debug:debug}%{!?debug:advance}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name},%{_mandir}/man1}

install biew $RPM_BUILD_ROOT%{_bindir}
install bin_rc/{biew.hlp,skn/*} $RPM_BUILD_ROOT%{_datadir}/biew
cp -a bin_rc/{xlt,skn,*.hlp} $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -a bin_rc/syntax/*.stx $RPM_BUILD_ROOT%{_datadir}/biew
cp -a doc/biew.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*txt doc/*.en
%lang(ru) %doc doc/*.ru
%attr(755,root,root) %{_bindir}/biew
%{_datadir}/%{name}
%{_mandir}/man1/biew*
