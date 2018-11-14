#############################################################################
# Generated by PAGE version 4.17
# in conjunction with Tcl version 8.6
# Oct 15, 2018 03:30:23 PM WIB  platform: Linux
set vTcl(timestamp) ""


if {!$vTcl(borrow)} {

vTcl:font:add_GUI_font TkDefaultFont \
"-family fixed -size 10 -weight normal -slant roman -underline 0 -overstrike 0"
vTcl:font:add_GUI_font TkFixedFont \
"-family fixed -size 10 -weight normal -slant roman -underline 0 -overstrike 0"
vTcl:font:add_GUI_font TkMenuFont \
"-family Helvetica -size -12 -weight normal -slant roman -underline 0 -overstrike 0"
vTcl:font:add_GUI_font TkTextFont \
"-family Helvetica -size -12 -weight normal -slant roman -underline 0 -overstrike 0"
set vTcl(actual_gui_bg) #f5deb3
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_menu_bg) #f5deb3
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #b2c9f4
set vTcl(analog_color_p) #eaf4b2
set vTcl(analog_color_m) #f4bcb2
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #f4bcb2
set vTcl(active_menu_fg) #000000
}

#################################
#LIBRARY PROCEDURES
#


if {[info exists vTcl(sourcing)]} {

proc vTcl:project:info {} {
    set base .top39
    global vTcl
    set base $vTcl(btop)
    if {$base == ""} {
        set base .top39
    }
    namespace eval ::widgets::$base {
        set dflt,origin 0
        set runvisible 1
    }
    namespace eval ::widgets_bindings {
        set tagslist _TopLevel
    }
    namespace eval ::vTcl::modules::main {
        set procs {
        }
        set compounds {
        }
        set projectType single
    }
}
}

#################################
# GENERATED GUI PROCEDURES
#

