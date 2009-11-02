# NOTE:
# - slang (recommented screen lib) doesn't have mouse support
Summary:	BIEW is Binary vIEWer and editor
Summary(pl.UTF-8):	BIEW jest przeglądarką plików binarnych z edytorem
Summary(ru.UTF-8):	biew - редактор двоичных файлов с дизассемблером
Summary(uk.UTF-8):	biew - редактор двійкових файлів з дизасемблером
Name:		biew
Version:	602
Release:	1
License:	GPL
Group:		Applications/Editors
Source0:	http://dl.sourceforge.net/biew/%{name}-%{version}-src.tar.bz2
# Source0-md5:	3226a466ae5989d7e12a947bc8e76ed4
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

%description -l pl.UTF-8
BIEW (Binary vIEWer) jest zaawansowaną przeglądarką i edytorem plików
binarnych. Zawiera wbudowany disasembler ze wsparciem dla wielu nowych
procesorów (w tym Pentium4, Athlon i Cyrix-M2) oraz wielu formatów
plików wykonywalnych (MZ, NE, PE, LE, LX, DOS.SYS, NLM, arch, ELF,
a.out, coff32 PharLap, rdoff).

%description -l ru.UTF-8
biew - это просмотрщик/редактор двоичных файлов с возможностью
просмотра и редактирования в двоичном, шестнадцатиричном и
дизассемберном режимах. Поддерживается выделение ассемблерных команд
PentiumIV/K7-Athlon/Cyrix-M2, есть конвертор кириллических кодировок,
полный просмотр форматов MZ, NE, PE, LE, LX, DOS.SYS, NLM, ELF.

%description -l uk.UTF-8
biew - це переглядач/редактор двійкових файлів з можливістю перегляду
та редагування в двійковому, шістнадцятковому та дизасемблерному
режимах. Підтримується виділення асемберних команд
PentiumIV/K7-Athlon/Cyrix-M2, є конвертор кирилічних кодувань, повний
перегляд форматів MZ, NE, PE, LE, LX, DOS.SYS, NLM, ELF.

%prep
%setup -q

%build
./configure --prefix=%{_prefix}
%{__make} \
	PREFIX=%{_prefix} \
	CC="%{__cc}" \
	HOST_CFLAGS="%{rpmcflags} -mmmx -msse" \
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
