package chessgame;

import javax.imageio.ImageIO;
import javax.swing.*;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.util.LinkedList;

public class ChessGame {
    public static void main(String[] args) throws IOException {
        LinkedList<Piece> pieces = new LinkedList<>();

        BufferedImage all = ImageIO.read(new File("images/chess.png"));
        Image imgs[] = new Image[12];

        int idx = 0;
        for (int y = 0; y < 400; y += 200) {
            for (int x = 0; x < 1200; x += 200) {
                imgs[idx] = all.getSubimage(x, y, 200, 200).getScaledInstance(64, 64, BufferedImage.SCALE_SMOOTH);
                idx++;
            }
        }
        Piece brook=new Piece(0, 0, false, "rook", pieces);
        Piece bkinght=new Piece(1, 0, false, "knight", pieces);
        Piece bbishop=new Piece(2, 0, false, "bishop", pieces);
        Piece bqueen=new Piece(3, 0, false, "queen", pieces);
        Piece bking=new Piece(4, 0, false, "king", pieces);
        Piece bbishop2=new Piece(5, 0, false, "bishop", pieces);
        Piece bkight2=new Piece(6, 0, false, "knight", pieces);
        Piece brook2=new Piece(7, 0, false, "rook", pieces);
        Piece bpawn1=new Piece(1, 1, false, "pawn", pieces);
        Piece bpawn2=new Piece(2, 1, false, "pawn", pieces);
        Piece bpawn3=new Piece(3, 1, false, "pawn", pieces);
        Piece bpawn4=new Piece(4, 1, false, "pawn", pieces);
        Piece bpawn5=new Piece(5, 1, false, "pawn", pieces);
        Piece bpawn6=new Piece(6, 1, false, "pawn", pieces);
        Piece bpawn7=new Piece(7, 1, false, "pawn", pieces);
        Piece bpawn8=new Piece(0, 1, false, "pawn", pieces);

        Piece wrook=new Piece(0, 7, true, "rook", pieces);
        Piece wkinght=new Piece(1, 7, true, "knight", pieces);
        Piece wbishop=new Piece(2, 7, true, "bishop", pieces);
        Piece wqueen=new Piece(3, 7, true, "queen", pieces);
        Piece wking=new Piece(4, 7, true, "king", pieces);
        Piece wbishop2=new Piece(5, 7, true, "bishop", pieces);
        Piece wkight2=new Piece(6, 7, true, "knight", pieces);
        Piece wrook2=new Piece(7, 7, true, "rook", pieces);
        Piece wpawn1=new Piece(1, 6, true, "pawn", pieces);
        Piece wpawn2=new Piece(2, 6, true, "pawn", pieces);
        Piece wpawn3=new Piece(3, 6, true, "pawn", pieces);
        Piece wpawn4=new Piece(4, 6, true, "pawn", pieces);
        Piece wpawn5=new Piece(5, 6, true, "pawn", pieces);
        Piece wpawn6=new Piece(6, 6, true, "pawn", pieces);
        Piece wpawn7=new Piece(7, 6, true, "pawn", pieces);
        Piece wpawn8=new Piece(0, 6, true, "pawn", pieces);


        JFrame frame = new JFrame();
        frame.setBounds(10, 10, 512, 512);
        frame.setUndecorated(true);
        JPanel pn = new JPanel() {
            boolean white = true;

            @Override
            public void paint(Graphics g) {
                for (int y = 0; y < 8; y++) {
                    for (int x = 0; x < 8; x++) {
                        if (white) {
                            g.setColor(new Color(235,235, 208));
                        }else{
                            g.setColor(new Color(119, 148, 85));
                        }
                        g.fillRect(x * 64, y * 64, 64, 64);
                        white = !white;
                    }
                    white = !white;
                }

                for (Piece p : pieces) {
                    int idx = 0;
                    if (p.name.equalsIgnoreCase("king")) {
                        idx = 0;
                    }
                    if (p.name.equalsIgnoreCase("queen")) {
                        idx = 1;
                    }
                    if (p.name.equalsIgnoreCase("bishop")) {
                        idx = 2;
                    }
                    if (p.name.equalsIgnoreCase("knight")) {
                        idx = 3;
                    }
                    if (p.name.equalsIgnoreCase("rook")) {
                        idx = 4;
                    }
                    if (p.name.equalsIgnoreCase("pawn")) {
                        idx = 5;
                    }

                    if (!p.isWhite) {
                        idx += 6;
                    }
                    g.drawImage(imgs[idx], p.xp * 64, p.yp * 64, this);
                }

            }
        };
        frame.add(pn);
        frame.setDefaultCloseOperation(3);
        frame.setVisible(true);
    }
}