proc vTclWindow.top39 {base} {
    if {$base == ""} {
        set base .top39
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -menu "$top.m41" -background {#d9d9d9} -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 1036x600+147+144
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1425 870
    wm minsize $top 1 1
    wm overrideredirect $top 0
    wm resizable $top 0 0
    wm deiconify $top
    wm title $top "Treadmill"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    labelframe $top.lab40 \
        -foreground black -text {Treadmill Mode} -background {#d9d9d9} \
        -height 325 -highlightcolor black -width 980 
    vTcl:DefineAlias "$top.lab40" "Labelframe1" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.lab40
    button $site_3_0.but42 \
        -activebackground {#d9d9d9} -activeforeground black \
        -background {#d9d9d9} -command start -font TkFixedFont \
        -foreground {#000000} -highlightcolor black -text Recovery 
    vTcl:DefineAlias "$site_3_0.but42" "mode1" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but43 \
        -activebackground {#d9d9d9} -activeforeground black \
        -background {#d9d9d9} -command start -font TkFixedFont \
        -foreground {#000000} -highlightcolor black -text Aerobic 
    vTcl:DefineAlias "$site_3_0.but43" "mode2" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but44 \
        -activebackground {#d9d9d9} -activeforeground black \
        -background {#d9d9d9} -command start -font TkFixedFont \
        -foreground {#000000} -highlightcolor black -justify left \
        -text {Extensive Endurance} 
    vTcl:DefineAlias "$site_3_0.but44" "mode3" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but45 \
        -activebackground {#d9d9d9} -activeforeground black \
        -background {#d9d9d9} -command start -foreground {#000000} \
        -highlightcolor black -text {Intensive Endurance} -width 122 
    vTcl:DefineAlias "$site_3_0.but45" "mode4" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but46 \
        -activebackground {#d9d9d9} -activeforeground black \
        -background {#d9d9d9} -command start -font font18 \
        -foreground {#000000} -highlightcolor black -state active \
        -text {Anaerobic Treshold} 
    vTcl:DefineAlias "$site_3_0.but46" "mode5" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but47 \
        -activebackground {#d9d9d9} -activeforeground black \
        -background {#d9d9d9} -command start -foreground {#000000} \
        -highlightcolor black -text {Maximum Aerobic} 
    vTcl:DefineAlias "$site_3_0.but47" "mode6" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.but42 \
        -in $site_3_0 -x 20 -y 30 -width 132 -relwidth 0 -height 265 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but43 \
        -in $site_3_0 -x 180 -y 30 -width 132 -relwidth 0 -height 265 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but44 \
        -in $site_3_0 -x 340 -y 30 -width 132 -relwidth 0 -height 265 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but45 \
        -in $site_3_0 -x 500 -y 30 -width 132 -relwidth 0 -height 265 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but46 \
        -in $site_3_0 -x 660 -y 30 -width 132 -relwidth 0 -height 265 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but47 \
        -in $site_3_0 -x 820 -y 30 -width 132 -relwidth 0 -height 265 \
        -relheight 0 -anchor nw -bordermode ignore 
    label $top.lab41 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -font font9 -foreground {#000000} \
        -highlightcolor black -text iTreadmill 
    vTcl:DefineAlias "$top.lab41" "Label1" vTcl:WidgetProc "Toplevel1" 1
    labelframe $top.lab48 \
        -foreground black -text Settings -background {#d9d9d9} -height 135 \
        -highlightcolor black -width 980 
    vTcl:DefineAlias "$top.lab48" "Labelframe2" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.lab48
    button $site_3_0.but49 \
        -activebackground {#d9d9d9} -activeforeground black \
        -background {#d9d9d9} -command register -font TkFixedFont \
        -foreground {#000000} -highlightcolor black -text Register 
    vTcl:DefineAlias "$site_3_0.but49" "register" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but50 \
        -activebackground {#d9d9d9} -activeforeground black \
        -background {#d9d9d9} -command connect -font TkFixedFont \
        -foreground {#000000} -highlightcolor black -state active \
        -text {Connect Mi Band} 
    vTcl:DefineAlias "$site_3_0.but50" "connect" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but51 \
        -activebackground {#d9d9d9} -activeforeground black \
        -background {#d9d9d9} -command other -font TkFixedFont \
        -foreground {#000000} -highlightcolor black -text {Other Settings} 
    vTcl:DefineAlias "$site_3_0.but51" "other" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.but49 \
        -in $site_3_0 -x 20 -y 30 -width 292 -relwidth 0 -height 85 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but50 \
        -in $site_3_0 -x 340 -y 30 -width 292 -height 85 -anchor nw \
        -bordermode ignore 
    place $site_3_0.but51 \
        -in $site_3_0 -x 660 -y 30 -width 292 -height 85 -anchor nw \
        -bordermode ignore 
    set site_3_0 $top.m41
    menu $site_3_0 \
        -activebackground {#f4bcb2} -activeforeground {#000000} \
        -background {#f5deb3} -font TkMenuFont -foreground {#000000} \
        -tearoff 0 
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.lab40 \
        -in $top -x 30 -y 90 -width 980 -relwidth 0 -height 325 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab41 \
        -in $top -x 40 -y 40 -anchor nw -bordermode ignore 
    place $top.lab48 \
        -in $top -x 30 -y 430 -width 980 -relwidth 0 -height 135 -relheight 0 \
        -anchor nw -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

#############################################################################
## Binding tag:  _TopLevel

bind "_TopLevel" <<Create>> {
    if {![info exists _topcount]} {set _topcount 0}; incr _topcount
}
bind "_TopLevel" <<DeleteWindow>> {
    if {[set ::%W::_modal]} {
                vTcl:Toplevel:WidgetProc %W endmodal
            } else {
                destroy %W; if {$_topcount == 0} {exit}
            }
}
bind "_TopLevel" <Destroy> {
    if {[winfo toplevel %W] == "%W"} {incr _topcount -1}
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top39 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}
