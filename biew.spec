Summary:	BIEW is Binary vIEWer and editor
Summary(pl):	BIEW jest przegl╠dark╠ plikСw binarnych z edytorem
Summary(ru):	biew - редактор двоичных файлов с дизассемблером
Summary(uk):	biew - редактор дв╕йкових файл╕в з дизасемблером
Name:		biew
Version:	532
Release:	1
License:	GPL
Group:		Applications/Editors
Source0:	http://dl.sourceforge.net/biew/%{name}-%{version}.tar.bz2
#Patch0:		%{name}-CURSES.patch
URL:		http://biew.sourceforge.net/
BuildRequires:	ncurses-devel
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BIEW is advanced Binary vIEWer with built-in editor for binary,
hexadecimal and disassembler modes. His disassembler supports many
processors (Pentium4, K7 Athlon, Cyrix-M2) and many file formats
(MZ, NE, PE, LE, LX, DOS.SYS, NLM, arch, ELF, a.out, coff32 PharLap,
rdoff).

%description -l pl
BIEW (Binary vIEWer) jest zaawansowan╠ przegl╠dark╠ i edytorem plikСw
binarnych. Zawiera wbudowany disasembler ze wsparciem dla wielu nowych
procesorСw (w tym Pentium4, Athlon i Cyrix-M2) oraz wielu formatСw
plikСw wykonywalnych (MZ, NE, PE, LE, LX, DOS.SYS, NLM, arch, ELF,
a.out, coff32 PharLap, rdoff).

%description -l ru
biew - это просмотрщик/редактор двоичных файлов с возможностью просмотра
и редактирования в двоичном, шестнадцатиричном и дизассемберном режимах.
Поддерживается выделение ассемблерных команд PentiumIV/K7-Athlon/Cyrix-M2,
есть конвертор кириллических кодировок, полный просмотр форматов MZ, NE, PE,
LE, LX, DOS.SYS, NLM, ELF.

%description -l uk
biew - це переглядач/редактор дв╕йкових файл╕в з можлив╕стю перегляду та
редагування в дв╕йковому, ш╕стнадцятковому та дизасемблерному режимах.
П╕дтриму╓ться вид╕лення асемберних команд PentiumIV/K7-Athlon/Cyrix-M2,
╓ конвертор кирил╕чних кодувань, повний перегляд формат╕в MZ, NE, PE, LE,
LX, DOS.SYS, NLM, ELF.

%prep
%setup -q
#%patch0 -p1

%build
%ifarch %{ix86}
 target=%{_target_cpu}
%else
 target=generic
%endif

%{__make} \
	TARGET_PLATFORM=$target \
	TARGET_OS=unix \
	INCS="-I. -I/usr/include/ncurses" \
	compilation=%{?debug:debug}%{!?debug:advance}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}/ $RPM_BUILD_ROOT%{_libdir}/biew/

install biew $RPM_BUILD_ROOT%{_bindir}
install bin_rc/{biew.hlp,skn/*} $RPM_BUILD_ROOT%{_libdir}/biew/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*txt doc/*.en
%lang(ru) %doc doc/*.ru
%attr(755,root,root) %{_bindir}/biew
%{_libdir}/biew
